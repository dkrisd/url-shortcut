from django.urls import path
from . import views

app_name = 'urlshortcut'

urlpatterns = [
    path('urls/',
         views.UrlListView.as_view(),
         name='url_list'),

    path('urls/<pk>/',
         views.UrlDetailView.as_view(),
         name='url_detail'),
]