from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpRequest
from django.utils import timezone
from .models import Post




def home(request):
    posts = Post.objects.filter(is_published=True)
    return render(request, "blogger/home.html", {"posts": posts})


def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                published_at=timezone.now(),
            )
            return redirect("blogger:home")

    return render(request, "blogger/add_post.html")