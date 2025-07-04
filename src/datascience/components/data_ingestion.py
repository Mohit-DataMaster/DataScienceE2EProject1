import os
import shutil
from src.datascience import logger
from src.datascience.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config
    
    def copy_file(self):

        try:
            # Copy original data to artifact folder
            shutil.copy(self.config.project_source_file, self.config.project_raw_file)
        except FileNotFoundError:
            logger.error(f"Source file not found: {self.config.project_source_file}")
