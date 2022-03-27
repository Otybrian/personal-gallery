from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^display/$',views.display_page,name = 'display'),
    url('^category/$',views.my_category,name = 'category'),
    url('^search/', views.search_results, name='search_results'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)