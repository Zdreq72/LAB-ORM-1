from django.shortcuts import render, redirect 
from django.http import HttpResponse , HttpRequest
from django.utils import timezone
from .models import Post



def home(request):
    posts = Post.objects.all()
    return render(request, "blogger/home.html", {"posts": posts})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, "blogger/all_posts.html", {"posts": posts})

def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        content = request.POST.get("content", "").strip()
        is_published = request.POST.get("is_published") == "on"
        publisher = request.POST.get("publisher", "").strip()
        image = request.FILES.get("post_image")

        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                published_at=timezone.now(),
                publisher=publisher,
                post_image=image,
            )
            return redirect("blogger:home")

    return render(request, "blogger/add_post.html")


def post_detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("blogger:home")

    return render(request, "blogger/detail.html", {"post": post})


def edit_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("blogger:home")

    if request.method == "POST":
        post.title = request.POST.get("title", "").strip()
        post.content = request.POST.get("content", "").strip()
        post.is_published = request.POST.get("is_published") == "on"
        post.publisher = request.POST.get("publisher", "").strip()

        image = request.FILES.get("post_image")
        if image:
            post.post_image = image

        post.save()
        return redirect("blogger:detail", post_id=post.id)

    return render(request, "blogger/edit_post.html", {"post": post})


def delete_post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        return redirect("blogger:home")

    if request.method == "POST":
        post.delete()
        return redirect("blogger:home")

    return redirect("blogger:detail", post_id=post.id)
