from django.db import models


GENDER_CHOICES = (
    (u'M', u'Male'),
    (u'F', u'Female'),
    (u'U', u'Unknown'),
)

SUFFIX_CHOICES = (
    (u'JR.',u'JR.'),
    (u'SR.',u'SR.'),
    (u'I', u'I'),
    (u'II', u'II'),
    (u'III', u'III'),
    (u'IV', u'IV'),
)

REL_CHOICES = (
    (u'FATHER', u'Father'),
)



class Place(models.Model):
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.city + ' ' + self.state + ' ' + self.zip


class Ethnicity(models.Model):
    ethnicity = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.ethnicity


class Race(models.Model):
    race = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.race


class Specimen_Source(models.Model):
    source = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.source


class Insurance(models.Model):
    last_name = models.CharField(max_length=255, help_text="Subscriber Last Name", blank=True)
    first_name = models.CharField(max_length=255, help_text="Subscriber First Name", blank=True)
    middle_initial = models.CharField(max_length=3, help_text="Subscriber MI", blank=True)
    relationship = models.CharField(max_length=32, choices=REL_CHOICES, blank=True)
    group_number = models.CharField(max_length=255, help_text="Insurance Group Number", blank=True)
    contract_number = models.CharField(max_length=255, help_text="Insurance Contract Number", blank=True)
    
    def __unicode__(self):
        return self.last_name + ' ' + self.first_name


class Test_Reason(models.Model):
    reason = models.CharField(max_length=1024)
    
    def __unicode__(self):
        return self.reason


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True)
    middle_initial = models.CharField(max_length=3, blank=True)
    suffix = models.CharField(max_length=3, choices=SUFFIX_CHOICES, blank=True)
    birth_date = models.DateField(blank=True)
    gender = models.CharField(max_length=16, choices=GENDER_CHOICES, blank=True)
    address = models.ForeignKey(Place, null=True)
    race = models.ForeignKey(Race, null=True) #TODO: continue making optional.
    ethnicity = models.ForeignKey(Ethnicity, null=True)
    patient_id = models.CharField(max_length=255, help_text="Submitter's Patient ID Number", blank=True)
    insurance = models.ForeignKey(Insurance, null=True)
    
    def __unicode__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.birth_date)
    

class Specimen(models.Model):
    patient = models.ForeignKey(Patient)
    collection_time = models.DateTimeField()
    specimen_id = models.CharField(max_length=255, blank=True)
    source = models.ForeignKey(Specimen_Source, null=True)
    test_reason = models.ManyToManyField(Test_Reason, verbose_name="reason for testing", null=True)
    
    def __unicode__(self):
        return self.patient.first_name + ' ' + self.patient.last_name + ' ' + str(self.source)


