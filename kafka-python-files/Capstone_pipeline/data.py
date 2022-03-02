import json
import requests
def get_data():

	

	url = "https://cricket-live-data.p.rapidapi.com/fixtures"

	headers = {
    	'x-rapidapi-host': "cricket-live-data.p.rapidapi.com",
    	'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
    	}

	response = requests.request("GET", url, headers=headers)


	result=response.json()["results"]
	return json.dumps(result,indent=2)

if  __name__ == "__main__":
   
	print(get_data())

