
import requests
def get_data():


	import requests

	url = "https://countries-cities.p.rapidapi.com/location/country/GB/city/list"

	querystring = {"page":"2","per_page":"4","population":"3000"}

	headers = {
    	'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers, params=querystring)


	result= response.json()
	return result

if  __name__ == "__main__":
   
	get_data()


