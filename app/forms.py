from django import forms
from app.models import *
class Topicforms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
   
