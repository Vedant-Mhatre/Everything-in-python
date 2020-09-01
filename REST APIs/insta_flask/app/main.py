import os
import json
from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient( os.environ['DB_PORT_27017_TCP_ADDR'],
			27017)
db = client["mydb"]

Users = db.mydb.find()

posts = {

}

post_put_args = reqparse.RequestParser()
post_put_args.add_argument("likes", type=int, required=True)
post_put_args.add_argument("comments", type=int, required=True)

class todo(Resource):
	def get(self):
		# name1 = client.list_database_names()
		_items = db.mydb.find()
		items = [item for item in _items]
		with open("todo.txt", "w") as text_file:
			text_file.write(str(items))
		# print(items)
		return json.dumps(items, default=str)

class Post(Resource):
	def get(self, id):
		with open("getpost.txt", "w") as text_file:
			temp1 = db.mydb.find()
			items = [item for item in temp1]
			text_file.write(str(items[]))
		return json.dumps(items, default=str)

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

class User(Resource):
	def get(self, iname):
		if iname not in Users:
			abort(404)
		else:
			return Users[name]

	def put(self, iname):
		# tempuser = {
		# 	'username':name
		#
		# }
		# tempuser = {"user1": {"email":"user1@gmail.com", "username":"User 1"}}
		new = {
			'dbname':iname[name],
			'dbemail':iname[email]
		}
		db.mydb.insert_one(new)
		return new

class Index(Resource):
	def get(self):
		# storetempdataindb()
		users = [user for user in Users]
		print(users)
		return users

api.add_resource(Index, "/")
api.add_resource(todo, "/todo")
api.add_resource(User, "/<string:iname>")
api.add_resource(Post, "/p/<string:id>")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
