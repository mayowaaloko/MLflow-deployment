import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from src.mlproject import logger
from src.mlproject.entity.config_entity import DataTransformationConfig

print(">>> DataTransformation module loaded successfully <<<")


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def initiate_data_transformation(self):
        logger.info("Initiating data transformation...")
        self.transform_data()

    def transform_data(self):
        df = pd.read_csv(self.config.data_path)
        logger.info(f"Original Data Shape: {df.shape}")

        # Example transformation: train-test split
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
        logger.info(f"Train Data Shape: {train_df.shape}")
        logger.info(f"Test Data Shape: {test_df.shape}")

        # Save transformed data
        train_df.to_csv(self.config.root_dir / "train.csv", index=False)
        test_df.to_csv(self.config.root_dir / "test.csv", index=False)
        logger.info("Data transformation completed.")
