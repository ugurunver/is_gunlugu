from django.db import models


class Is(models.Model):
	aciklama = models.TextField()
	gun = models.DateField(auto_now_add=True)
	olusturulma = models.DateTimeField(auto_now_add=True)
	guncellenme = models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True


class Not(Is):
	tip = "not"


class Problem(Is):
	baslik = models.CharField(max_length=500)
	cozuldu = models.BooleanField(default=False)
	tip = "problem"

