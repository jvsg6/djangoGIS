from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class Accident(models.Model):
	name = models.CharField(max_length=20)
	location = models.PointField(srid=4326)
	objects = models.Manager()

	def __unicode__(self):
		return self.name