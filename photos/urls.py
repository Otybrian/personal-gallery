from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('display/',views.display_page,name = 'allImages'),
    path('search/',views.search_results,name = 'search_results'),
]


