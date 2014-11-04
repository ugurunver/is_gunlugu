from django.forms import ModelForm

from isler.models import Not, Problem


class NotForm(ModelForm):
	
	class Meta:
		model = Not
