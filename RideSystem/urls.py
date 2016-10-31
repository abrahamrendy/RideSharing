"""RideSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from RideSystem_app import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^(?i)login/', views.Login.as_view()),
    url(r'^(?i)sendpresence/', views.SendPresence.as_view()),
    url(r'^(?i)sendrequest/', views.SendRequest.as_view()),
    url(r'^(?i)receiverequest/', views.ReceiveRequest.as_view()),
    url(r'^(?i)acceptrequest/', views.AcceptRequest.as_view()),
    url(r'^(?i)receiveacceptedrequest/', views.ReceiveAcceptedRequest.as_view()),
    url(r'^(?i)senddriverlocation/', views.SendDriverLocation.as_view()),
    url(r'^(?i)receivedriverlocation/', views.ReceiveDriverLocation.as_view()),
    url(r'^(?i)starttrip/', views.StartTrip.as_view()),
    url(r'^(?i)endtrip/', views.EndTrip.as_view()),
]
