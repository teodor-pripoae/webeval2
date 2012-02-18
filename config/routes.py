from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # url(r'^webEval/', include('webEval.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),

    url(r'^$', 'app.controllers.wiki_controller.dashboard', name="dashboard"),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon.ico$', 'django.views.generic.simple.redirect_to', {'url': '%s/images/favicon.ico' % settings.MEDIA_URL}),

    url(r'^blog/new-entry/$', 'app.controllers.blog_controller.new_entry', name="new_entry"),
    url(r'^blog/comments/posted/$', 'app.controllers.blog_controller.comment_posted', name="comment_posted"),
    url(r'^blog/comments/', include('django.contrib.comments.urls')),
    url(r"^blog/delete_comment/(\d+)/$", "app.controllers.blog_controller.delete_comment", name="delete_blog_comment"),
    url(r"^blog/delete_comment/(\d+)/(\d+)/$", "app.controllers.blog_controller.delete_comment", name="delete_blog_comment"),

    url(r'^blog/(?P<username>[\w_.-@]+)/(?P<permalink>[\w-]+)/edit/$', 'app.controllers.blog_controller.edit_entry', name="edit_entry"),
    url(r'^blog/(?P<username>[\w_.-@]+)/(?P<permalink>[\w-]+)/delete/$', 'app.controllers.blog_controller.delete_entry', name="delete_entry"),
    url(r'^blog/(?P<username>[\w_.-@]+)/(?P<permalink>[\w-]+)/toogle-dashboard/$', 'app.controllers.blog_controller.toggle_dashboard', name="toggle_dashboard"),
    url(r'^blog/(?P<username>[\w_.-@]+)/(?P<permalink>[\w-]+)/$', 'app.controllers.blog_controller.display_entry', name="display_entry"),
    url(r'^blog/(?P<username>[\w_.-@]+)/$', 'app.controllers.blog_controller.index', name="blog_posts"),
    url(r'^blog/$', 'app.controllers.blog_controller.index', name="blog_posts"),

    url(r'^contests/$', 'app.controllers.grader_controller.display_all_contests', name="display_all_contests"),
    url(r'^contest/(?P<contest_code>\w+)/$', 'app.controllers.grader_controller.display_contest', name="display_contest"),
    url(r'^contest/(?P<contest_code>\w+)/toogle-registration/$', 'app.controllers.grader_controller.toggle_contest_registration', name="toggle_contest_registration"),
    url(r'^contest/(?P<contest_code>\w+)/edit/$', 'app.controllers.grader_controller.edit_contest_statement', name="edit_contest_statement"),
    url(r'^contest/(?P<contest_code>\w+)/configure/$', 'app.controllers.grader_controller.configure_contest', name="configure_contest"),
    url(r'^contest/(?P<contest_code>\w+)/users-registered/$', 'app.controllers.grader_controller.display_contest_registered_users', name="display_contest_registered_users"),
    url(r'^contest/(?P<contest_code>\w+)/standings/$', 'app.controllers.grader_controller.display_contest_standings', name="display_contest_standings"),

    url(r'^forum/board/(?P<board_id>\d+)/$', 'app.controllers.forum_controller.display_board', name="display_board"),
    url(r'^forum/topic/(?P<topic_id>\d+)/$', 'app.controllers.forum_controller.display_topic', name="display_topic"),
    url(r'^forum/topic/(?P<topic_id>\d+)/reply/$', 'app.controllers.forum_controller.reply', name="forum_reply"),
    url(r'^forum/board/(?P<board_id>\d+)/new-topic/$', 'app.controllers.forum_controller.new_topic', name="new_topic"),
    url(r'^forum/post/(?P<post_id>\d+)/edit/$', 'app.controllers.forum_controller.edit_post', name="edit_forum_post"),
    url(r'^forum/post/(?P<post_id>\d+)/move/$', 'app.controllers.forum_controller.move_post', name="move_forum_post"),
    url(r'^forum/post/(?P<post_id>\d+)/delete/$', 'app.controllers.forum_controller.delete_post', name="delete_forum_post"),
    url(r'^forum/private-messages/new/', 'app.controllers.user_controller.new_private_message', name="new_private_message"),
    url(r'^forum/private-messages/$', 'app.controllers.user_controller.private_messages', name="private_messages"),

    url(r'^admin/$', 'app.controllers.grader_controller.admin_page', name="admin_page"),
    url(r'^admin/create-problem/', 'app.controllers.grader_controller.create_problem', name="create_problem"),
    url(r'^admin/create-contest/', 'app.controllers.grader_controller.create_contest', name="create_contest"),

    url(r'^problem/(?P<problem_code>\w+)/$', 'app.controllers.grader_controller.display_problem', name="display_problem"),
    url(r'^problem/(?P<problem_code>\w+)/edit/$', 'app.controllers.grader_controller.edit_problem_statement', name="edit_problem_statement"),
    url(r'^problem/(?P<problem_code>\w+)/configure/$', 'app.controllers.grader_controller.configure_problem', name="configure_problem"),
    url(r'^problem/(?P<problem_code>\w+)/edit-tags/$', 'app.controllers.grader_controller.edit_problem_tags', name="edit_problem_tags"),
    url(r'^problems-by-author/(?P<author_code>\w+)/$', 'app.controllers.grader_controller.display_problems_by_author', name="display_problems_by_author"),

    url(r'^status/$', 'app.controllers.grader_controller.status', name="grader_status"),
    url(r'^status/job/(?P<job_id>\d+)/details/$', 'app.controllers.grader_controller.display_job', name="display_job"),
    url(r'^status/job/(?P<job_id>\d+)/source-code/$', 'app.controllers.grader_controller.display_job_source_code', name="display_job_source_code"),

    url(r'^submit/$', 'app.controllers.grader_controller.submit', name="submit_source"),

    url(r'^tickets/$', 'app.controllers.utils_controller.tickets', name="tickets"),
    url(r'^tickets/new/$', 'app.controllers.utils_controller.new_ticket', name="new_ticket"),
    url(r"^tickets/(?P<ticket_id>\d+)/delete_comment/$", "app.controllers.utils_controller.delete_comment", name="delete_ticket_comment"),
    url(r"^tickets/(?P<ticket_id>\d+)/delete_comment/(?P<comment_id>\d+)/$", "app.controllers.utils_controller.delete_comment", name="delete_ticket_comment"),
    url(r'^ticket/(?P<ticket_id>\d+)/$', 'app.controllers.utils_controller.display_ticket', name="display_ticket"),
    url(r'^ticket/(?P<ticket_id>\d+)/edit/$', 'app.controllers.utils_controller.edit_ticket', name="edit_ticket"),

    url(r'^captcha/', include('captcha.urls')),
    url(r'^auth/successful-login/$', 'app.controllers.auth_controller.successful_login', name="successful_login"),
    url(r'^auth/login/$', 'app.controllers.auth_controller.login', name="login"),
    url(r'^auth/facebook-login/$', 'app.controllers.auth_controller.facebook_login', name="facebook_login"),

   # url(r'^openid/', include('django_openid_auth.urls')),
    url(r'^auth/openid-login/$', 'django_openid_auth.views.login_begin', name='openid-login'),
    url(r'^auth/openid-login-complete/$', 'django_openid_auth.views.login_complete', name='openid-complete'),
    url(r'^auth/openid-logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
    url(r'^auth/logout/$', 'app.controllers.auth_controller.logout'),

    url(r'^auth/twitter-login/$', 'app.controllers.auth_controller.twitter_login', name="twitter_login"),
    url(r'^auth/twitter-login/return/$', 'app.controllers.auth_controller.twitter_return', name="twitter_return"),

    url(r'^auth/register/$', 'app.controllers.auth_controller.register', name="register"),
    url(r'^auth/succesful-register/', 'app.controllers.auth_controller.successful_register', name="successful_register"),

    url(r'^user/(?P<user_name>[\w_.]+)/$', 'app.controllers.user_controller.display_user', name="display_user"),
    url(r'^user/(?P<user_name>[\w_.]+)/edit/$', 'app.controllers.user_controller.edit_user_description', name="edit_user_description"),
    url(r'^user/(?P<user_name>[\w_.]+)/edit-account/$', 'app.controllers.user_controller.edit_user_account', name="edit_user_account"),
    url(r'^user/(?P<user_name>[\w_.]+)/get-avatar/$', 'app.controllers.user_controller.get_avatar', name="get_avatar"),
    url(r'^user/(?P<user_name>[\w_.]+)/rating/$', 'app.controllers.user_controller.display_user_rating', name="display_user_rating"),
    url(r'^user/(?P<user_name>[\w_.]+)/statistics/$', 'app.controllers.user_controller.display_user_statistics', name="display_user_statistics"),
    url(r'^user/(?P<user_name>[\w_.]+)/validate-key/(?P<validation_key>\w+)/$', 'app.controllers.auth_controller.validate_user', name="validate_user"),

    url(r'^api/get_rounds_for_problem', 'app.controllers.grader_controller.get_rounds_for_problem', name="get_rounds_for_problem"),
    url(r'^api/search_tags/$', 'app.controllers.blog_controller.get_tags_ajax', name="get_tags_ajax"),
    url(r'^api/register_form/$', 'app.controllers.auth_controller.register_remote_form', name="register_remote_form"),
    url(r'^api/login_form/$', 'app.controllers.auth_controller.login_remote_form', name="login_remote_form"),

    url(r'^ranks/$', 'app.controllers.grader_controller.ranks', name="ranks"),

    url(r'^wiki/$', 'app.controllers.wiki_controller.wiki_index', name="wiki_index"),
    url(r'^wiki/create-wiki-page/$', 'app.controllers.wiki_controller.create_wiki_page', name="create_wiki_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/attach/$', 'app.controllers.wiki_controller.attach', name="attach"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/attachments/$', 'app.controllers.wiki_controller.attachments', name="attachments"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/attachment/(?P<hash>\w+)/rename/$', 'app.controllers.wiki_controller.rename_attachment', name="rename_attachment"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/attachment/(?P<hash>\w+)/delete/$', 'app.controllers.wiki_controller.delete_attachment', name="delete_attachment"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/attachment/(?P<hash>\w+)/$', 'app.controllers.wiki_controller.display_attachment', name="display_attachment"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/download-attachments/$', 'app.controllers.wiki_controller.download_attachments', name="download_attachments"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/copy/$', 'app.controllers.wiki_controller.copy_page', name="copy_wiki_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/diff/$', 'app.controllers.wiki_controller.diff', name="wiki_diff"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/edit/$', 'app.controllers.wiki_controller.edit_page', name="edit_wiki_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/history/$', 'app.controllers.wiki_controller.history', name="wiki_history"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/move/$', 'app.controllers.wiki_controller.move_page', name="move_wiki_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/restore/(?P<revision_id>\d+)/$', 'app.controllers.wiki_controller.restore', name="restore_wiki_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/revision/(?P<revision_id>\d+)/$', 'app.controllers.wiki_controller.display_page', name="display_page"),
    url(r'^(?P<page_url>[\w_.,-@/]+)/$', 'app.controllers.wiki_controller.display_page', name="display_page"),
)
