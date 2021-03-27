import os
import sys

# How to run 
# python3 publish.py 127.0.0.1 topic/subtopic "ini pesannya" 2

host = str(sys.argv[1])
port = str(sys.argv[2])
topic = str(sys.argv[3])
message = str(sys.argv[4])
qos = str(sys.argv[5]) #Available QoS 0, 1, and 2.

command = "mosquitto_pub -h "+host+" -p "+port+" -t "+topic+" -m '"+message+"' -q "+str(qos)+" -d"

os.system(command)
print("----------")