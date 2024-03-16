from .IFileValidation import IFileValidation
from baselineCsv.CsvFile import Csv_File
from fileValidation.fileErrors import FileNotFoundErr, WrongFileExtensionErr
import os

class ValidateCsv(IFileValidation):

    def __init__(self, csv_file: Csv_File):
        self.csv_file = csv_file

    def doesFileExists(self) -> bool:
        return os.path.exists(self.csv_file.path)
        
    def isExtensionValid(self) -> bool:
        return self.csv_file.path.endswith('.csv')
    
    def validate(self) -> bool:
         #check that the local csv file exists.
        if not self.doesFileExists():
            raise FileNotFoundErr(f'Baseline csv file with path: {self.csv_file.path} could not be found')
        #check if the extension s correct
        if not self.isExtensionValid():
            raise WrongFileExtensionErr(f'File with path: {self.csv_file.path} is not of csv extension')
    
