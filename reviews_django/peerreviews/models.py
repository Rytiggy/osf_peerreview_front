from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
import hashlib

import datetime


class Reviewer(models.Model):
    user = models.OneToOneField(User,default=None)
    name = models.CharField(max_length=200)
    affiliation = models.TextField(null=True)
    email = models.EmailField(default=None)
    bio = models.TextField(null=True)
    research = models.TextField(null=True)
    website = models.URLField(null=True)
    osfreviews = models.IntegerField(default=0)
    avatar = models.ImageField(blank=True, null=True, upload_to='media/avatars')

class Author(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(default=None)


class Reviewslist(models.Model):

    conference = models.TextField(null=True)
    title = models.TextField(null=True)
    reviewdeadline = models.DateField(default=None)
    reviewer = models.ForeignKey(Reviewer)
    author = models.ManyToManyField(Author)
    status = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)
    attachment = models.FileField(blank=True, null=True, upload_to='media/files')



class submissionevals(models.Model):

    #reviewer = models.OneToOneField(Reviewer)
    #submission = models.OneToOneField(Reviewslist)
    premise = models.IntegerField(default=0)
    research = models.IntegerField(default=0)
    style = models.IntegerField(default=0)
    comment = models.TextField(null=True)


    @property
    def total(self):
        return self.premise + self.research + self.style

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'

    def account_verified(self):
        if self.user.is_authenticated:
            result = EmailAddress.objects.filter(email=self.user.email)
            if len(result):
                return result[0].verified
        return False

    def profile_image_url(self):
        fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='osf')
        if len(fb_uid):
            return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)
        return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
