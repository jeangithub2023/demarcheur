from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views
from django.conf import settings

from accounts.forms import LoginForm
from accounts.views import register

app_name='accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='accounts/logout.html', next_page='accounts:login'), name='logout'),
    path('register/', register, name='register')
] 