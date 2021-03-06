"""urlshortcut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from urlshort import views
from urlshort import api

urlpatterns = [
    path('', views.all_url_shortcuts, name="index"),
    path('login', views.login_page),
    path('create-url', views.create_url),
    path('<pk>/delete', views.UrlDelete.as_view(), name="url_delete"),
    path('admin', admin.site.urls),
    path('<shortcut>', views.redirect_shortcut),
    path('api/', include('urlshort.api.urls', namespace='api')),

]
