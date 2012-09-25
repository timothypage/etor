from django.db import models

from samples.models import Place

# Create your models here.

class Agency(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Place)
    phone = models.CharField(max_length=64)
    fax = models.CharField(max_length=64)
    # preferred_delivery_method = models.ForeignKey(DeliveryMethod)

    def __unicode__(self):
        return self.name
