"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from management.views import *
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^rooms/', listRooms),
    url(r'^record/(\d*)/(\d{4}-\d{2}-\d{2})/(\d{4}-\d{2}-\d{2})/$', record),
    url(r'^record/$', record),
    url(r'^records/$', listRecords),
    url(r'^bill/$', bill),
    url(r'^payment/$', add_payment),
    url(r'^login/$', login, {'template_name' : 'login.html'}),
    url(r'^logout/$', logout_view),
    url(r'^$', main),
]
