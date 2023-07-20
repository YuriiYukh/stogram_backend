from django.db import models
from django.contrib.auth.models import User


class Poster(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, db_column='id')
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    image = models.ImageField(upload_to="images/profile_images")
    birth_date = models.DateField(null=True, blank=True, default="")
    registered_at = models.DateField(auto_now=True)
    description = models.CharField(
        max_length=2000, null=True, blank=True, default="")


class Post(models.Model):
    image = models.ImageField(upload_to="images/post_images")
    description = models.CharField(
        max_length=2000, null=True, blank=True, default="")
    created = models.DateField(auto_now=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Vote(models.Model):
    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
