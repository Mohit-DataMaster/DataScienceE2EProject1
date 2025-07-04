from src.datascience.components.data_transformation import DataTransformation
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):#

        try:
            with open(Path('artifacts\data_validation\status.txt'), 'r') as f:
                for line in f:
                    if line.strip().startswith('[Status]'):
                        status = line.split(":", 1)[1].strip()
            if status == 'True':
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception('Data Schema is not valid')
            
        except Exception as e:
            raise e
