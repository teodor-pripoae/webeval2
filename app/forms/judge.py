from django import forms
from app.models import *

class ContestCreateForm (forms.ModelForm):
    class Meta:
        model = Contest
        exclude = ('start_time', 'end_time', 'name', 'wiki_page', 'with_rating', 'with_open_eval', 'problems', 'registered_users')


class ContestEditForm (forms.ModelForm):
    #formfield_callback=parsefield_callback
    class Meta:
        model = Contest
        exclude = ('wiki_page', 'problems', 'registered_users')
        #widgets = {
        #    'start_time' : forms.DateTimeInput(),
        #    'end_time' : forms.DateTimeInput(),
        #}



class JobSubmitForm (forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('percent_completed', 'processing', 'message', 'type', 'date', 'source_size', 'user', 'score', 'private')


class ProblemCreateForm (forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ('name', 'owner', 'resource', 'author', 'type',
                   'time_limit', 'memory_limit', 'source_limit',
                   'forum_topic', 'wiki_page',  'type', 'tags')


class ProblemEditForm (forms.ModelForm):
    class Meta:
        model = Problem
        exclude = ('wiki_page', 'forum_topic', 'type', 'author', 'owner', 'tags')


