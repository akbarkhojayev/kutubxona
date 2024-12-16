from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

def test_view(request):
    return HttpResponse("Salom Dunyo")

def home_view(request):
    return render(request, "home.html")

def talabalar_view(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get("ism"),
            kurs=request.POST.get("kurs"),
            guruh=request.POST.get("guruh"),
            tel=request.POST.get("tel"),
            yosh=request.POST.get("yosh"),
            kitob_soni=request.POST.get("kitob_soni"),
        )
        return redirect("talabalar")
    talabalar = Talaba.objects.all()

    q_soz = request.GET.get("q_soz")

    if q_soz is not None:
        talabalar = Talaba.objects.filter(ism__icontains=q_soz)

    context = {"talabalar": talabalar, 'q_soz': q_soz}
    return render(request, "talabalar.html", context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    qsoz = request.GET.get("qsoz")

    if qsoz is not None:
        kitoblar = Kitob.objects.filter(nom__icontains=qsoz)

    context = {"kitoblar": kitoblar, 'qsoz': qsoz}
    return render(request, "kitoblar.html", context)

def kitob_qoshish_view(request):
    if request.method == "POST":
        kitob = Kitob.objects.create(
            nom=request.POST.get("nom"),
            janr=request.POST.get("janr"),
            sahifa=request.POST.get("sahifa"),
            muqova=request.POST.get("muqova"),
        )
        muallif = get_object_or_404(Muallif,id=request.POST.get("muallif_id"))
        kitob.muallif.add(muallif)
        kitob.save()
        return redirect("kitoblar")
    context = {
        'mualliflar': Muallif.objects.all(),
    }
    return render(request, "kitob_qoshish.html", context)

def mualliflar_view(request):
    if request.method == "POST":
        if request.POST.get('tirik') == 'on':
            tirik = True
        else:
            tirik = False
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            millat=request.POST.get("millat"),
            kitoblar_soni=request.POST.get("kitoblar_soni"),
            tirik=tirik,
            jins=request.POST.get("jins"),
            t_yil=request.POST.get("t_yil")
        )
        return redirect("mualliflar")
    muallif = Muallif.objects.all()

    qsoz1 = request.GET.get("qsoz1")
    if qsoz1 is not None:
        muallif = Muallif.objects.filter(ism__icontains=qsoz1)

    context = {"mualliflar": muallif, 'qsoz1': qsoz1}
    return render(request, "mualliflar.html", context)

def muallif_details_view(request , muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {"muallif": muallif}
    return render(request, "muallif_details.html", context)

def recordlar_view(request):

    record = Record.objects.all()
    context = {"recordlar": record}
    return render(request, "recordlar.html", context)

def record_details_view(request , record_id):
    record = Record.objects.get(id=record_id)
    context = {"record": record}
    return render(request, "record_details.html", context)

def kitob_details_view(request , kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {"kitob": kitob}
    return render(request, "kitob_details.html", context)

def talaba_details_view(request , talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {"talaba": talaba}
    return render(request, "talabalar_details_view.html", context)

def talaba_delete_view(request , talaba_id):
    talaba = get_object_or_404(Talaba, id=talaba_id)
    talaba.delete()
    return redirect('talabalar')

def kitob_delete_view(request , kitob_id):
    kitob = get_object_or_404(Kitob, id=kitob_id)
    kitob.delete()
    return redirect('kitoblar')

def record_delete_view(request , record_id):
    record = get_object_or_404(Record,id=record_id)
    record.delete()
    return redirect('recordlar')

def record_qoshish_view(request):
    if request.method == "POST":
        Record.objects.create(
        olingan_sana=request.POST.get("olingan_sana"),
        qaytarilgan_sana=request.POST.get("qaytarilgan_sana"),
        qaytardi = request.POST.get("qaytardi"),
        kitob = get_object_or_404(Kitob, id=request.POST.get("kitob_id")),
        muallif = get_object_or_404(Muallif,id=request.POST.get("talaba_id")),
        )
        return redirect("recordlar")
        record.save()
    context = {
        "kitoblar": Kitob.objects.all(),
        "talabalar": Talaba.objects.all(),
    }
    return render(request, "record_qoshish.html",context)



