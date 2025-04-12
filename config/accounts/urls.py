from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register_view, login_view, dashboard_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),  # Dashboard page
]
