from django import forms
from app.models import *

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=32)


class UserRegisterForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = UserProfile
        exclude = ('avatar', 'wiki_page', 'last_login', 'date_joined', 'rating', 'reputation', 'forum_posts', 'developer')
    def is_valid(self):
        valid = forms.ModelForm.is_valid(self)

        if not valid:
            return False

        if re.match(r"^[\w\.]+$", self.data['username']) is None:
            valid = False
            self.errors['username'] = 'Username contains invalid characters. Please use only letters, numbers, . and _. '

        if len(self.data['password']) < 6 :
            valid = False
            self.errors['password'] = 'Password too short. Must be at least 6 characters. '

        if self.data['password'] != self.data['password2']:
            valid = False
            self.errors['password'] = 'Passwords didn\'t match. '

        if email_re.match(self.data['email']) is None:
            valid = False
            self.errors['email'] += 'Please enter a valid email. '
        elif User.objects.filter(email = self.data['email']):
            valid = False
            self.errors['email'] = 'There is another account with this email address. Please enter other email address.'

        return valid


class UserEditAccountForm(forms.ModelForm):
    #captcha = ReCaptchaField()
    class Meta:
        model = UserProfile
        exclude = ('wiki_page', 'last_login', 'date_joined', 'rating', 'reputation', 'forum_posts', 'username', 'developer')



