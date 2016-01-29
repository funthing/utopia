# coding:utf-8
from django.conf.urls import patterns, include, url
from upapp.views import *

urlpatterns = patterns('',
    url(r'^app/add/$', app_add, name='app_add'),
    url(r"^app/add_batch/$", app_add_batch, name='app_add_batch'),
    url(r'^app/list/$', app_list, name='app_list'),
    url(r'^app/del/$', app_del, name='app_del'),
    url(r"^app/detail/$", app_detail, name='app_detail'),
    url(r'^app/edit/$', app_edit, name='app_edit'),
    url(r'^app/edit_batch/$', app_edit_batch, name='app_edit_batch'),
    url(r'^app/update/$', app_update, name='app_update'),
    url(r'^app/update_batch/$', app_update_batch, name='app_update_batch'),
    url(r'^app/upload/$', app_upload, name='app_upload'),
    url(r'^group/del/$', group_del, name='app_group_del'),
    url(r'^group/add/$', group_add, name='app_group_add'),
    url(r'^group/list/$', group_list, name='app_group_list'),
    url(r'^group/edit/$', group_edit, name='app_group_edit'),
    url(r'^map/list/$', map_list, name='map_list'),
    url(r'^map/add/$', map_add, name='map_add'),
    url(r"^map/add_batch/$", map_add_batch, name='map_add_batch'),
    url(r'^map/detail/$', map_detail, name='map_detail'),
    url(r'^map/edit/$', map_edit, name='map_edit'),
    url(r'^map/del/$', map_del, name='map_del'),
    url(r'^map/edit_batch/$', app_edit_batch, name='map_edit_batch'),
    url(r'^map/update/$', map_update, name='map_update'),
    url(r'^map/update_batch/$', map_update_batch, name='map_update_batch'),
    url(r'^map/upload/$', map_upload, name='map_upload'),
    url(r'^web/list/$', web_list, name='web_list'),
    url(r'^dns/list/$', dns_list, name='dns_list'),
)
