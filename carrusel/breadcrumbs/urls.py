
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_breadcrumbs, name='index'),
    url(r'^new_breadcrumbs/$', views.new_breadcrumbs, name='new_breadcrumbs'),
    url(r'^new_content/(?P<pk>[0-9]+)/$', views.new_content, name='new_content'),
    url(r'^generar/$', views.generar, name='generar'),
    url(r'^generar/(?P<pk>[0-9]+)/$', views.generar, name='generar'),

    url(r'^link1/$', views.link1, name='link1'),
    url(r'^link1/interno1$', views.interno1, name='interno1'),
    url(r'^link1/interno1/interno2$', views.interno2, name='interno2'),
    url(r'^link1/interno1/interno2/interno3$', views.interno3, name='interno3'),
    url(r'^link2/$', views.link2, name='link2'),
    url(r'^link3/$', views.link3, name='link3'),
]
