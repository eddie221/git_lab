from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	context = {}
	context['hello'] = "Hello world!!!!"
    #return HttpResponse("Hello, world. You're at the homeweb index.")
	return render(request, 'hello.html', context)