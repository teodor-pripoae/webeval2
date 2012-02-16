import json
from django.http import HttpResponse

def ajax_response(message, object_data = None, code = 0):
    response = {'message' : message, 'code': code}

    if object_data is not None:
        response['object'] = object_data

    return HttpResponse(json.dumps(response))

def ajax_no_perm():
    return ajax_response("You don't have permission to do that.", code = 1)


def serialize_form_errors(form):
    return [(k, v[0]) for k, v in form.errors.items()]
