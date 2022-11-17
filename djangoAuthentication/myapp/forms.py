from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('__all__')



from django.contrib.auth import forms
from django.contrib.auth import get_user_model

class CustomUserCreationForm(forms.UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "age"]
        field_classes = {"username": forms.UsernameField}