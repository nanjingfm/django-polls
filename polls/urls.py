from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^vote/(?P<question_id>[0-9]+)$', views.vote, name='vote'),
    url(r'^savevote/$', views.saveVote, name='savevote'),
    url(r'^detail/$', views.detail, name='detail'),
]