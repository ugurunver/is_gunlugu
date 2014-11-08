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
	cozumu = models.TextField(blank=True, null=True)
	tip = "problem"


class Gorev(Is):
	baslik = models.CharField(max_length=500)
	yapildi = models.BooleanField(default=False)
	notlar = models.TextField(blank=True, null=True)
	tip = "gorev"


class Hatirlatma(Is):
	tarih = models.DateTimeField(blank=True, null=True)
	aktif = models.BooleanField(default=True)
	tip = "hatirlatma"
