from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()
baseline_csv_path = os.getenv("BASELINE_CSV_PATH")
@dataclass
class Csv_File:
    path: str = baseline_csv_path
    length: int = 3

    
