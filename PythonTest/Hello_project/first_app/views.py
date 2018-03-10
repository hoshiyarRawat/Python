# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView,DeleteView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post,PostBlog
from django.urls import reverse_lazy
# Create your views here.

#"""def HomePageView(request):
 #   return HttpResponse('Hello World page test')"""

class HomePageView(ListView):
    model = PostBlog
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogCreateView(CreateView):
    model = PostBlog
    template_name = 'post_new.html'
    fields = '__all__'

class BlogDetailView(DetailView):
    model = PostBlog
    template_name = 'post_detail.html'
    context_object_name = 'Detail'

class BlogPostUpdate(UpdateView):
    model = PostBlog
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogPostDelete(DeleteView):
    model = PostBlog
    template_name = 'post_delete.html'
    context_object_name = 'Detail'
    success_url= reverse_lazy('home')
