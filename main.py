from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.pipeline.train_pipeline import TrainPipeline
import sys

def test_exception():
    try:
        x=100/0
    except Exception as ex:
        raise SensorException(ex,sys)    

if __name__ == '__main__':
    #mongodb_client = MongoDBClient()
  #  print("collection name:",mongodb_client.database.list_collection_names())
    try:
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
    except Exception as e:
        print(e)    