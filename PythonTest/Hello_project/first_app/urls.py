

from django.conf.urls import url

from . import views

urlpattrens = [
    url(' ', views.HomePageView,name = 'Home')
]
