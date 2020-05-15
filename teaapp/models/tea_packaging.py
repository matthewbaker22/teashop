from django.db import models


class TeaPackaging(models.Model):

    tea = models.ForeignKey("Tea", on_delete=models.CASCADE)
    packaging = models.ForeignKey("Packaging", on_delete=models.CASCADE)
    longevity_in_months = models.IntegerField()
