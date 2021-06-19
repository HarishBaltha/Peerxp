"""Project5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
#from App5 import urls as core_urls
from App5 import views
from Project5 import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register, name="register"),
    path('register_up/', views.register_up, name="register_up"),
    path('login/', views.login, name="login"),
    path('login_up/', views.login_up, name="login_up"),
    path('twitter/', views.twitter, name="twitter"),
    path('twitter_up/', views.twitter_up, name="twitter_up"),
    path('home/', views.home, name="home"),
    path('home_save/', views.home_save, name="home_save"),
    path('view/', views.view, name="view"),
    path('login1', views.login1, name="login1"),
    path('update/', views.update, name="update"),
    path('update_save/', views.update_save, name="update_save"),
    path('viewall/', views.viewall, name="viewall"),
    path('delete/', views.delete, name="delete"),
    path('social-auth/', include('social_django.urls', namespace='social')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
