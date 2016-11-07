# -*- coding:utf-8 -*-
from suds.client import Client
from suds.xsd.doctor import ImportDoctor,Import
from suds import WebFault
from django.shortcuts import render_to_response
from django.http import HttpRequest,HttpResponseRedirect
from django.template.loader import get_template
import re

def weatherclient():
	url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
	imp = Import('http://www.w3.org/2001/XMLSchema',location = 'http://www.w3.org/2001/XMLSchema.xsd')
	imp.filter.add('http://WebXml.com.cn/')
	client = Client(url, plugins =[ImportDoctor(imp)])
	return client

def WeatherQuery(request):
	client = weatherclient()
	weatherinfo=''
	if 'city' in request.GET:
		cityname=request.GET['city']
		weatherinfo = str(client.service.getWeatherbyCityName(cityname))
		#print type(weatherinfo)
		#print weatherinfo
		return render_to_response('WeatherResult.html',{'weather':weatherinfo})
	else:
		return render_to_response('WeatherResult.html')
	#return render_to_response('WeatherResult.html')

def SupportCityQuery(request,provincename):
	client = weatherclient()
	supportcity = client.service.getSupportCity(provincename)
	return supportcity

def SupportDataSetQuery(request):
	client =weatherclient()
	supportdataset = str(client.service.getSupportDataSet())
	temp = supportdataset.decode('utf-8')
	res=r'Area = "(.+)"'
	citys = re.findall(res,temp)
	return render_to_response('WeatherQuery.html',{'city':citys})

def SupportProvinceQuery(request):
	client = weatherclient()
	supportprovince = client.service.GetSupportProvince()
	return supportprovince