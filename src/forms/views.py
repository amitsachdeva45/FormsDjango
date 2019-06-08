from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def forms(request):
    return HttpResponse("<h2>Forms Views</h1>")
