from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('Portfolio Home')
def contact(request):
    return HttpResponse('Contact me')

def greet_by_name(request, name):
    return HttpResponse(f'Your name is {name}')    
