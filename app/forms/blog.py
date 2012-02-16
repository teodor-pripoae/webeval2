from django import forms
from app.models import *


class BlogEntryCreateForm (forms.ModelForm):
    class Meta:
        model = BlogEntry
        exclude = ('permalink', 'author', 'date', 'tags')


class BlogEntryEditForm (forms.ModelForm):
    class Meta:
        model = BlogEntry
        exclude = ('permalink', 'author', 'date', 'tags')




