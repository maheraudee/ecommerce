from dataclasses import Field
from importlib.metadata import files
from pyexpat import model
from django import forms

from .models import Reserve

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['name','email', 'message', 'date', 'time','nperson']
