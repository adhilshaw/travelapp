from xml.etree.ElementInclude import include

from django.template.context_processors import static

from . import views, admin
from django.urls import path

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')

]
