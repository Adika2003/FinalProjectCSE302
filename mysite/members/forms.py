from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'role_type', 'role', 'batch', 'reg_no', 'email', 'photo']
