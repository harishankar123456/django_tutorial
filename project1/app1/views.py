from django.shortcuts import render
from django.http import HttpResponse
def print_hello(request):
        return HttpResponse("Hello django")

def home(request):
    return HttpResponse("Welcome to the home page!")