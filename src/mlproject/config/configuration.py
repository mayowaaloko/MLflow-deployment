from src.mlproject.constants import *
from src.mlproject.utils.common import read_yaml, create_directories
from src.mlproject.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)
from pathlib import Path


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
        schema_file_path: Path = SCHEMA_FILE_PATH,
    ) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)
        create_directories([Path(self.config["artifacts_root"])])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        create_directories([Path(config["root_dir"])])
        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_URL"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"]),
        )

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config["data_validation"]
        schema = dict(self.schema["COLUMNS"])
        create_directories([Path(config["root_dir"])])
        return DataValidationConfig(
            root_dir=Path(config["root_dir"]),
            local_data_file=Path(self.config["data_ingestion"]["local_data_file"]),
            unzip_data_dir=Path(config["unzip_data_dir"]),
            all_schema=schema,
            status_file=Path(config["status_file"]),
        )

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config["data_transformation"]
        create_directories([Path(config["root_dir"])])
        return DataTransformationConfig(
            root_dir=Path(config["root_dir"]),
            data_path=Path(config["data_path"]),
        )

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config["model_trainer"]
        params = self.params["ElasticNet"]
        schema = self.schema["TARGET_COLUMN"]
        create_directories([Path(config["root_dir"])])
        return ModelTrainerConfig(
            root_dir=Path(config["root_dir"]),
            train_data_path=Path(config["train_data_path"]),
            test_data_path=Path(config["test_data_path"]),
            model_name=Path(config["model_name"]),
            alpha=params["alpha"],
            l1_ratio=params["l1_ratio"],
            target_column=schema,
        )
