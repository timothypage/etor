from django.db import models

from picker.models import SpecimenSource

# Create your models here.
class Analysis(models.Model):
    name = models.CharField(max_length=255);
    accepted_sources = models.ManyToManyField(SpecimenSource)
    
    def __unicode__(self):
        return self.name
