from pymongo import MongoClient
from decouple import config

# Load MongoDB URI from environment
MONGO_URI = config("MONGO_URI", default="mongodb://localhost:27017")

# Establish the connection
client = MongoClient(MONGO_URI)
db = client.assignment_portal  # Database name
