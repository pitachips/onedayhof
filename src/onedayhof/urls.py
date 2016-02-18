"""onedayhof URL Configuration

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

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from django.contrib import admin

from hof import views as hof_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', hof_views.index, name='index'),
    url(r'^store/$', hof_views.store_list, name='store_list'),
    url(r'^store/(?P<pk>[0-9]+)/$', hof_views.store_detail, name='store_detail'),
    url(r'^store/new/$', hof_views.store_new, name='store_new' ),
    # url(r'^(?P<pk>[0-9]+)/edit/$', hof_views.store_edit, name='store_edit'),
    # url(r'^(?P<pk>[0-9]+)/delete/$', hof_views.store_delete, name='store_delete'),
    # url(r'^(?P<id>[0-9]+)/review/new/$', hof_views.review_new, name='review_new'),
    # url(r'^(?P<store_pk>[0-9]+)/review/(?P<pk>[0-9]+)/edit/$', hof_views.review_edit, name='review_edit'),
    # url(r'^(?P<id>[0-9]+)/review/(?P<pk>[0-9]+)/delete/$', hof_views.review_delete, name='review_delete'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)