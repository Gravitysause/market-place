from pymongo import MongoClient
import os
import dotenv

dotenv.load_dotenv()

# Mongo Client
dataClient = MongoClient(os.getenv("mongo"))

db = dataClient.users
collection = db.userCollection

def createAccount(name, balence):
    user = {
        "name": name,
        "balence": balence
    }

    collection.insert_one(user)
