from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^jsconfig$', views.jsconfig, name='jsconfig'),
    url(r'^vote/(?P<question_id>[0-9]+)$', views.vote, name='vote'),
    url(r'^savevote/$', views.saveVote, name='savevote'),
    url(r'^detail/(?P<question_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^topfivepolls/$', views.topFivePolls, name='topfivepolls'),
]