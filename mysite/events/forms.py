from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title','slug','description','start_time','end_time','location','club']
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type':'datetime-local'}),
        }
