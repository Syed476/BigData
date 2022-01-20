from json import dumps
from kafka import KafkaProducer
from data2 import get_data
import time
import json

def json_serializer(data):
	return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=json_serializer)



if __name__ == "__main__":
	while 1==1:
		getData=get_data()
		print (getData)	
		producer.send('topic-name',getData)
		time.sleep(15)
	
