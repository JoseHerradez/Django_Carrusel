from django import forms
from breadcrumbs.models import BreadcrumbsLevels, BreadcrumbsContent


class BreadcrumbsForm(forms.ModelForm):
    class Meta:
        model = BreadcrumbsLevels
        fields = ('niveles',)
        widgets = {
            'niveles': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = BreadcrumbsContent
        fields = ('title', 'url',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }
