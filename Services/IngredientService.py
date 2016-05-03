import uuid
import json
from pprint import pprint

class IngredientService:
	def __init__(self):
		with open('ingrediants.json') as json_data:
			self.ingredients = json.load(json_data)
			json_data.close()


	def getIngredientUUIDs(self, ids):
		for id in ids:
			print id
			#if not isinstance(id, uuid.UUID) :
				#raise ValueError("Expecting UUID")

		ingredients = []

		for id in ids:
			str_id = str(id)
			if str_id in self.ingredients:
				ingredients.append(self.ingredients[str_id])
			else:
				ingredients.append("Ingredient {0} not found".format(str_id))
		print(ingredients)
		return ingredients




if __name__ == '__main__':
	service = IngredientService()
	#Test for invalid value
	try:
		service.getIngredientUUIDs(["bad value"])
		print "Failed invalid value test"
	except ValueError:
		print "Pass invalid value test"
	except:
		print "failed invalid value test"

	#Test for valid empty value
	value = service.getIngredientUUIDs([uuid.UUID('{00000000-0000-0000-0000-000000000000}')])

	if len(value) == 1 and value[0] == "Ingredient {0} not found".format(str(uuid.UUID('{00000000-0000-0000-0000-000000000000}'))) :
		print "Pass empty value"
	else:
		print "Failed empty value"

	#Test for valid key no value
	value = service.getIngredientUUIDs([uuid.UUID('{00000000-0000-0000-0000-000000000001}')])
	if len(value) == 1 and bool(value[0]) == False:
		print "Pass key no value"
	else:
		print "Failed key no value"

	#Test for valid value
	value = service.getIngredientUUIDs([uuid.UUID('{00000000-0000-0000-0000-000000000002}')])
	if bool(value) == True :
		print "Pass key value"
	else:
		print "Failed key value"

	#Test for multiple value
	value = service.getIngredientUUIDs([uuid.UUID('{00000000-0000-0000-0000-000000000002}'),uuid.UUID('{00000000-0000-0000-0000-000000000003}')])
	if len(value) == 2 :
		print "Pass multiple value"
	else:
		print "Failed multiple value"
