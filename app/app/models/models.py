from django.db import models

class Location(models.Model):
    id = models.AutoField(primary_key=True)
    officename = models.CharField(max_length=25)
    pincode = models.IntegerField()
    officeType = models.CharField(max_length=25)
    Deliverystatus = models.CharField(max_length=25)
    divisionname = models.CharField(max_length=25)
    regionname = models.CharField(max_length=25)
    circlename = models.CharField(max_length=25)
    Taluk = models.CharField(max_length=25)
    Districtname = models.CharField(max_length=25)
    statename = models.CharField(max_length=25)
    class Meta:
        db_table = u'location'
