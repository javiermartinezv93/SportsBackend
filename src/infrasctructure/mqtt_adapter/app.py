from paho.mqtt.client import Client

broker = '127.0.0.1'
port = 1883
client_id = 'server'

client = Client(client_id)
client.connect(broker, port)

def on_connect(client, userdata, flags, rc):
    print('Connected with result code ' + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

client.on_connect = on_connect
client.on_message = on_message