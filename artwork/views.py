from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from .models import webContent, Artpiece



def home(request):
    # think about making this another static .py file to change later
    # also add in my welcome message to it instead of hard coded?
   
    content = webContent()
    context = content.getDictionary()
    return render(request, 'portfolio/index.html', context)

def sketchbook(request):
    return HttpResponse("This is the sketchbook page.")

def about(request):
    content = webContent()
    context = content.getDictionary()
    return render(request, 'portfolio/about.html', context)


def contact(request):
    content = webContent()
    context = content.getDictionary()
    return render(request, 'portfolio/contact.html', context)


class portfolioView(generic.ListView):
    template_name = 'portfolio/portfolio.html'
    context_object_name = 'image_list'
    model = Artpiece
    

# def portfolio(request):

    # return render(request, 'portfolio/portfolio.html')

# Create your views here.

# make a template that is returned with a context
# import anything i'll need in the html templates here in the views
