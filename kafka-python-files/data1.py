
import requests
def get_data():



	import requests

	url = "https://cricket-live-data.p.rapidapi.com/fixtures-by-date/2020-09-21"

	headers = {
    	'x-rapidapi-host': "cricket-live-data.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers)

	result= response.json()
	return result

if  __name__ == "__main__":
   
	get_data()


