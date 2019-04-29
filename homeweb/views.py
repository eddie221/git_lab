from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
	context = {}
	context['hello'] = "Hello world! It is really hard to use this."
    #return HttpResponse("Hello, world. You're at the homeweb index.")
	return render(request, 'hello.html', context)