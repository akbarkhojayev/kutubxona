from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Talaba)
admin.site.register(Muallif)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi)
admin.site.register(Record)
