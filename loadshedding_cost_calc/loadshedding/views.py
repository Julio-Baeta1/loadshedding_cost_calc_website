from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Duration

def home(request):
    return HttpResponse("Home page")

#class IndexView(generic.ListView):
#    template_name = "loadshedding/index.html"
