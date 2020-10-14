# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. From index WelcomeLite index view")

def add_offer(request):
    return HttpResponse("We made it to the add offers page!")

def edit_offer(request):
    return HttpResponse("Another page for editing offers")