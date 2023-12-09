import pymongo
from swagger_server.config import configuration

myclient = pymongo.MongoClient(configuration['db']['url'])
fuzzy_db = myclient["fuzzy_search"]

Users = fuzzy_db["Users"]
