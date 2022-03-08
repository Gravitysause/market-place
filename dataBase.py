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
        "ballence": 100
    }
    
    collection.insert_one(user)


def viewBallence(ID):
    userObject = collection.find_one()

    if userObject["discordID"] == ID:
        return userObject["ballence"]