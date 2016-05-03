import json
import uuid
import requests

recipe_base_url = "http://localhost:5000/v0/"
ingredient_base_url = "http://localhost:5001/v0/"

class RecipeProxy:
	def get_with_retry(self,url):
	 	retryCnt = 0
	 	while retryCnt < 10:
	 		try:
	 			response = requests.get(url,timeout=0.5)
	 			break
	 		except requests.exceptions.Timeout:
	 			print("Request has timed out")
	 			retryCnt += 1
	 			if retryCnt == 10 :
	 				raise requests.exceptions.Timeout

	 	return response

	def getrecipe(self,id):
		url = "{0}recipes/{1}".format(recipe_base_url,id)
		response = self.get_with_retry(url)
		#response = requests.get(url)

		ingredients = json.loads(response.json())
		if ingredients != None and len(ingredients) > 0:
			needPrefix = False
			url = "{0}ingredients/".format(ingredient_base_url)
			for i in ingredients:
				if needPrefix == True:
					url+=";{0}".format(i)
				else:
					url += "{0}".format(i)
					needPrefix = True

			response = self.get_with_retry(url)
			#response = requests.get(url)
			recipe = json.loads(response.json())

			response = { id: response.text }
			return response
		#print recipe

if __name__ == '__main__':
	proxy = RecipeProxy()
	uid = raw_input("Enter your recipe id: ")
	#'00000000-0000-0000-0000-000000000002'
	response = proxy.getrecipe(uuid.UUID(uid))
	if response == None:
		print "Nothing found for that id"
	else:
		for i in response:
			print i, response[i]