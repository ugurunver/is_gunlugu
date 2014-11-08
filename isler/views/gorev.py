from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Gorev
from isler.forms import GorevForm


def gorev_kaydi(request):	
	if request.method == "POST":
		form  = GorevForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "isler/gorev_formu.html", locals())
	else:
		form  = GorevForm()
		return render(request, "isler/gorev_formu.html", locals())
