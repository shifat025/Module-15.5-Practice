from django.shortcuts import render,redirect
from . import forms
from album import models

# Create your views here.
def add_profile(request):
    if request.method == 'POST':
        profileform = forms.profile_Form(request.POST)
        if profileform.is_valid():
            profileform.save()
            return redirect('profile')
    
    else:
        profileform = forms.profile_Form()
    return render(request, 'musician.html', {'form' : profileform})





