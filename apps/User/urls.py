from django.conf.urls import url
from .models import User
from . import views
urlpatterns = [
    url(r'^$',views.index, name="index"),
    url(r'^register$',views.register, name="register"),
    url(r'^login$',views.login, name="login"),
    url(r'^main$',views.main, name="main"),
    url(r'^logout$',views.logout, name="logout")
]
