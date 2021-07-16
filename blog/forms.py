from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Author, Contact

#Updating Author profile
class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['image']

#Updating User/Author Profle
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

#User contact form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'mobile', 'message']
