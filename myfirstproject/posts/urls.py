from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('posts_list/', views.posts_list, name="list"),
    path('post_new/', views.post_new, name="post_new"),
    path('<slug:slug>', views.post_page, name="page"),
]
