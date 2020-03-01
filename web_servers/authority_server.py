from flask import Flask, render_template
from pymongo import MongoClient
import requests

app = Flask(__name__)

#THIS IS THE MAIN AUTHORITY SERVER
#THIS WILL HAVE ACCESS TO 4 DATABASES

#DEFININING DATABASE HANDLERS
client = MongoClient('localhost', 27017) #connecting to Mongo

db1 = client.resource_states #connecting to the database
db1_handler = db1.resource_states #connecting to the collection 

db2 = client.villages_info #connecting to the database
db2_handler = db2.villages_info #connecting to the collection 

db3 = client.villagers_info #connecting to the database
db3_handler = db3.villagers_info #connecting to the collection 

db4 = client.village_complaints #connecting to the database
db4_handler = db4.village_complaints #connecting to the collection 
"""
TECHNICALLY
EACH VILLAGE WILL HAVE 3 RECORDS IN THE COLLECTION.
1 RECORD FOR EVERY VILLAGE
"""
resource_db_data = {
    "village_name" : "",
    "resource_name" : "",
    "resource_state" : "",
    "resource_activation_time" : "",
    "resouce_deactivation_time" : "",
    "resource_activation_date" : "",
    "resouce_deactivation_date" : "",
    
}

villager_db_data = {
    "villager_name" : "",
    "village_identifiation_type" : "",
    "villager_identification_value": "",
    "village_name": "",
    "villager_contact_phone" : "",
    "villager_contact_landline" : "",
    "villager_age" : "",
    "villager_occupation_status": ""
}

villages_db_data = {
    "village_name"  : "",
    "village_pos_lat" : "",
    "village_pos_lon" : "",
    "village_population" :"",
    "village_state" : "",
    "village_score" : "",
    "village_govt_auth" : "",
    "village_govt_auth_contact" : "",
    "village_local_auth": "",
    "village_local_auth_contact" : ""
}

@app.route("/",methods=["GET"])
def index_page():
    return render_template("authority_webapp/authority.html")

@app.route("/update_resource",methods=["POST"])
def update_resource_status():
    #getting all the data in json format , made as an API call
    try:
        resource_db_data["village_name"] = request.get_json()["resource_name"]
        resource_db_data["resource_name"] = request.get_json()["resource_name"]
        resource_db_data["resource_state"] = request.get_json()["resource_state"]
        resource_db_data["resource_activation_time"] = request.get_json()["resource_activation_time"]
        resource_db_data["resouce_deactivation_time"] = request.get_json()["resouce_deactivation_time"]
        resource_db_data["resource_activation_date"] = request.get_json()["resource_activation_date"]
        resource_db_data["resouce_deactivation_date"] = request.get_json()["resouce_deactivation_date"]
    except:
        abort(400)

    #now we just need to update the specific village's ; specific resources
    #let's access the village records
    #we need to access only those records where village name and resource name matches

    try:
        new_record = resource_db_data
        newvalues = { "$set": new_record }

        myquery = {"village_name": village_name}
        db1_handler.update_one(myquery, newvalues) #find the document with myquery and update it with the newvalues
        return 1
    except:
        return 0


@app.route("/add_villager",methods=["POST"])
def add_villager():
    #this function will allow us to add a new villager to the databasesystem
    try:
        villager_db_data["villager_name"] = request.get_json()["villager_name"]
        villager_db_data["villager_identification"] = request.get_json()["villager_identification"]
        villager_db_data["village_name"] = requests.get_json()["village_name"]
        villager_db_data["village_contact_phone"] = requests.get_json()["village_contact_phone"]
        villager_db_data["village_contact_landline"] = requests.get_json()["village_contact_landline"]
        villager_db_data["villager_age"] = requests.get_json()["villager_age"]       
        villager_db_data["villager_occupation_status"] = requests.get_json()["villager_occupation_status"]  
    except:
        abort(400)
    
    #now we just need to insert this data into the db
    #NOT DOING ANY ERROR HANDLING RIGHT NOW AS WE DO NOT HAVE MUCH TIME
    
    #hence directly inserting everything into the database
    #we add villager_db_data directly into the daatbase
    #db_handler ==== db3_handler
    try:
        db3_handler.insert_one(villager_db_data) 
        return 1
    except:
        return 0
    
@app.route("/add_village",methods=["PUT"])
def add_village():
    #this api will be used to add a new village into the database
    try:
        villages_db_data["village_name"] = request.get_json()["village_name"]
        villages_db_data["village_pos_lat"] = request.get_json()["village_pos_lat"]
        villages_db_data["village_pos_lon"] = requests.get_json()["village_pos_lon"]
        villages_db_data["village_state"] = requests.get_json()["village_state"]
        villages_db_data["village_score"] = requests.get_json()["village_score"]
        villages_db_data["village_govt_auth"] = requests.get_json()["village_govt_auth"]       
        villages_db_data["village_govt_auth_contact"] = requests.get_json()["village_govt_auth_contact"]
        villages_db_data["village_local_auth"] = requests.get_json()["village_local_auth"]       
        villages_db_data["village_local_auth_contact"] = requests.get_json()["village_local_auth_contact"]  
    except:
        abort(400)

    #now we just need to insert this data into the db
    #NOT DOING ANY ERROR HANDLING RIGHT NOW AS WE DO NOT HAVE MUCH TIME
    
    #hence directly inserting everything into the database
    #we add villager_db_data directly into the daatbase
    #db_handler ==== db3_handler
    try:
        db2_handler.insert_one(villages_db_data) 
        return 1
    except:
        return 0


@app.route("/get_complaints",methods=["GET"])
def get_complaints():
    try:
        complaint_resource_tag = requests.get_json("complaint_resource_tag")
    except:
        abort(400)
    

    #now we need to access the complaints database
    data_retrieved  = db4_handler.find({"complaint_resource_tag" : complaint_resource_tag},{"_id":0}) 
    return json.dumps(list(data_retrieved))




    
    






    


if __name__ == "__main__" :
    app.run(debug=True,port=5001)