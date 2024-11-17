from pymongo import MongoClient
from assignmentapp.utils.db import db

user_collection = db.get_collection("users")

def create_user(data: dict):
    """Create a new user in the database."""
    return user_collection.insert_one(data)

def find_user_by_email(email: str):
    """Find a user by email."""
    return user_collection.find_one({"email": email})
