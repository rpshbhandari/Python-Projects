from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request) -> HttpResponse:
    posts = Post.objects.all()
    return render(request, 'NoStylesApp/home.html', {'posts': posts})

def detail(request, post_id) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'NoStylesApp/detail.html', {'post': post})
