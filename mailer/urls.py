#-*- coding: utf-8 -*-
# from django.conf.urls import include
from django.urls import path, re_path

from mailer.views import IndexView
from django.views.decorators.cache import cache_page
from django.core.cache import cache


urlpatterns = [
    path('', cache_page(60 * 60)(IndexView.as_view()), name="index"),  # Cache for 60 minutes
]
