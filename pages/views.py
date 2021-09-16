from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect

# Create your views here.

def about(request):
	return render(request , 'core/about.html')


def services(request):
	return render(request , 'core/services.html')
