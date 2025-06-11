from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
    client = MongoClient('localhost', 27017, serverSelectionTimeoutMS=2000)
    # Force connection on a request as the connect=True parameter of MongoClient is deprecated
    client.admin.command('ping')
    print("✅ MongoDB is running and accessible.")
except ConnectionFailure:
    print("❌ MongoDB is not accessible or not running.")
