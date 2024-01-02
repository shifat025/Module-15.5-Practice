from django import forms
from .models import musicians

class profile_Form(forms.ModelForm):
    class Meta:
        model = musicians
        fields = '__all__'