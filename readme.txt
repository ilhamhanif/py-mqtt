Playground, do not expect much from this repo.

Communication to get file data on another device in a local connection through local broker using mosquitto.

Prerequisite :
1. Install Mosquitto Broker
$ sudo apt-get update
$ sudo apt-get install mosquitto

2. Install Mosquitto Clients
$ sudo apt-get install mosquitto-clients

!. Use sames topic between publisher and subscriber.
Default : topic/subtopic

!. How to run
!.. Publisher
python3 publish.py <mqtt broker host> <port> <topic> <message> <qos level>
ex:
python3 publish.py 127.0.0.1 1883 topic 'hello world' 2
sh publish.sh 127.0.0.1 1883 topic 'hello world' 2
!.. Subscribers
python3 subscriber.py <mqtt broker host> <port> <topic> <format> <qos level>
ex:
python3 subscriber.py 127.0.0.1 1883 topic '%I|%U|%t|%q|%p|%l' 2

Credits :
https://www.vultr.com/docs/how-to-install-mosquitto-mqtt-broker-server-on-ubuntu-16-04
https://mosquitto.org/man/mosquitto_sub-1.html
http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/
http://www.steves-internet-guide.com/understanding-mqtt-qos-levels-part-1/
http://www.steves-internet-guide.com/understanding-mqtt-qos-2/
