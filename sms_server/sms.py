from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages
from flask import Flask, render_template,abort,request
from pymongo import MongoClient
import requests
import json
from datetime import datetime
import os 
app = Flask(__name__)

ip = IPv4Address("192.168.43.64")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)

#authorization
was_accepted = session.request_authorization()
#sendign messages
service = MessagingService(session)

@app.route("/send_weather_update",methods=["POST"])
def weather_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "WEATHER UPDATE BROADCAST MESSAGE: MAX TEMP:32C, MIN TEMP:28C,LOW CHANCES OF RAIN."
    for i in numbers:
        service.send_message(i,message)

@app.route("/send_crop_prices_update",methods=["POST"])
def crops_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "CROP PRICES UPDATE BROADCAST MESSAGE:Commodity	MSP for 2018-19 (Rs per quintal): Bajra-1950 ;  Maize-1700;  Ragi-2897; Arhar(Tur)-5675;"
    for i in numbers:
        service.send_message(i,message)


@app.route("/send_water_update",methods=["POST"])
def water_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "WATER SUPPLY @ 3PM - 5PM"
    for i in numbers:
        service.send_message(i,message)


@app.route("/send_electricity_update",methods=["POST"])
def electricity_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "ELECTRICITY CUTS @ 2AM - 5AM"
    for i in numbers:
        service.send_message(i,message)

@app.route("/update_phone_book",methods=["GET"])
def get_all_messages():
    messages = service.fetch_message_history()
    for i in messages:
        user_number = messages[i].phone
        user_message = usermessages[i].content
        if(user_message in ["v001","v002"]):
            filee = open(user_message+".txt","w+")
            filee.write("," + user_number)
        else:
            filee = open(user_complaints+".txt","w+")
            filee.write((user_number,user_message))



if __name__ == "__main__" :
    app.run(debug=True,port=5004,host="0.0.0.0")