from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from RideSystem_app.models import Passenger, Driver, System
from RideSystem_app.serializers import SystemSerializer
from math import sin, cos, sqrt, atan2, radians


#
# type = 1 is for Passenger
# type = 0 is for Driver
#
############# CONNECTION #############
class Login(APIView):
	def post(self,request,format=None):
		if (request.data['type'] == '1'):
			try:			
				user = Passenger.objects.get(username__iexact=request.data['username'])
			except Passenger.DoesNotExist:
				user = None
			if (user is not None):
				if (user.password == request.data['password']):
					return Response({'info': 'Success'})
				else:
					return Response({'info': 'Failed', 'message' : 'Failed to connect'})
			else:
				return Response({'info' : 'Failed','message': 'Failed to Connect, Incorrect Passenger Username'})
		else:
			try:
				driver = Driver.objects.get(username__iexact=request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				if (driver.password == request.data['password']):
					return Response({'info': 'Success'})
				else:
					return Response({'info': 'Failed', 'message' : 'Failed to connect'})
			else:
				return Response({'info' : 'Failed','message': 'Failed to Connect, Incorrect Driver Username'})

class SendPresence(APIView):
	def post(self, request, format=None):
		if (request.data['type'] == '1'):
			try:			
				user = Passenger.objects.get(username__iexact=request.data['username'])
			except Passenger.DoesNotExist:
				user = None
			if (user is not None):
				user.lat = request.data['lat']
				user.long = request.data['long']
				user.save()
				return Response({'info' : 'Success', 'longitude' : request.data['long'], 'latitude' : request.data['lat']})
			else:
				return Response({'info' : 'Failed' , 'message' : 'Send presence failed'})
		else:
			try:			
				driver = Driver.objects.get(username__iexact=request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				driver.lat = request.data['lat']
				driver.long = request.data['long']
				driver.save()
				return Response({'info' : 'Success', 'longitude' : request.data['long'], 'latitude' : request.data['lat']})
			else:
				return Response({'info' : 'Failed' , 'message' : 'Send presence failed'})

############# PAIRING #############
class SendRequest(APIView):
	def post(self, request, format=None):
		if (request.data['type'] == '1'):
			try:
				user = Passenger.objects.get(username__iexact = request.data['username'])
			except Passenger.DoesNotExist:
				user = None
			if (user is not None):
				passenger_id = user.id
				lat_from = user.lat
				long_from = user.long
				lat_to = request.data['lat']
				long_to = request.data['long']
				#check request with the same user
				if (System.objects.filter(passenger_id = user.id, status = 'P').exists()):
					return Response ({'info' : 'Failed', 'message' : 'Request already made'})
				else:
					ct = passenger_id
					request_id = 'R' + str(passenger_id)
					while (System.objects.filter(request_id = request_id).exists()):
						request_id = 'R' + str(ct+1)
						ct = ct + 1
					if (lat_to != '' and long_to != ''):
						System.objects.create(passenger_id = passenger_id, request_id = request_id, lat_from = lat_from, long_from = long_from, lat_to = lat_to, long_to = long_to, status = 'P')
						return Response({'info' : 'Success', 'request_id': request_id ,'passenger_id' : passenger_id,'from' : lat_from + ', '+ long_from, 'to' : lat_to + ', '+ long_to})
					else:
						return Response({'info' : 'Failed', 'message' : 'There is empty required parameter'})
			else:
				return Response({'info' : 'Failed', 'message' : "User doesn't exist"})
		else:
			return Response({'info' : 'Failed', 'message' : "You can't make a request"})

class ReceiveRequest(APIView):
	def post(self, request, format=None):
		if (request.data['type'] == '0'):
			try:
				driver = Driver.objects.get(username__iexact = request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				driver_id = driver.id
				if (System.objects.filter(status = 'P').exists()):
					requests = System.objects.filter(status = 'P')
					serializer = SystemSerializer(requests, many = True)
					return Response({'message' : serializer.data})
				else:
					return Response ({'message' : ''})
			else:
				return Response ({'info' : 'Failed', 'message' : 'Driver not exist'})

class AcceptRequest (APIView):
	def post(self, request, format = None):
		if (request.data['type'] == '0'):
			try:
				driver = Driver.objects.get(username__iexact = request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				driver_id = driver.id
				accepted_request = System.objects.get(request_id = request.data['request_id'])
				accepted_request.driver_id = driver_id
				accepted_request.status = 'A'
				accepted_request.save()
				return Response({'info' : 'Success', 'message' : 'Request ' + accepted_request.request_id + ' accepted'})
			else:
				return Response ({'info' : 'Failed', 'message' : 'Driver not exist'})

class ReceiveAcceptedRequest(APIView):
	def post (self, request, format = None):
		if (request.data['type'] == '1'):
			try:
				user = Passenger.objects.get(username__iexact = request.data['username'])
			except User.DoesNotExist:
				user = None
			if (user is not None):
				accepted_request = System.objects.get(request_id = request.data['request_id'])
				driver = Driver.objects.get(id = accepted_request.driver_id)
				if accepted_request.driver_id != '':
					return Response ({'info' : 'Success', 'message' : driver.name + " has accepted your request.", 'details' : {'username' : driver.username, 'name' : driver.name}})
				else:
					return Response ({'info' : 'Success', 'message' : "No driver accepted your request yet"})
			else:
				return Response ({'info' : 'Failed', 'message' : 'User not exist'})

############# APPROACHING #############
class SendDriverLocation(APIView):
	def post(self, request, format = None):
		if (request.data['type'] == '0'):
			try:			
				driver = Driver.objects.get(username__iexact=request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				driver.lat = request.data['lat']
				driver.long = request.data['long']
				driver.save()
				return Response({'info' : 'Success', 'longitude' : request.data['long'], 'latitude' : request.data['lat']})
			else:
				return Response({'info' : 'Failed', 'message' : 'Sending location failed'})
		else:
			return Response({'info' : 'Failed', 'message' : 'Sending location failed'})

class ReceiveDriverLocation(APIView):
	def post (self, request, format = None):
		if (request.data['type'] == '1'):
			try:
				user = Passenger.objects.get(username__iexact = request.data['username'])
			except User.DoesNotExist:
				user = None
			if (user is not None):
				accepted_request = System.objects.get(request_id = request.data['request_id'])
				driver = Driver.objects.get(id = accepted_request.driver_id)
				if accepted_request.driver_id != '':
					return Response ({'info' : 'Success', 'latitude' : driver.lat, 'longitude' : driver.long})
				else:
					return Response ({'info' : 'Success', 'message' : "No driver accepted your request yet"})
			else:
				return Response ({'info' : 'Failed', 'message' : 'User not exist'})
		else:
			return Response({'info' : 'Failed'})

############# DRIVING #############
class StartTrip(APIView):
	def post(self, request, format = None):
		if (request.data['type'] == '0'):
			try:			
				driver = Driver.objects.get(username__iexact=request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				request = System.objects.get(request_id = request.data['request_id'])
				request.trip_status = 'O'
				request.save()
				return Response({'info' : 'Success', 'message': 'Trip started'})
			else:
				return Response({'info' : 'Failed', 'message' : "Driver doesn't exist"})
		else:
			return Response({'info' : 'Failed'})

class EndTrip(APIView):
	def post(self, request, format = None):
		if (request.data['type'] == '0'):
			try:			
				driver = Driver.objects.get(username__iexact=request.data['username'])
			except Driver.DoesNotExist:
				driver = None
			if (driver is not None):
				request = System.objects.get(request_id = request.data['request_id'])
				request.trip_status = 'C'
				request.status = 'C'
				request.save()
				R = 6373.0

				lat1 = radians(float(request.lat_from))
				lon1 = radians(float(request.long_from))
				lat2 = radians(float(request.lat_to))
				lon2 = radians(float(request.long_to))

				dlon = lon2 - lon1
				dlat = lat2 - lat1

				a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
				c = 2 * atan2(sqrt(a), sqrt(1 - a))

				distance = R * c
				distance = round(distance,3)

				return Response({'info' : 'Success', 'message': 'Trip ended', 'distance' : str(distance) + ' km'})
			else:
				return Response({'info' : 'Failed', 'message' : "Driver doesn't exist"})
		else:
			return Response({'info' : 'Failed'})
