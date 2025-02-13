# Component
import os
from pathlib import Path
from pymongo.mongo_client import MongoClient
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


class DataIngestion:
    def __init__(self, data_ingestion_config):
        self.data_ingestion_config = data_ingestion_config
        
        # create ingestion artifacts root dir
        Path(self.data_ingestion_config.get("root_dir")).mkdir(parents=True, exist_ok=True)
        
    def ingest_data(self):
        mongodb_uri = os.getenv("MONGODB_URI")
        database_name = os.getenv("DATABASE")
        collection_name = os.getenv("COLLECTION")

        client = MongoClient(mongodb_uri)
        db = client[database_name]
        collection = db[collection_name]
        
        try:
            data= collection.find()
            df = pd.DataFrame(list(data))
            print(f"loaded data from mongodb. dataframe shape: {df.shape}")
            
            df_save_path = self.data_ingestion_config.get("ingested_data_file")
            
            # make parent directory
            Path(df_save_path).parent.mkdir(parents=True, exist_ok=True)
            
            # save dataframe
            df.to_csv(df_save_path, index=False)
            
        except Exception as e:
            raise e
        