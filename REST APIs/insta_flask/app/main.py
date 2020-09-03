import os
import json
from bson.json_util import dumps
from flask import Flask, redirect, url_for, request, render_template, abort, jsonify
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client["mydatabase"]
users = db["myusers"]
posts = db["myposts"]


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

post_args = reqparse.RequestParser()
post_args.add_argument("userid", type=str, required=True)
post_args.add_argument("caption", type=str)
post_args.add_argument("likes", type=int)
post_args.add_argument("comments", type=str)

# POST - for creating new post
#         args - postid, caption, userid
#         return 201
#
# PUT - for updating post
#         args - postid, caption, userid, likes, comments
#               if userid does not belong to postid's original userid it won't \
#               update changes
#         return 200
#
# GET - for getting post
#         args - postid
#         return postid, userid, caption, likes, comments, 200

# if posts.find_one({'postid': id}):
#     return f'Post with id:{id} already exists', 400
# else:
    # args = post_args.parse_args()

class Post(Resource):
    def post(self,id):
        if posts.find_one({'postid': id}):
            return f'Post with id:{id} already exists', 400
        else:
            json_data = request.get_json()
            args = post_args.parse_args()
            new = {'postid':id,
                'userid':args.userid
            }
            posts.insert_one(new)
            return '',201

    def put(self,id):
        args = post_args.parse_args()
        filter = {
            'postid':id,
            'userid':args.userid
        }
        newvalues = {
            '$set':{
                'caption':args.caption,
                'likes':args.likes,
                'comments':args.comments
            }
        }
        posts.update_one(filter, newvalues)
        return '',201

    def get(self, id):
        if posts.find_one({'postid': id}):
            post = posts.find_one({'postid': id})
            resp = dumps(post)
            return resp
        else:
            return 'Error 404 - Post Not Found', 404



user_put_args = reqparse.RequestParser()
user_put_args.add_argument("username", type=str, required=True)
user_put_args.add_argument("email", type=str, required=True)

class User(Resource):
	def get(self, id):
		if users.find_one({'userid': id}):
			user = users.find_one({'userid': id})
			resp = dumps(user)
			return resp
		else:
			return 'Error 404 - User Not Found', 404

	def put(self, id):
		args = user_put_args.parse_args()
		new = {
			'userid':str(id),
			'username':args.username,
			'email':args.email
		}


		# to check if user already exists
		if users.find_one({'userid': id}):
			return '', 409
		else:
			users.insert_one(new)
			return '', 201






class Index(Resource):
	def get(self):
		# storetempdataindb()
		# users = [user for user in Users]
		# print(users)
		return None

api.add_resource(Index, "/")
api.add_resource(todo, "/todo")
api.add_resource(User, "/<string:id>")
api.add_resource(Post, "/p/<string:id>")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
