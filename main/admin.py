from django.contrib import admin
from django.contrib.auth.models import Group,User
from .models import *

class TalabaAdmin(admin.ModelAdmin):
    list_display = ('id' , 'ism' , 'yosh' , 'tel' , 'guruh' , 'kurs' , 'kitob_soni')
    list_display_links = ('id', 'ism')
    list_filter = ('guruh', 'kurs')
    list_per_page = 50
    list_editable = ('guruh', 'kitob_soni')

    search_fields = ('guruh', 'ism')
    search_help_text = "Ism va guruh orqali qidiring!"

class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ('id','ism' , 'telefon_raqam' , 'ish_vaqti')
    list_display_links = ('id','ism')
    list_filter = ('id','ism')

    search_fields = ('id','ish_vaqti')
    search_help_text = "ish vaqti orqali qidiring!"

class RecordAdmin(admin.ModelAdmin):
    date_hierarchy = 'olingan_sana'

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1

class MuallifAdmin(admin.ModelAdmin):
    list_display = ('id','ism' , 't_yil' , 'jins' , 'millat' , 'tirik' , 'kitoblar_soni')
    inlines = (KitobInline,)
    list_filter = ('tirik',)
    list_display_links = ('id', 'ism')
    list_editable = ('kitoblar_soni','tirik')


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Talaba , TalabaAdmin)
admin.site.register(Muallif , MuallifAdmin)
admin.site.register(Kitob)
admin.site.register(Kutubxonachi , KutubxonachiAdmin)
admin.site.register(Record , RecordAdmin)
