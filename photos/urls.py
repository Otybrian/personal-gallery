from django.conf.urls import url
from . import views


ulrpatterns = [
    url(r'^$', views.gallery, name = 'gallery'),
    url(r'^addPhoto$/', views.addPhoto, name = 'addPhoto'),
    url(r'^search/', views.search_results, name = 'search_results')

]