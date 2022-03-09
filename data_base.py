from pymongo import MongoClient
import os
import dotenv

dotenv.load_dotenv()

# Mongo Client
dataClient = MongoClient(os.getenv("mongo"))

db = dataClient.users
collection = db.userCollection


def createAccount(ID):
    """
    Creates an object on mongodb for the specified user
    Each new account will start with 100 dollars
    """

    user = {
        "discordID": ID,
        "balance": 100
    }
    
    collection.insert_one(user)


def viewBalance(ID):
    userObject = collection.find_one({"discordID": ID})
    return userObject["balance"]


def updateBalance(ID, added):
    userObject = collection.find_one({"discordID": ID})
    myQuery = {"balance": userObject["balance"]}
    newValues = {"$set": {"balance": userObject["balance"] + added}}

    collection.update_one(myQuery, newValues)
