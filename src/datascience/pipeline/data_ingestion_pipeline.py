from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger

STAGE_NAME = "Data Ingestion"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):

        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.copy_file()

if __name__ == "__main__":
    try:
        logger.info(f"---- Stage: {STAGE_NAME} Started ----")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"---- Stage: {STAGE_NAME} Completed ----")
    except Exception as e:
        logger.exception(e)
        raise e

