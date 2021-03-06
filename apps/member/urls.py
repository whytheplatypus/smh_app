# Copyright Videntity Systems, Inc.
from django.conf.urls import url
from .views import (
    DashboardView, approve_resource_request, get_member_data, revoke_resource_request
)

# Copyright Videntity Systems Inc.

app_name = 'member'
urlpatterns = [
    url(r'^$',
        DashboardView.as_view(), name='dashboard'),
    url(r'^approve_resource_request/(?P<pk>[0-9]+)/$',
        approve_resource_request,
        name='approve_resource_request'),
    url(r'^revoke_resource_request/(?P<pk>[0-9]+)/$',
        revoke_resource_request,
        name='revoke_resource_request'),
    url(r'^(?P<pk>[0-9]+)/get_data/(?P<resource_name>[\w]+)/(?P<record_type>[\w]+)/$',
        get_member_data,
        name='get_member_data'),
]
