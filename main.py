import sys
from src.pipeline.data_ingestion_pipeline import run_ingestion_pipeline
from src.utils.logger import logging
from src.utils.exception import CustomException


if __name__=="__main__":
    run_ingestion_pipeline()
    logging.info(f"Done !============!")
    
    
    
    