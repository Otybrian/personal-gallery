from django.conf.urls import url
from django.urls import path
from . import views


ulrpatterns = [
    url(r'^$', views.gallery, name = 'gallery'),
    path('photo/<str:pk>', views.viewPhoto, name = 'viewPhoto'),
    url(r'^search/', views.search_results, name = 'search_results')

]