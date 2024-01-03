from django import forms
from .models import Book
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'rented_books']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['booktitle', 'picture', 'info', 'creator', 'release']

class PostSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Posts', max_length=100)


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')