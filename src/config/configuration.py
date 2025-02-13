# Configuration

from pathlib import Path

from src.utils.common import read_yml


class ConfigurationManager:
    def __init__(self, config_filepath):
        self.config = read_yml(config_filepath)
        
        # create artifacts root directory
        artifacts_root = self.config.get("artifacts_root", "artifacts")
        Path(artifacts_root).mkdir(parents=True, exist_ok=True)
        
    def get_data_ingestion_config(self):
        ingestion_config = self.config.get("data_ingestion")
        
        return {
            "root_dir": Path(ingestion_config.get("root_dir")), 
            "ingested_data_file": Path(ingestion_config.get("ingested_data_file"))
            }