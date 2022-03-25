from django.shortcuts import render, redirect
import datetime as dt



# Create your views here.

def gallery(request):


    return render(request, 'gallery.html')

def search_results(request):


    return render(request, 'search.html')
