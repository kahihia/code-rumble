from django.conf.urls import patterns, url, include
from django.contrib import admin
from code_rumble.apps.main.views.user_login import (user_profile, users, login_view, signup, logout_view,
                                                    verify_account)

from code_rumble.apps.main.views import Shipper, create_get, GoodsOwner

from .views import Home

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(), name='home_url'),
    url(r'^login$', login_view),
    url(r'^logout$', logout_view),
    url(r'^signup$', signup),
    url(r'^users/$', users),
    url(r'^verify/(?P<username>\w{0,30})$', verify_account),
    url(r'^users/(?P<username>\w{0,30})/$', users),
    url(r'^user_profile/(?P<username>\w{0,30})/$', user_profile, name='user_profile'),
    url(r'^user_profile/$', user_profile),
    url(r'shipper$', Shipper.as_view(), name='shipper_url'),
    url(r'^goods_owner/(?P<task_id>[1-9]{1})$', GoodsOwner.as_view(), name='goods_owner_url'),
    url(r'job', create_get, name='job_url'),
)

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^static/(?P<path>.*)$', 'serve'),
)
