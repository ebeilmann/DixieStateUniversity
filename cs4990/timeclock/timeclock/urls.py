from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^', include('checkin.urls', namespace='checkin')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
