from django.urls import path, re_path
from . import views
from myapp.views import login_view, profile_view, logout_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('', login_view.as_view(), name='login'),
    # re_path(r'^profile$', profile_view.as_view()),
    path('profile/<str:username>/', profile_view.as_view(), name='profile'),
    path('signin/', auth_view.LoginView.as_view(template_name='signin.html'), name='signin'),
    re_path(r'^logout.html$', logout_view.as_view(), name='logout_view'),
]