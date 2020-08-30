import os
from flask import Flask, redirect, url_for, request, render_template, abort
from flask_restful import Api, Resource, reqparse
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

posts = {

}

post_put_args = reqparse.RequestParser()
post_put_args.add_argument("likes", type=int, required=True)
post_put_args.add_argument("comments", type=int, required=True)

class Post(Resource):
	def get(self, id):
		if id not in posts:
			abort(404)
		else:
			return posts[id]

	def put(self,id):
		args = post_put_args.parse_args()
		posts[id] = args
		return posts[id], 201

class User(Resource):
	def get(self, name):
		if name not in Users:
			abort(404)
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

api.add_resource(Index, "/")
api.add_resource(User, "/<string:name>")
api.add_resource(Post, "/p/<string:id>")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
