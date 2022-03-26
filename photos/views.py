from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt

from photos.models import Image, category
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

def display_page(request):
    image = Image.objects.all()
    return render(request, 'all.html', {'image':image} )



