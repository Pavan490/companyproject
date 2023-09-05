from django.shortcuts import render
from django.http import HttpResponse
def demo(request):
    return HttpResponse("this is a demo")