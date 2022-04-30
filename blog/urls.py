from django.urls import path

from .views import post_list, post_detail, post_new, post_edit

urlpatterns = [
    path('', post_list, name='post_list'),
    path(r'^post/(?P<pk>[0-9]+)/$', post_detail, name="post_detail"),
    path(r'^post/new/$', post_new, name='post_new'),
    path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
]
