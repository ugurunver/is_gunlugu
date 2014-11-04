from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Not, Problem, Is

from isler.forms import NotForm, ProblemForm

def bugun(request):
	bugunun_notlari = Not.objects.filter(gun=datetime.now())
	bugunun_problemleri = Problem.objects.filter(gun=datetime.now())
	return render(request, "bugun.html", locals())



def not_kaydi(request):	
	if request.method == "POST":
		form  = NotForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "genel_form.html", locals())
	else:
		form  = NotForm()
		return render(request, "genel_form.html", locals())


def problem_kaydi(request):	
	if request.method == "POST":
		form  = ProblemForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "genel_form.html", locals())
	else:
		form  = ProblemForm()
		return render(request, "genel_form.html", locals())





