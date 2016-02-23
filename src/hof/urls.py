from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.store_list, name='store_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.store_detail, name='store_detail'),
    url(r'^(?P<pk>[0-9]+)/tel/$', views.tel_detail, name='tel_detail'),

    url(r'^new/$', views.store_new, name='store_new'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.store_edit, name='store_edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.store_delete, name='store_delete'),

    url(r'^(?P<store_id>[0-9]+)/review/new/$', views.review_new, name='review_new'),
    url(r'^(?P<store_id>[0-9]+)/review/(?P<review_id>[0-9]+)/edit/$', views.review_edit, name='review_edit'),
    url(r'^(?P<store_id>[0-9]+)/review/(?P<review_id>[0-9]+)/delete/$', views.review_delete, name='review_delete'),

    url(r'^(?P<store_id>[0-9]+)/favorite_this_store/(?P<flag>[01])/(?P<from_fav_list>[\w]+)/$', views.favorite_this_store, name='favorite_this_store'),
]