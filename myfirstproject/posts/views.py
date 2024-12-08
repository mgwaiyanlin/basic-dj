from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    posts = Posts.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_page(request, slug):
    post = Posts.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login_view/")
def post_new(request):
    return render(request, "posts/post_new.html")

