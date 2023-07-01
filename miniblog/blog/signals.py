from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post, Comment, User

@receiver(post_save, sender=Post)
def update_post_count(sender, instance, created, **kwargs):
    if created:
        autor = instance.autor
        autor.posts_count = Post.objects.filter(autor=autor).count()
        autor.save()

@receiver(post_save, sender=Comment)
def update_comments_count(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.comments_count = Comment.objects.filter(post=post).count()
        post.save()
