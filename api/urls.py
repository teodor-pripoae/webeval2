from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^login/$', 'api.views.login'),
    (r'^get-job/$', 'api.views.return_job'),
    (r'^update-job/$', 'api.views.update_job'),
    (r'^create-eval/$', 'api.views.create_eval'),
    (r'^get-your-score/$', 'api.views.get_your_score'),
    (r'^check_if_username-exists/$', 'api.views.check_if_username_exists')
)
