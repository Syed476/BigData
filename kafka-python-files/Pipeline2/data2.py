import json
import requests
def get_data():



	import requests

	url = "https://countries-cities.p.rapidapi.com/location/city/nearby"

	querystring = {"latitude":"55.11","longitude":"37.02","radius":"25","min_population":"99","max_population":"10000"}

	headers = {
    	'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers, params=querystring)


	result= response.json()
	return json.dumps(result,indent=2)

if  __name__ == "__main__":
   
	print(get_data())


