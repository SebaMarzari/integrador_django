from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    pass

User._meta.get_field('groups').related_name = 'blog_users'
User._meta.get_field('user_permissions').related_name = 'blog_users_permissions'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
