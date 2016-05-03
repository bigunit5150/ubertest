from flask import Flask, request
from flask_restful import Resource, Api
import ../Services/RecipeService

app = Flask(__name__)
api = Api(app)
recipes_service = RecipeService()

class HelloWorld(Resource):
	def get(self):
		return {'Hello':'World'}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
	app.debug = True
	app.run()