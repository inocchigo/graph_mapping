from __future__ import unicode_literals

from django.db import models

class TargetPlace(models.Model):
#    id = models.PositiveIntegerField('id',blank=False, primary_key=True,unique=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(u'name', max_length=255)
    description = models.CharField(u'descrption', max_length=1024) 
    time = models.CharField('time', max_length=50)
    region = models.CharField(u'region', max_length=50)
    url = models.CharField(u'url', max_length=1024)
    pointX = models.FloatField('point_x')
    pointY = models.FloatField('point_y')

    def __unicode__(self):
        return self.name

class TargetImage(models.Model):
#    id = models.PositiveIntegerField('id',blank=False, primary_key=True,unique=True)
    id = models.AutoField(primary_key=True)
    image_data = models.BinaryField()
    name = models.CharField(u'name', max_length=255)
    targetplace = models.ForeignKey(TargetPlace)
    def __unicode__(self):
        return self.name