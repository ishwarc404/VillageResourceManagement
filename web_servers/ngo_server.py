from flask import Flask, render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

#THIS IS THE MAIN AUTHORITY SERVER
#THIS WILL HAVE ACCESS TO 4 DATABASES

#DEFININING DATABASE HANDLERS
client = MongoClient('localhost', 27017) #connecting to Mongo

db2 = client.villages_info #connecting to the database
db2_handler = db2.villages_info #connecting to the collection 

db4 = client.village_complaints #connecting to the database
db4_handler = db4.village_complaints #connecting to the collection 


@app.route("/",methods=["GET"])
def index_page():
    return render_template("ngo_webapp/ngo.html")



if __name__ == "__main__" :
    app.run(debug=True,port=5003)