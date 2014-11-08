from django.conf.urls import patterns, url

from isler import views

urlpatterns = patterns('',
                       url(r'^bugun/$', views.bugun, name='bugun'),
                       url(r'^not_kaydi/$', views.not_kaydi, name='not_kaydi'),
                       url(r'^problem_kaydi/$', views.problem_kaydi, name='problem_kaydi'),
                       url(r'^gorev_kaydi/$', views.gorev_kaydi, name='gorev_kaydi'),
                       url(r'^hatirlatma_kaydi/$', views.hatirlatma_kaydi, name='hatirlatma_kaydi'),
                       )
                     