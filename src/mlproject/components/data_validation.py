import os
from src.mlproject import logger
import pandas as pd
from pathlib import Path
from src.mlproject.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:  # renamed
        try:
            validation_status = None

            data = pd.read_csv(self.config.local_data_file)
            all_cols = list(data.columns)
            schema_cols = self.config.all_schema.keys()

            for col in all_cols:
                if col not in schema_cols:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write("Validation_status: False")
                    break
            else:
                validation_status = True
                with open(self.config.status_file, "w") as f:
                    f.write("validation_status: True")

            return validation_status

        except Exception as e:
            raise e
