from datetime import time
from django.conf import settings
from django.contrib import auth
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING, SET_DEFAULT, SET_NULL
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=SET_NULL, null=True)
    text = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)


class MyUser(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    #gender = models.TextChoices('Man', 'Woman')
    date_of_birth = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.login