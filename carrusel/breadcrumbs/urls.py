
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_breadcrumbs, name='index'),
    url(r'^new_breadcrumbs/$', views.new_breadcrumbs, name='new_breadcrumbs'),
    url(r'^new_content/(?P<pk>[0-9]+)/$', views.new_content, name='new_content'),
    url(r'^generar/$', views.generar, name='generar'),
    url(r'^generar/(?P<pk>[0-9]+)/$', views.generar, name='generar'),
]
