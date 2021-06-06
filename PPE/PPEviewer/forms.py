from django import forms
from .models import feedback


class PPEviewerForm(forms.ModelForm):
    
    class Meta:
        model = feedback
        fields = '__all__'
