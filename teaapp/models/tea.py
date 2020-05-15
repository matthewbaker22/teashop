from django.db import models
from django.urls import reverse


class Tea(models.Model):

    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=100)
    packagings = models.ManyToManyField("Packaging", through='TeaPackaging')

    class Meta:
        verbose_name = ("Tea")
        verbose_name_plural = ("Teas")

    def __str__(self):
        return f"{self.name} ({self.flavor})"

    def get_absolute_url(self):
        return reverse("Tea_detail", kwargs={"pk": self.pk})
