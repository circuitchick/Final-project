from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import BlogEntry

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=BlogEntry.objects.all().order_by("-date")[:20],template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=BlogEntry, template_name="blog/blogentry.html")),
]