from django.forms import ModelForm
from django.forms import DateField

from isler.models import Not, Problem, Gorev, Hatirlatma


class NotForm(ModelForm):
	class Meta:
		model = Not


class ProblemForm(ModelForm):
	class Meta:
		model = Problem


class GorevForm(ModelForm):
	class Meta:
		model = Gorev

class HatirlatmaForm(ModelForm):
	#tarih = 
	class Meta:
		model = Hatirlatma
