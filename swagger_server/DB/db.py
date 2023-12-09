from swagger_server.config import configuration
from pymongo import MongoClient

from datetime import datetime
from bson import ObjectId

class Database(object):
    def __init__(self):
        self.client = MongoClient(configuration['db']['url'])
        self.db = self.client[configuration['db']['name']]

    def insert(self, collection, item):
        item["date_created"] = datetime.now()
        item["date_updated"] = datetime.now()
        inserted = self.db[collection].insert_one(item)
        if inserted.inserted_id:
            return {"status":200, "id": str(inserted.inserted_id)}

    def find(self, collection, conditions={}, project=None, sort=None, limit=0, cursor=False):
        if "_id" in conditions: conditions["_id"] = ObjectId(conditions["_id"])

        results = self.db[collection].find(filter=conditions, projection=project, limit=limit, sort=sort)
        if cursor: return results

        results = list(results)
        for i in range(len(results)):
            if "_id" in results[i]: results[i]["_id"] = str(results[i]["_id"])

        return results

    def find_by_id(self, collection, id, project=None):
        result = self.db[collection].find_one({"_id": ObjectId(id)}, projection=project)
        if result is None: return {"message": "Not Found", "status": 404}

        if "_id" in result:
            result["_id"] = str(result["_id"])

        return result

    def update(self, collection, id, item):
        conditions = {"_id": ObjectId(id)}
        item["updated"] = datetime.now()
        set_obj = {"$set": item}

        updated = self.db[collection].update_one(conditions, set_obj)
        if updated.matched_count == 1:
            return {"status": 200, "message": "Updated Successfully"}

    def delete(self, collection, id):
        deleted = self.db[collection].delete_one({"_id": ObjectId(id)})
        if deleted.deleted_count == 1:
            return {"status":200, "message": "Deleted Successfully"}
        else:
            return {"status": 500, "message": "No item deleted"}