from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_carousel/$', views.new_carousel, name='new_carousel'),
    url(r'^new_content/(?P<pk>[0-9]+)/$', views.new_content, name='new_content'),
    url(r'^generar/$', views.generar, name='generar'),
    url(r'^generar/(?P<pk>[0-9]+)/$', views.generar, name='generar'),
]
