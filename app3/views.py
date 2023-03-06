from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apple(request):
    return HttpResponse('<h1><marquee>apples are famous in jammu and simla</h1>')