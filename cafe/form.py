from dataclasses import Field
from importlib.metadata import files
from pyexpat import model
from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput

from .models import Reserve

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['name','email', 'message', 'date', 'time','nperson']
        widgets = {
        'date': DatePickerInput(
             options={
                    "format": "MM/DD/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }
        ),
        'time': TimePickerInput(),
    }
