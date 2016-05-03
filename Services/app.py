from flask import Flask, request
from flask_restful import Resource, Api, abort
from RecipeService import RecipeService
from IngredientService import IngredientService
from werkzeug.routing import BaseConverter
import json
import uuid

app = Flask(__name__)
api = Api(app)
recipes_service = RecipeService()
ingredients_service = IngredientService()

class uuidListConverter(BaseConverter):
	# at least one uuid seperated by ;, with optional trailing ;
	regex = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}(?:;[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})*;?'

	def to_python(self,value):
		return [uuid.UUID(x) for x in value.split(';')]

	def to_url(self,value):
		return ';'.join(str(x) for x in value)


class Recipes(Resource):
	def get(self,id):
		try:
			value = recipes_service.getIngredientUUIDs(id)
			return json.dumps(value)
		except ValueError:
			abort(400)
		except:
			abort(500)

class Ingredients(Resource):
	def get(self,ids):
		#try:
		value = ingredients_service.getIngredientUUIDs(ids)
		return json.dumps(value)
		#except ValueError:
			#abort(400)
		#except:
		#	abort(500)

app.url_map.converters['uuid_list'] = uuidListConverter

api.add_resource(Recipes,'/v0/recipes/<uuid:id>')
api.add_resource(Ingredients,'/v0/ingredients/<uuid_list:ids>')

if __name__ == '__main__':
	app.debug = True
	app.run()
