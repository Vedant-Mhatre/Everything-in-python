from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

Users = {"user1": {"email":"user1@gmail.com", "username":"User 1"},
		"user2": {"email":"user2@gmail.com", "username":"User 2"},
				}

class User(Resource):
	def get(self, name):
		return Users[name]
		
	def post(self):
		return {"userid": "0"}

api.add_resource(User, "/<string:name>")


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
