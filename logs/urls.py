from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView 
from django.urls import path
from logs import views


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.register, name="register"),
    path('home/', views.home, name='home'), 
]
