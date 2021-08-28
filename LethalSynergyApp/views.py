from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def about(request):
  return render(request,'about.html')

def supported(request):
  return render(request, 'supported.html')

def ffxiv(request):
  return render(request, 'ffxiv.html')

def lost_ark(request):
  return render(request, 'lost_ark.html')

def eso(request):
  return render(request, 'eso.html')