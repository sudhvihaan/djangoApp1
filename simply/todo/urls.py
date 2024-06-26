from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),  # Ensure 'login' is the correct URL name
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user-logout/', views.user_logout, name='user-logout'),
]
