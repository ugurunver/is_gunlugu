from django.forms import ModelForm

from isler.models import Not, Problem


class NotForm(ModelForm):
	class Meta:
		model = Not


class ProblemForm(ModelForm):
	class Meta:
		model = Problem
