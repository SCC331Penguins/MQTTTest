import paho.mqtt.client as mqtt
import json;

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client1, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("SCC33102_R01")

# The callback for when a PUBLISH message is received from the server.
def on_message(client1, userdata, msg):
    print(msg.topic+" "+str(msg.payload)+" "+str())

def pub(topic, data):
    client.publish(topic,data)

client = mqtt.Client("")

data = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IlNDQzMzMTAyX1IwMSJ9.DjgR09-WqfVFcCs2IOSYAVZMoF0wbbkyQZlppIoY95I",
    "type":"DATA",
    "payload":{
    "sensors": []}
}

sensor = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IlNDQzMzMTAyX1IwMSJ9.DjgR09-WqfVFcCs2IOSYAVZMoF0wbbkyQZlppIoY95I",
    "type": "ACTSEN",
    "payload":["3123123123", "12359213123", "12941230213123"]
}

notif = {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IlNDQzMzMTAyX1IwMSJ9.DjgR09-WqfVFcCs2IOSYAVZMoF0wbbkyQZlppIoY95I",
    "type": "COM",
    "payload":{"MAC":"NOTIFICATIONS", "command":"sendNotification", "message":"Hi this is a notification"}
}
test = json.dumps(data, ensure_ascii=False)
print(str(test))

print(client._client_id)
client.on_connect = on_connect
client.on_message = on_message
client.subscribe("SCC33102_R01");

client.connect("sccug-330-02.lancs.ac.uk", 1883, 60)
pub("SCC33102_R01", json.dumps(notif))
client.loop_forever()