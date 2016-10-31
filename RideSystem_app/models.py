from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Passenger(models.Model):
	username = models.CharField (max_length = 50, blank = True, null = True) # passenger username
	password = models.CharField (max_length = 50, blank = True, null = True) # passenger password
	name = models.CharField (max_length = 50, blank = True, null = True) # passenger name
	lat = models.CharField (max_length = 20, blank = True, null = True) # passenger location
	long = models.CharField (max_length = 20, blank = True, null = True) # passenger location

class Driver(models.Model):
	username = models.CharField (max_length = 50, blank = True, null = True) # driver username
	password = models.CharField (max_length = 50, blank = True, null = True) # driver password
	name = models.CharField (max_length = 50, blank = True, null = True) # driver name
	lat = models.CharField (max_length = 20, blank = True, null = True) # driver location
	long = models.CharField (max_length = 20, blank = True, null = True) # driver location
	status = models.CharField (max_length = 1, blank = True, null = True) # driver status A: Active, I: Inactive

class System(models.Model):
	passenger_id = models.IntegerField (blank = True, null = True)
	driver_id = models.IntegerField(blank = True, null = True)
	request_id = models.CharField (max_length = 20, blank = True, null = True)
	lat_from = models.CharField (max_length = 20, blank = True, null = True) # latitude from
	long_from = models.CharField (max_length = 20, blank = True, null = True) # longitude from
	lat_to = models.CharField (max_length = 20, blank = True, null = True) # latitude destination
	long_to = models.CharField (max_length = 20, blank = True, null = True) # longitude destination
	status = models.CharField (max_length = 1, blank = True, null = True) #request status A: Accepted, P: Pending, C: Completed
	trip_status = models.CharField (max_length = 1, blank = True, null = True) # trip status O: Ongoing, C: Completed
