from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['title', 'text', 'rating']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})

class BookReleaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['booktitle', 'picture', 'info', 'creator', 'release', 'available_copies', 'rented_by', 'status']

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