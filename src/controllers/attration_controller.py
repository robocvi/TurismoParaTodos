import json
from bson import ObjectId, json_util
from src.settings import CONNECTION_STRING
from pymongo import MongoClient        

class AttrationController:
    @staticmethod
    def all_attrations():
        client = MongoClient(CONNECTION_STRING)
        db = client['TurismoParaTodos']

        collection = db['TurismoParaTodos']
        atracciones = list(collection.find())
        atracciones_json = json.loads(json_util.dumps(atracciones))

        return {"response": atracciones_json}
        

