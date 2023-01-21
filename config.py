import pymongo
import certifi


connection_str = "mongodb+srv://kternity:test1234@cluster0.ufjzvii.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_str, tlsCAFile=certifi.where())
db = client.get_database("Onlinestore")