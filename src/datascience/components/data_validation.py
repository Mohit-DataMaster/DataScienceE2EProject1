import os
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self):
        try:
            data = pd.read_csv(self.config.data_file)
            all_cols = data.columns

            all_schema = self.config.all_schema.keys()
            all_schema_datatypes = self.config.all_schema

            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Validation status:\n")
            flag = True
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "a") as f:
                        f.write(f"Validation status for {col}: {validation_status}\n")
                else:
                    if data[col].dtype == all_schema_datatypes[col]:
                        validation_status = True
                        Datatype_status = True
                        with open(self.config.STATUS_FILE, "a") as f:
                            f.write(f"Validation status for {col}: {validation_status}, Column Datatype validation: {Datatype_status}\n")
                    else:
                        flag = False
                        validation_status = True
                        Datatype_status = False
                        with open(self.config.STATUS_FILE, "a") as f:
                            f.write(f"Validation status for {col}: {validation_status}, Column Datatype validation: {Datatype_status}\n")
            with open(self.config.STATUS_FILE, "a") as f:
                f.write(f"[Status] Complete Validation Check: {flag}\n\n")
            return validation_status
        
        except Exception as e:
            raise e
                    