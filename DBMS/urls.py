"""DBMS URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from memes.admin import user_admin_site


user_admin_site.site_header = "User settings"
user_admin_site.index_title = ""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^change/', include(user_admin_site.urls), name="change"),
    url(r'^memes/', include("memes.urls")),
    url(r'^$', include("memes.urls")),
]
