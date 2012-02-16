import random
import string

def user_auth(request):
    if request.user.is_authenticated():
        return request.user.customer
    return None


