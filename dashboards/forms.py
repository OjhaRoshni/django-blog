from django import forms
from blogs.models import Category

class categoryForms(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'