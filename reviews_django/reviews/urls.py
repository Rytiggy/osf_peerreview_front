from django.conf.urls import include, url

from django.contrib.staticfiles.urls import static
from django.conf import settings



admin.autodiscover()

urlpatterns = [

    url(r'', include('peerreviews.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^authenticate/', AuthenticateUser.as_view(), name='authenticate'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
