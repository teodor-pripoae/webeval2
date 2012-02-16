from django import forms
from app.models import *

class ForumTopicCreateForm (forms.Form):
    title = models.CharField(max_length=128)
    content = models.TextField()


class ForumPostEditForm (forms.ModelForm):
    class Meta:
        model = ForumPost
        exclude = ('topic', 'author', 'date')


class PrivateMessageForm (forms.ModelForm):
    class Meta:
        model = PrivateMessage
        exclude = ('date', 'user_from')

class ForumPostReplyForm (forms.ModelForm):
    class Meta:
        model = ForumPost
        exclude = ('topic', 'author', 'date')


