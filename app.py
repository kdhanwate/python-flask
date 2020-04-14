from flask import Flask
from pymongo import MongoClient
from flask import request
import json
import conn
from bson.json_util import dumps
app = Flask(__name__)

@app.route("/hello/")
def hello():
    return "hello"
@app.route("/add_contact", methods=["POST"])
def add_contact():
    try:
        db = conn.makeConnection() 
        data = json.load(request.data)
        user_name=data['name']
        user_contact=data['contact']
        if user_name and user_contact:
            status = db.Contact.insert_one({"name":user_name}, {"contact":user_contact})
        return dumps({'message':'SUCCESS'})
    except Exception as e:
        return dumps({'error': str(e)})
@app.route("/get_all_contact", methods=['GET'])
def get_all_contact():
    try:
        db = conn.makeConnection()
        contacts = db.Contacts.find()
        return dumps(contacts)
    except Exception as e:
        return dumps({'error': str(e)})