from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from logs import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='logs/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.register, name="register"),
]
