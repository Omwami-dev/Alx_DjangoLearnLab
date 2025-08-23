from django.contrib import admin
from .models import Post, Comment # adjust if your Post import differs


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
list_display = ("id", "post", "author", "created_at", "updated_at")
list_filter = ("created_at", "updated_at", "author")
search_fields = ("content", "author__username", "post__title")


# If not already registered
# admin.site.register(Post)
