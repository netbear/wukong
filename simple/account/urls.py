from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'$', 'simple.account.views.display_credit'),
)

invpatterns = patterns('simple.account.views',
    (r'^invite/$', 'invite_friends'),
    (r'^invite/(?P<invitation_code>\w+)/$', 'register'),
)

#login_replacement = url(r'^invite
