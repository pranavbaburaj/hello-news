import requests 


secret = "key"
# Define the endpoint 
url = 'https://newsapi.org/v2/everything?'

# Specify the query and 
# number of returns 
parameters = { 
	'q': 'merkel', # query phrase 
	'pageSize': 100, # maximum is 100 
	'apiKey': secret # your own API key 
} 

# Make the request 
def get_news():
	response = requests.get(url, 
						params = parameters) 
	response_json = response.json() 
	return response_json['articles']


