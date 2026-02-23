from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

_client = None
_db = None


def get_db():
    global _client, _db
    if _db is not None:
        return _db

    uri     = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    db_name = os.getenv('DB_NAME',   'webdevquiz')

    try:
        _client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        _client.admin.command('ping')
        _db = _client[db_name]
        print(f'✅ MongoDB connected → {db_name}')
    except ConnectionFailure as e:
        print(f'⚠️  MongoDB unavailable: {e}')
        _db = None

    return _db


def get_collection(name):
    db = get_db()
    return db[name] if db is not None else None
