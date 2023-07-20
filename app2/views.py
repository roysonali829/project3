from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def demo(request):
    return HttpResponse('<i>data that you have to response</i>')
def bristi(request):
    return HttpResponse('<marquee>Hii, i am here....</marquee>')