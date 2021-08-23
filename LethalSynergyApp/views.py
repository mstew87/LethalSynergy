from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def about(request):
  return render(request,'about.html')

def supported(request):
  return render(request, 'supported.html')