from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    project_source_file: Path
    project_raw_file: Path

@dataclass
class DataValidationConfig:
    root_dir:Path
    data_file:Path 
    STATUS_FILE:Path 
    all_schema:dict
