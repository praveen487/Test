from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexview(request):
    return HttpResponse("<h2><i>hello world</i></h2> <h1>Something BIG is coming</h1>")
