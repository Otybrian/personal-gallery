from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def display_page(request):
    image = Image.display_images()
    return render(request, 'all.html', {"image":image})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})