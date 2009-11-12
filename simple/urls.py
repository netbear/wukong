from django.conf.urls.defaults import *

from satchmo_store.urls import urlpatterns
from simple.account.urls import invpatterns

urlpatterns += patterns('',
    (r'test/', include('simple.localsite.urls'))
)

urlpatterns += patterns('',
    (r'accounts/credits/$', 'simple.account.views.display_credit')
)

urlpatterns += invpatterns
