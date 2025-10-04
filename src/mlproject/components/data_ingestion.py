# components

import os
import urllib.request as request
import zipfile
from src.mlproject import logger
from src.mlproject.utils.common import get_size
from pathlib import Path
from src.mlproject.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig) -> None:
        self.config = config

    def download_data(self) -> Path:
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )
        return Path(self.config.local_data_file)

    def extract_zip_file(self, zip_file_path: Path) -> Path:
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)  # always ensure dir exists

        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"File extracted to {unzip_path}")

        return unzip_path
