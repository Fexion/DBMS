from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<mem_id>[0-9]+)/$', views.mem_information, name='mem_inf'),
]
