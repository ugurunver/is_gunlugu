from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Not, Problem, Is

from isler.forms import NotForm

def bugun(request):
	simdi = datetime.now()
	bugunun_notlari = Not.objects.filter(olusturulma__year=simdi.year, olusturulma__month=simdi.month, olusturulma__day=simdi.day)
	
	return render(request, "bugun.html", locals())



def not_kaydi(request):
	
	if request.method == "POST":
		form  = NotForm(request.POST)
		if form.is_valid():
			obj = form.save()
			obj.save()
			print obj
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "genel_form.html", locals())
	else:
		form  = NotForm()
		return render(request, "genel_form.html", locals())





