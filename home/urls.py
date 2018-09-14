from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='zzz'),
    url(r'^1/', views.index, name='zzz')
]
