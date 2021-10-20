from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def about(request):
  return render(request,'about.html')

def ffxiv(request):
  return render(request, 'ffxiv.html')

def lost_ark(request):
  return render(request, 'lost_ark.html')

def elyon(request):
  return render(request, 'elyon.html')

def eso(request):
  return render(request, 'eso.html')