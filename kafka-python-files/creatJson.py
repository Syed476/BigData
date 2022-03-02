import json

file="01_name.json"

def write_json (data,filename="01_new_json_data.json"):
	with open (filename, 'w') as f:
		json.dump(data,f,indent: 4)

	data ={"bob","cindy"}
	write_json(data)
