from django.conf.urls import url
from . import views


ulrpatterns = [
    url(r'^$', views.gallery, name = 'gallery'),
    url(r'^viewPhoto$/', views.viewPhoto, name = 'viewPhoto'),
    url(r'^search/', views.search_results, name = 'search_results')

]