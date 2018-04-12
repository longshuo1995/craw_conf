from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url('^main$', views.main),
    url('^check$', views.check),
    url('^insert$', views.insert),
    url('^', views.main)
]
