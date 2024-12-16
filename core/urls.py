from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', test_view),
    path('', home_view),
    path('talabalar/', talabalar_view,name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('recordlar/<int:record_id>/', record_details_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitob-qoshish/', kitob_qoshish_view),
    path('mualliflar/', mualliflar_view, name= 'mualliflar'),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('kitoblar/<int:kitob_id>/', kitob_details_view),
    path('kitoblar/<int:kitob_id>/delete/', kitob_delete_view),
    path('recordlar/<int:record_id>/delete/', record_delete_view),
    path('recordlar/', recordlar_view,name='recordlar'),
    path('record_qoshish/', record_qoshish_view , name='record_qoshish'),
]
