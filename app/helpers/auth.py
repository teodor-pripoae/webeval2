import random
import string

#def user_auth(request):
    #if request.user.is_authenticated():
        #return request.user.customer
    #return None


from django.core.validators import email_re

def user_auth (request):
    if request.user.is_anonymous():
        return None
    return request.user.userprofile

def email_is_valid(email):
    return True if email_re.match(email) else False
