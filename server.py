from flask import Flask, request
import json
from mock_data import catalog
from config import db
from flask_cors import CORS

app = Flask("server")
CORS(app) # disable CORS to allow request from any origin
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
   cursor = db.products.find({})
   results = []
   for prod in cursor:
      prod["_id"] = str(prod["_id"]) #fix _id issue
      results.append(prod)

   return json.dumps(results)

#save product
@app.post("/api/catalog")
def save_product():
   product = request.get_json()
   db.products.insert_one(product)

   product["_id"] = str(product["_id"]) #clean the objectId('asd') from the obj
   
   return json.dumps(product)




#get all products that belong to a category
@app.get("/api/catalog/<category>")
def get_by_category(category):
   cursor = db.products.find({"category":category})
   # create a list, travel the cursor, fix the id, add it to the list and return the list
   results = []
   for prod in cursor: 
      prod["_id"] = str(prod["_id"])
      results.append(prod)   
   return json.dumps(results)


#return all products whose title CONTAINS the title variable
@app.get("/api/catalog/search/<title>")
def search_by_title(title):
   cursor = db.products.find({"title": {"$regex": title, "$options": "i"}}) #title contains this text
   results = []
   for prod in cursor:
      prod["_id"] = str(prod["_id"])
      results.append(prod)

   return json.dumps(results)


# create a get endpoint that returns the number of products in the catalog
@app.get("/api/product/count")
def count_products():
   count = db.products.count_documents({})
   return json.dumps(count)
   #json.dumps(len(catalog))




#End point whose price is lower than a specific $
@app.get('/api/product/cheaper/<price>')
def search_by_price(price):
     cursor = db.products.find({})
     results = []
     for prod in cursor:
      if prod["Price"] < float(price):
            prod["_id"] = str(prod["_id"])
            results.append(prod)

      return json.dumps(results)




# create a get endpoint that returns the cheapest product
@app.get("/api/product/cheapest")
def get_cheapest():
   cursor = db.products.find({})
   answer = cursor[0]
   for prod in cursor:
      if prod["Price"] < answer["Price"]:
         answer = prod

   answer["_id"] = str(answer["_id"])
   return json.dumps(answer)


#create a list of numbers 1 to 20 except 13 & 17 and return the list as json
@app.get('/test/numbers')
def get_numbers():
   result = []
   for n in range(1,21):
      if n != 13 and n != 17:
         result.append(n)

   return json.dumps(result)

app.run(debug=True)