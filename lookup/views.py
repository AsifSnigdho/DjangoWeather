from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_requests = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=0416B2DD-3ABE-4698-9F78-433D7B46FA55")
		
		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
	  		category_description="Air Quality is satisfactory vey nice"
	  		category_color="veryunhealthy"


		elif api[0]['Category']['Name'] == "Moderate":
	  		category_description= "Air quality is accepatable and fine"
	  		category_color="moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	  		category_description= "People with lung deasese are in danger"
	  		category_color="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	  		category_description="May occour health effect"
	  		category_color="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
	  		category_description="Serious health effect"
	  		category_color="veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
	  		category_description="You are dead"
	  		category_color="hazardous"

	  		
		
		return render(request,'home.html',{
			'api': api,
			'category_description': category_description,
			'category_color': category_color
			})


	else:	

		api_requests= requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=19106&distance=5&API_KEY=0416B2DD-3ABE-4698-9F78-433D7B46FA55")

		try:
			api = json.loads(api_requests.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
	  		category_description="Air Quality is satisfactory vey nice"
	  		category_color="good"


		elif api[0]['Category']['Name'] == "Moderate":
	  		category_description= "Air quality is accepatable and fine"
	  		category_color="moderate"

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	  		category_description= "People with lung deasese are in danger"
	  		category_color="usg"
		elif api[0]['Category']['Name'] == "Unhealthy":
	  		category_description="May occour health effect"
	  		category_color="unhealthy"
		elif api[0]['Category']['Name'] == "Very Unhealthy":
	  		category_description="Serious health effect"
	  		category_color="veryunhealthy"
		elif api[0]['Category']['Name'] == "Hazardous":
	  		category_description="You are dead"
	  		category_color="hazardous"

	  		
		
		return render(request,'home.html',{
			'api': api,
			'category_description': category_description,
			'category_color': category_color
			})

def about(request):
	return render(request, 'about.html' ,{})	
