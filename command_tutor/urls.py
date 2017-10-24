from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^clicked$', views.on_clicked, name='onclick'),
    url(r'^slash$', views.on_slash, name='onslash'),
    url(r'^debug$', views.on_debug, name='ondebug'), # デバッグ用
]