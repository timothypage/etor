from django.db import models


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.ethnicity


class Race(models.Model):
    race = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.race


class SpecimenSource(models.Model):
    source = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.source


class TestReason(models.Model):
    reason = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.reason

