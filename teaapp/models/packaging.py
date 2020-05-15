from django.db import models
from django.urls import reverse


class Packaging(models.Model):

    name = models.CharField(max_length=100)
    handmade = models.BooleanField()
    production_location = models.CharField(max_length=100)
    teas = models.ManyToManyField("Tea", through='TeaPackaging')

    class Meta:
        verbose_name = ("Packaging")
        verbose_name_plural = ("Packagings")

    def __str__(self):
        return f"{self.name} ({self.flavor})"

    def get_absolute_url(self):
        return reverse("Packaging_detail", kwargs={"pk": self.pk})
