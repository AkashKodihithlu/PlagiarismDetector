from pymongo import MongoClient
import pymongo
from datetime import datetime
from bson import ObjectId
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# MongoDB connection using environment variable
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

db = client["codeguard"]

users_collection = db["users"]
scans_collection = db["scan_results"]

# Ensure indexes for performance
users_collection.create_index("username", unique=True)
scans_collection.create_index("user_id")
scans_collection.create_index([("created_at", pymongo.DESCENDING)])


def save_scan_result(
    user_id: ObjectId,
    filename: str,
    language: str,
    line_count: int,
    char_count: int,
    algorithm_detected: str,
    similarity: dict,
    copied_lines: dict
) -> ObjectId:
    """
    Saves a plagiarism scan result to MongoDB.
    Returns the inserted ObjectId.
    """

    doc = {
        "user_id": user_id,
        "filename": filename,
        "language": language,
        "line_count": line_count,
        "char_count": char_count,
        "algorithm_detected": algorithm_detected,
        "similarity": similarity,
        "copied_lines": copied_lines,
        "created_at": datetime.utcnow()
    }

    result = scans_collection.insert_one(doc)

    return result.inserted_id