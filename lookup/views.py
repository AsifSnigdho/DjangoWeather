from django.shortcuts import render

def home(request):
	import json
	import requests

	api_requests= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19106&distance=5&API_KEY=0416B2DD-3ABE-4698-9F78-433D7B46FA55")

	try:
		api = json.loads(api_requests.content)
	except Exception as e:
		api = "Error..."
	
	return render(request,'home.html',{'api': api})

def about(request):
	return render(request, 'about.html' ,{})	
