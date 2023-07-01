from django.shortcuts import render, get_object_or_404
from .models import Post, Comment

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/list_posts.html', {'posts': posts})

def view_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment = Comment.objects.filter(post=post)
    return render(request, 'blog/view_post.html', {'post': post, 'comments': comment})
