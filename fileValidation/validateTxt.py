from .IFileValidation import IFileValidation
from fileValidation.fileErrors import FileNotFoundErr, WrongFileExtensionErr
import os

class ValidateTxt(IFileValidation):

    
    def doesFileExists(self,txt_file_path) -> bool:
        return os.path.exists(txt_file_path)
        
    def isExtensionValid(self,txt_file_path ) -> bool:
        return txt_file_path.endswith(('.txt', '.docx'))
    
    def validate(self, txt_file_path) -> bool:
         #check that the local csv file exists.
        if not self.doesFileExists(txt_file_path):
            raise FileNotFoundErr(f'Baseline csv file with path: {self.txt_file_path} could not be found')
        #check if the extension s correct
        if not self.isExtensionValid(txt_file_path):
            raise WrongFileExtensionErr(f'File with path: {self.txt_file_path} is not of csv extension')
    
