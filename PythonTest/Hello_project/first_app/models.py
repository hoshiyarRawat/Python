# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    text= models.TextField()
    date= models.DateField()


    def __str__(self):
        """A string representation of the model"""

        return self.text[:50]

class PostBlog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.id)])

    def __str__(self):
        return self.title
