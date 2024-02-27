# app/db/database.py
from pymongo import MongoClient
from app.core.config import settings
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

client: MongoClient = None
db = None

def connect_to_mongo():
    global client, db
    client = MongoClient('mongodb+srv://anupnair:HzbVctRgK5iU25oB@turf-mongo.x5hhfko.mongodb.net')
    db = client['turfdb']
    logger("db>>", db)

def close_mongo_connection():
    global client
    client.close()
    
def get_db():
    client = MongoClient('mongodb+srv://anupnair:HzbVctRgK5iU25oB@turf-mongo.x5hhfko.mongodb.net')
    db = client['turfdb']
    return db
