from django.urls import path
from . import views

app_name = "blogger"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_post, name="add_post"),
    path("<int:post_id>/", views.post_detail, name="detail"),
    path("<int:post_id>/edit/", views.edit_post, name="edit"),
    path("<int:post_id>/delete/", views.delete_post, name="delete"),
    path("all_posts/", views.all_posts, name="all_posts"),
]
