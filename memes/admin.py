from django.contrib import admin
from .models import *
from django.contrib.admin.sites import AdminSite



user_admin_site = AdminSite(name='usersadmin')

user_admin_site.register(User)
user_admin_site.register(Mem)
user_admin_site.register(Creator)
user_admin_site.register(Sphere)
user_admin_site.register(Source)
user_admin_site.register(Tag)


admin.site.register(User)
admin.site.register(Mem)
admin.site.register(Creator)
admin.site.register(Sphere)
admin.site.register(Source)
admin.site.register(Tag)
