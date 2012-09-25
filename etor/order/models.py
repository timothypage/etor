from django.db import models

from samples.models import Specimen
from picker.models import SpecimenSource
from analysis.models import Analysis
from agency.models import Agency

# Create your models here.



class Order(models.Model):
    specimen = models.ForeignKey(Specimen)
    analysis = models.ForeignKey(Analysis)
    order_time = models.DateTimeField(auto_now_add=True)
    submitted = models.BooleanField(default=False)
    submitted_time = models.DateTimeField()

    def __unicode__(self):
        return self.specimen + str(self.order_time)

class Package(models.Model):
    submitted = models.BooleanField(default=False)
    submitted_time = models.DateTimeField(auto_now_add=True)
    orders = models.ManyToManyField(Order)
    tracking_number = models.CharField(max_length=255)
    submitting_agency = models.ForeignKey(Agency)

    def __unicode__(self):
        return str(self.id) + str(self.submitting_agency) + str(submitted_time)

