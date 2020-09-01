import os
import json
from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient( os.environ['DB_PORT_27017_TCP_ADDR'],
			27017)
db = client["mydatabase"]
users = db["myusers"]
posts = db["myposts"]


post_put_args = reqparse.RequestParser()
post_put_args.add_argument("likes", type=int, required=True)
post_put_args.add_argument("comments", type=int, required=True)

class todo(Resource):
	def get(self):
		# name1 = client.list_database_names()
		with open("todo.txt", "w") as text_file:
			for x in users.find():
				text_file.write(str(x))
			# tempp = json.dumps(dict, indent=4)
			# text_file.write(str(users.find({},{ "_id": 0,"address": 1 })))
			# text_file.write(f"database names:{client.list_database_names()}")
			# text_file.write(f"collection names:{db.list_collection_names()}")
		dict = {}
		for x in users.find():
			dict.update({"key":str(x)})
			#

		# print(items)
		# dict = users.find()
		tempp = json.dumps(dict, indent=4)
		return tempp

class Post(Resource):
	def get(self, id):
		with open("getpost.txt", "w") as text_file:
			temp1 = db.mydb.find()
			# items = [item for item in temp1]
			myquery	= {"postid":id}
			mydoc = db.mydb.find(myquery)
			text_file.write(str(mydoc))
		return json.dumps(mydoc, default=str)

	def put(self,id):
		args = post_put_args.parse_args()
		new = {'postid':str(id),
				'dblikes':args.likes,
				'dbcomments':args.comments
		}
		db.mydb.insert_one(new)
		# posts[id] = args
		with open("Output.txt", "w") as text_file:
			text_file.write(str(new))
		return args,201


user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", type=str, required=True)
user_put_args.add_argument("email", type=str, required=True)

class User(Resource):
	def get(self, iname):
		if iname not in Users:
			abort(404)
		else:
			return Users[name]

	def put(self, iname):
		args = user_put_args.parse_args()
		new = {
			'userid':str(iname),
			'username':args.username,
			'email':args.email
		}
		with open("userput.txt", "w") as text_file:
			text_file.write(str(new))
		users.insert_one(new)
		return 200



class Index(Resource):
	def get(self):
		# storetempdataindb()
		# users = [user for user in Users]
		# print(users)
		return None

api.add_resource(Index, "/")
api.add_resource(todo, "/todo")
api.add_resource(User, "/<string:iname>")
api.add_resource(Post, "/p/<string:id>")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
