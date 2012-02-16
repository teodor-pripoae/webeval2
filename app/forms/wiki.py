from django import forms
from app.models import *


class WikiRevisionEditForm (forms.ModelForm):
    forum_topic = models.IntegerField()
    class Meta:
        model = WikiRevision
        exclude = ('revision_id', 'date', 'ip', 'wiki_page', 'author')


