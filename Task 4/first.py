import requests
	def main():


	url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

	headers = {
		'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com",
		'x-rapidapi-key': "962b4f2e6emshb65a974b3b3acd2p1673e4jsn430c5613d124"
		}

	response = requests.request("GET", url, headers=headers)

	print(response.text)

main()