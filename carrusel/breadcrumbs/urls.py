from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^link1/$', views.link1, name='link1'),
    url(r'^link2/$', views.link2, name='link2'),
    url(r'^link3/$', views.link3, name='link3'),
]
