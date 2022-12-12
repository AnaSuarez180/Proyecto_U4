"""Portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp.views import signin_view, login_view, logout_view, ProfileView, RegistroView
from django.conf import settings
from django.urls import re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view.as_view(), name='login'),
    re_path(r'^logout.html$', logout_view.as_view(), name='logout_view'),
    path('signin/', signin_view.as_view(), name='signin'),
    path('accounts/login/profile/<str:username>/', ProfileView.items_view, name='profile'),
    path('registro/', RegistroView.as_view(), name='registro')
    # path('profile/<str:username>/', profile_view, name='profile', kwargs={'username': 'default_username'})
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
