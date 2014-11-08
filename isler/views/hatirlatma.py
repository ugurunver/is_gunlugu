from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Hatirlatma
from isler.forms import HatirlatmaForm

def hatirlatma_kaydi(request):	
	if request.method == "POST":
		form  = HatirlatmaForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "isler/hatirlatma_formu.html", locals())
	else:
		form  = HatirlatmaForm()
		return render(request, "isler/hatirlatma_formu.html", locals())