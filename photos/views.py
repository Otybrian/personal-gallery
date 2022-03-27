from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.views import View
from photos.models import Image, category
# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')

def display_page(request):
    image = Image.objects.all()
    return render(request, 'all.html', {'image':image} )

def viewDetails(request):
    image = Image.objects.all()
    return render(request, 'details.html', {'image':image} )

def my_category(request):
    categorys = category.objects.all()
    context = {
        'categorys': categorys,
    }
    return render(request, 'category.html', context)


def search_results(request):

    if 'category_name' in request.GET and request.GET["category_name"]:
        search_term = request.GET.get("category_name")
    
        searched_category_name = category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"category_name": searched_category_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


