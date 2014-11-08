from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Not, Problem, Gorev, Hatirlatma, Is


def bugun(request):
	bugunun_notlari = Not.objects.filter(gun=datetime.now())
	bugunun_problemleri = Problem.objects.filter(gun=datetime.now())
	bugunun_gorevleri = Gorev.objects.filter(gun=datetime.now())
	bugunun_hatirlatmalari = Hatirlatma.objects.filter(gun=datetime.now())
	return render(request, "isler/bugun.html", locals())










