from django.shortcuts import render
from django.views import generic
from .models import ExlFile


class Index(generic.ListView):
    model = ExlFile
    template_name = "index.html"
