from rest_framework import serializers
from RideSystem_app.models import Passenger, Driver, System

class SystemSerializer(serializers.ModelSerializer):
	pk = serializers.IntegerField(read_only=True)
	passenger_id = serializers.IntegerField (required = False)
	driver_id = serializers.IntegerField(required = False)
	request_id = serializers.CharField (required = False)
	lat_from = serializers.CharField (required = False) # latitude from
	long_from = serializers.CharField (required = False) # longitude from
	lat_to = serializers.CharField (required = False) # latitude destination
	long_to = serializers.CharField (required = False) # longitude destination
	status = serializers.CharField (required = False) #request status A: Accepted, P: Pending
	trip_status = serializers.CharField(required = False)

	class Meta:
		model = System
		fields = ('pk','passenger_id','driver_id','request_id','lat_from','long_from','lat_to','long_to','status', 'trip_status')