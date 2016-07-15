
from django.contrib import admin

from peerreviews.views import ReviewerViewSet, ReviewslistFilteredViewSet, ReviewslistViewSet, SubmissionEvallistViewSet, EmailViewSet, ReviewslistIdViewSet, UserViewSet
from django.conf.urls import include, url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'reviewers', ReviewerViewSet)
router.register(r'reviewslists', ReviewslistViewSet)
router.register(r'submissionevals',SubmissionEvallistViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^api/reviewslists/(?P<pk>[0-9]+)/', ReviewslistIdViewSet.as_view(), name='reviewslistid'),
    url(r'^api/reviewers/(?P<rid>[0-9]+)/reviews/', ReviewslistFilteredViewSet.as_view(), name='reviewerslist'),
    url(r'^api/emails/', EmailViewSet.as_view(), name='email'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/', include(router.urls)),
]
