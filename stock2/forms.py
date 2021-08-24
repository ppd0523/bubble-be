from django import forms

from .models import *

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ('cond_name', 'cond_owner', 'file')
