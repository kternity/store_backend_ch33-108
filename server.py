# flast is folder Flask is function

from flask import Flask, request
import json
from mock_data import catalog
from config import db


app = Flask("server")

@app.get("/")
def home():
   return "hello from flask"

@app.get("/test")
def test():
   return "This is another endpoint in new folder called 'test'."

@app.get("/about")
def about():
   return "About me: Kenneth Chung"

#############  catalogue API ##########

@app.get("/api/version")
def version():
   version = {
      "V":"V.1.0.1.",
      "name":"Candy Firewall",
   }
   return json.dumps(version)



@app.get("/api/catalog")
def get_catalog():
   return json.dumps(catalog)
      

#save product
@app.post("/api/catalog")
def save_product():
   product = request.get_json()
   db.products.insert_one(product)

   product["_id"] = str(product["_id"]) #clean the objectId('asd') from the obj
   
   return json.dumps(product)



@app.get("/api/catalog/<category>")
def get_by_category(category):
   result = []
   for prod in catalog:
      if prod ["category"].lower() == category.lower():
         result.append(prod)

   return json.dumps(result)



#return all products whose title CONTAINS the title variable
@app.get("/api/catalog/search/<title>")
def search_by_title(title):
   result =[]
   for prod in catalog:
      if title.lower() in prod["title"].lower():
         result.append(prod)

   return json.dumps(result)



# create a get endpoint that returns the number of products in the catalog
@app.get("/api/product/count")
def count_products():
   count = len(catalog)
   return json.dumps(count)
   #json.dumps(len(catalog))



# create a get endpoint that returns the cheapest product
@app.get("/api/product/cheapest")
def get_cheapest():
   answer = catalog[0]
   for prod in catalog:
      if prod["Price"] < answer["Price"]:
         answer = prod

   return json.dumps(answer)





#End point whose price is lower than a specific $
@app.get('/api/product/cheaper/<price>')
def search_by_price(price):
   result = []
   for prod in catalog:
      if prod["Price"] < float(price):
         result.append(prod)

   return json.dumps(result)




#create a list of numbers 1 to 20 except 13 & 17 and return the list as json
@app.get('/test/numbers')
def get_numbers():
   result = []
   for n in range(1,21):
      if n != 13 and n != 17:
         result.append(n)

   return json.dumps(result)

app.run(debug=True)