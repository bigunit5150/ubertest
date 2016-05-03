import uuid
import json
from pprint import pprint

class RecipeService:
	def __init__(self):
		with open('recipes.json') as json_data:
			self.ingredients = json.load(json_data)
			json_data.close()


	def getIngredientUUIDs(self, id):
		if not isinstance(id, uuid.UUID) :
			raise ValueError("Expecting UUID")

		str_id = str(id)

		if str_id in self.ingredients:
			return self.ingredients[str_id]
		else:
			return None




if __name__ == '__main__':
	service = RecipeService()
	#Test for invalid value
	try:
		service.getIngredientUUIDs("bad value")
		print "Failed invalid value test"
	except ValueError:
		print "Pass invalid value test"
	except:
		print "failed invalid value test"

	#Test for valid empty value
	value = service.getIngredientUUIDs(uuid.UUID('{00000000-0000-0000-0000-000000000000}'))
	if value == None :
		print "Pass empty value"
	else:
		print "Failed empty value"

	#Test for valid key no value
	value = service.getIngredientUUIDs(uuid.UUID('{00000000-0000-0000-0000-000000000001}'))
	print value
	if value != None and not bool(value):
		print "Pass key no value"
	else:
		print "Failed key no value"

	#Test for valid value
	value = service.getIngredientUUIDs(uuid.UUID('{00000000-0000-0000-0000-000000000002}'))
	if bool(value) == True :
		print "Pass key value"
		print value
	else:
		print "Failed key value"
