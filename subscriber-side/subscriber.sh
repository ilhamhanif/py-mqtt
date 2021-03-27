#!/bin/sh
mosquitto_sub -h $1 -p $2 -t $3 -F $4 -q $5 -d

/usr/bin/python3 ./run-test.py 

echo 'Finished.'