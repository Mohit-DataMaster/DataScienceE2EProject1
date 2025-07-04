from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configuration import ConfigurationManager
from src.datascience import logger
from pathlib import Path

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):#

        try:
            config=ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_training = ModelTrainer(model_trainer_config)
            model_training.model_train()
        except Exception as e:
            raise e
