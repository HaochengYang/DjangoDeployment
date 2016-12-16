from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check$', views.check, name='check'),
    url(r'^blog_and_comment$', views.blog_and_comment, name='blog_and_comment'),
    url(r'^add_to/(?P<id>\d+)$', views.add_to, name='add_to'),
    url(r'^show_information/(?P<id>\d+)$', views.show_information, name='show_information'),
]
