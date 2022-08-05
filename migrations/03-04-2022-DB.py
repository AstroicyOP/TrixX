"""
This is a one-shot script used to migrate all data's to new database.
6 December 2021
"""

import config
from pymongo import MongoClient

client = MongoClient(config.DATABASE_URI)
db = client[config.DATABASE_NAME]

result = db["member"].aggregate(
    [
        {"$match": {"suspended": {"$ne": True}}},
        {"$unwind": {"path": "$trixx", "includeArrayIndex": "idx"}},
        {"$addFields": {"trixxowner_id": "$_id"}},
       
    ],
    allowDiskUse=True,
)