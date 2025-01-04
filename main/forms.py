from django import forms

from main.models import Muallif, Kitob, Record


class TalabaPostForm(forms.Form):
    ism = forms.CharField()
    yosh = forms.IntegerField(min_value=15 , max_value=60)
    tel = forms.CharField()
    guruh = forms.CharField()
    kurs = forms.IntegerField(min_value=1,max_value=4)
    kitob_soni = forms.IntegerField()

class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'