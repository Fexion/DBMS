from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^search/$', views.search, name = "search"),
    url(r'^search_creator/$', views.search_creator, name = "search_creator"),
    url(r'^creators/$', views.creators, name = "creators"),
    url(r'^creators/(?P<Creator_id>[0-9]+)/$', views.creator_inf, name='creator_inf'),
    url(r'^(?P<mem_id>[0-9]+)/$', views.mem_information, name='mem_inf'),
]
