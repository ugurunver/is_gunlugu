from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from datetime import datetime

from isler.models import Problem
from isler.forms import ProblemForm

def problem_kaydi(request):	
	if request.method == "POST":
		form  = ProblemForm(request.POST)
		if form.is_valid():
			form.save()	
			return HttpResponseRedirect(reverse("isler:bugun"))
		else:
			return render(request, "isler/problem_formu.html", locals())
	else:
		form  = ProblemForm()
		return render(request, "isler/problem_formu.html", locals())
