from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_article(request):
    return HttpResponse("Hello, article!")