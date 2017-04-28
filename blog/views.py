from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.core.urlresolvers import reverse

class IndexView(generic.ListView): #<<-- since you just changed this to IndexView, be sure to update index to IndexView in urls.py 
    "Thoughts from the Peanut Gallery"
    