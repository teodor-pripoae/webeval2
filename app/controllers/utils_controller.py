import datetime

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect
from annoying.functions import get_object_or_None

from config.judge import *
from app.helpers.auth import user_auth
from app.models import *
from app.forms import *


def redirect_to_index(message):
    return HttpResponseRedirect(reverse('dashboard') + "?error_message=%s" % message)

def redirect_with_message(page, message):
    return HttpResponseRedirect(page + "?error_message=%s" % message)


