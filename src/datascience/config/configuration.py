from src.datascience.constants import *
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.entity.config_entity import (DataIngestionConfig, DataValidationConfig, 
                                                    DataTransformationConfig, ModelTrainerConfig,
                                                    ModelEvaluationConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            project_source_file=config.project_source_file,
            project_raw_file=config.project_raw_file
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])
        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            data_file=config.data_file,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )

        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config=self.config.data_transformation

        create_directories([config.root_dir])
        
        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_file=config.data_file,
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema.name
        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            test_data_path=config.test_data_path,
            metric_file_name=config.metric_file_name,
            all_params=params,
            mlflow_uri="https://dagshub.com/mohitsaini.nitk/DataScienceE2EProject1.mlflow",
            target_column=schema.name
        )

        return model_evaluation_config

