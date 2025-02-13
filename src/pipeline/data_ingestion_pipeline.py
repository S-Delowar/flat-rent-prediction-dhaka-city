# pipeline:
import sys
from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager
from src.utils.constant import CONFIG_FILE_PATH
from src.utils.logger import logging
from src.utils.exception import CustomException




def run_ingestion_pipeline():
    try:
        logging.info("Getting Data Ingestion Config")
        config = ConfigurationManager(config_filepath = CONFIG_FILE_PATH)
        ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(ingestion_config)
        data_ingestion.ingest_data()
        logging.info("Completed Ingestion of data")
    except Exception as e:
        raise CustomException(str(e), sys)

    