from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index2'),
    path('tweet', views.index, name='index'),  # make it index/
    path('tweets/$', views.main, name='tweets'),
    path('graph', views.graph, name='graph')
]
