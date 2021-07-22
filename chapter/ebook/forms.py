from django import forms
from ebook.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['bookname','mainimage','preview_text','pdf']

