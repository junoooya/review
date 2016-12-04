from django.conf.urls import url
from django.contrib import admin

from totalreview.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/$', news , name="news"),
]
