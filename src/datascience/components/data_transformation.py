import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience import logger
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # EDA/Feature Engineering, Transformation techniques like scaling, PCA or standardization can be performed here

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_file)
        train, test = train_test_split(data) # 75/25 split and shuffle=True

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = None)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = None)

        logger.info("Data split into Train and test")
        logger.info(f"train shape: {train.shape}")
        logger.info(f"test shape: {test.shape}")

        print(train.shape, test.shape)