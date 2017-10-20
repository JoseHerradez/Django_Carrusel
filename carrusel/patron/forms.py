from patron.models import Carousel, Content

from django import forms

class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ('title', 'count', 'timer', 'circular', 'auto',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.NumberInput(attrs={'class': 'form-control'}),
            'circular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'auto': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'timer': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        #image = forms.ImageField(widget=forms.ImageField)
        fields = ('title', 'description', 'url', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }
