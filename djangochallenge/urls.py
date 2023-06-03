#-*- coding: utf-8 -*-
from django.conf import settings
# from django.conf.urls import include
from django.urls import include, re_path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include("mailer.urls")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
