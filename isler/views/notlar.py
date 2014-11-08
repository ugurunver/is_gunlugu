from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Not
from isler.forms import NotForm


def not_kaydi(request):	
	if request.method == "POST":
		form  = NotForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "isler/not_formu.html", locals())
	else:
		form  = NotForm()
		return render(request, "isler/not_formu.html", locals())