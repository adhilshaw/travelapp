from xml.etree.ElementInclude import include

from django.template.context_processors import static

from . import views, admin
from django.urls import path

urlpatterns = [

    path('', views.demo, name='demo')
    # path('add/', views.addition, name='addition'),

]
