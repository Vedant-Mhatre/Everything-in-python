import os
from flask import Flask, redirect, url_for, request, render_template
from flask_restful import Api, Resource
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient( os.environ['DB_PORT_27017_TCP_ADDR'],
			27017)
db = client.tododb

Users = db.tododb.find()

# Users = {"user1": {"email":"user1@gmail.com", "username":"User 1"},
# 		"user2": {"email":"user2@gmail.com", "username":"User 2"},
# 		}

class User(Resource):
	def get(self, name):
		if name not in Users:
			return None
		else:
			return Users[name]

	def put(self, name):
		# tempuser = {
		# 	'username':name
		#
		# }
		tempuser = {"user1": {"email":"user1@gmail.com", "username":"User 1"}}
		print("before insert")

		db.tododb.insert_one(tempuser)
		print("after insert")
		print({name})

class Index(Resource):
	def get(self):
		users = [user for user in Users]
		return users

api.add_resource(User, "/<string:name>")
api.add_resource(Index, "/")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
