from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView 
from django.urls import path
from logs import views
from .views import home

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.register, name="register"),
    path('home/', home, name='home'), 
]
