import pymongo
#from sensor.constant.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    client = None
    def __init__(self, database_name='ineuron') -> None:
        try:
            if MongoDBClient.client is None:
               mongo_db_url  = "mongodb+srv://avnish:Aa327030@cluster0.or68e.mongodb.net/admin?authSource=admin&replicaSet=atlas-desfdx-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"
               MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("collection name:",mongodb_client.database.list_collection_names())
