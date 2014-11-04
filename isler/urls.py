from django.conf.urls import patterns, url

from isler import views

urlpatterns = patterns('',
                       url(r'^bugun/$', views.bugun, name='bugun'),
                       url(r'^not_kaydi/$', views.not_kaydi, name='not_kaydi'),
                       )
                     