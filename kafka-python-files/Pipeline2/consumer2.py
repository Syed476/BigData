import subprocess
from json import  loads
from kafka import KafkaConsumer
import pydoop.hdfs as hdfs
import json

hdfs.mkdir('hdfs://localhost:9000/myData')
file='/home/maqsood/dataUpdate.json'
args_list=['hdfs','dfs','put',file,'/myData']
print('Running system command {}'.format(' '.join(args_list)))
print ('This is data from a new stream')
hdfs_path='hdfs://localhost:9000/myData/dataUpdate.json'
consumer = KafkaConsumer('topic-name',bootstrap_servers=['localhost:9092'])
print ("Staring the consumer")

for message in consumer:
	print("myData = {} ".format(json.loads(message.value)))
		
	with hdfs.open(hdfs_path, 'at') as f:
		f.write(f"{json.loads(message.value)}\n")

main()
