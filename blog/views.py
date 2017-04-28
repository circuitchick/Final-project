from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.conf.urls import url, include
from blog.models import BlogEntry
from django.core.urlresolvers import reverse
urlpatterns = [ 
 url(r'^$', ListView.as_view( queryset=BlogEntry.objects.all().order_by("-date")[:20],template_name="blog/blog.html")),
            ]
                                    