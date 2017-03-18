from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    return render(request, 'ag/index.html')

def play(request):
    print("play")
    return HttpResponseRedirect("/ag/")

def stop(request):
    print("stop")
    return HttpResponseRedirect("/ag/")
