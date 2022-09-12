from pymongo import MongoClient
from login import login

uri = f'mongodb+srv://{login}@cluster0.m38rx.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(uri)
database = client['estauranteLunary']
collection = database['CardapioLunary']

print(collection.find_one())