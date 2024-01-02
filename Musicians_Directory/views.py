from django.shortcuts import render
from album.models import albums

def home(request):
    data = albums.objects.all()
    return render(request,'home.html', {'data':data})