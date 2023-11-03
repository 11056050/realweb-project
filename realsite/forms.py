from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['booktitle', 'picture', 'info', 'creator', 'release']

class PostSearchForm(forms.Form):
    search_query = forms.CharField(label='Search Posts', max_length=100)