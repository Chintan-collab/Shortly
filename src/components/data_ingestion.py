import os
import sys

from src.exception import CustomExceptionClass
from src.logger import logging

import pandas as pd
from dataclasses import dataclasses

@dataclasses
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts","train.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion in Progress!!")
        try:
            pass
        except:
            pass