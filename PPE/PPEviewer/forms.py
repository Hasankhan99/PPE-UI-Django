from django import forms
from .models import feedback,ppeviwer


class PPEviewerForm(forms.ModelForm):
    
    class Meta:
        model = feedback
        fields = '__all__'
class ppForm(forms.ModelForm):
    class Meta:
        model=ppeviwer
        fields='__all__'
