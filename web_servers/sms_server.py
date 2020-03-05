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

ip = IPv4Address("192.168.1.8")  # let's create an IP address object
# now create a session
session = AirmoreSession(ip)

#authorization
was_accepted = session.request_authorization()
#sendign messages
service = MessagingService(session)
@app.route("/",methods=["GET"])
def main():
    return render_template("broadcast_webapp/broadcast.html")

@app.route("/send_weather",methods=["POST"])
def weather_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "WEATHER UPDATE BROADCAST MESSAGE: MAX TEMP:32C, MIN TEMP:28C,LOW CHANCES OF RAIN."
    for i in numbers:
        service.send_message(i,message)

@app.route("/send_crop_prices",methods=["POST"])
def crops_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "CROP PRICES UPDATE BROADCAST MESSAGE:Commodity	MSP for 2018-19 (Rs per quintal): Bajra-1950 ;  Maize-1700;  Ragi-2897; Arhar(Tur)-5675;"
    for i in numbers:
        service.send_message(i,message)

@app.route("/send_ration",methods=["POST"])
def ration_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "RATION DISTRIBUTION @ 7AM;"
    for i in numbers:
        service.send_message(i,message)


@app.route("/send_water",methods=["POST"])
def water_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "WATER SUPPLY @ 3PM - 5PM"
    for i in numbers:
        service.send_message(i,message)


@app.route("/send_electricity",methods=["POST"])
def electricity_update():
    #send
    village_id = request.get_json()["village_id"] #getting the data from the broadcast website
    filee_read = open("village_database/{}.txt".format(village_id),"r")
    numbers = filee_read.read().split(",")
    message = "ELECTRICITY CUTS @ 2AM - 5AM"
    for i in numbers:
        service.send_message(i,message)

user_complaints = {
    "village1": []
}
@app.route("/update_phone_book",methods=["GET"])
def get_all_messages():
    messages = list(service.fetch_message_history())
    #takes the latest message fromevery number
    for i in range(0,len(messages)):
        print(i)
        print(messages[i].content)
        user_number = messages[i].phone
        user_message = messages[i].content
        if("v001" in user_message or "v002" in user_message):     #if user just wants to register
            filee = open("village_database/"+user_message+".txt","a")
            filee.write("," + user_number)
        else: #if user is filing a complaint
            filee = open("user_complaints_" + user_message +".txt","a")
            filee.write(user_number+":"+user_message+"\n")
            user_complaints["village1"].append(user_message)
    
    #displaying the entire database of usercomplaints
    print(user_complaints)
    return 1

@app.route("/view_complaints")
def view():
    return render_template("broadcast_webapp/view_complaints.html")
    
@app.route("/get_complaints",methods=["GET"])
def get_complaints():
    print(user_complaints)
    return user_complaints


if __name__ == "__main__" :
    app.run(debug=True,port=5004,host="0.0.0.0")