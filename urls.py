# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    (r'^admin/', include(admin.site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
