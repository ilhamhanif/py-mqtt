import os
import sys

# How to run 
# python3 subscriber.py 127.0.0.1 topic/subtopic '%I|%U|%t|%q|%p|%l' 2

host = str(sys.argv[1])
port = str(sys.argv[2])
topic = str(sys.argv[3])
data_format = str(sys.argv[4])
qos = str(sys.argv[5]) #Available QoS 0, 1, and 2.

result = os.system("mosquitto_sub -h "+host+" -p "+port+" -t "+topic+" -F '"+data_format+"' -q "+qos+" -d").read()
print(result)
print("----------")
