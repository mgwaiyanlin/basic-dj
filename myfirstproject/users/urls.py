from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register_user/', views.register_view, name="register"),
    path('login_view/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
