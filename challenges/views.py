from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def jan(request):
    return HttpResponse('January Goal!')

def feb(request):
    return HttpResponse('February Goal!')
