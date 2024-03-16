from .IHashRepo import IHashRepo
from .IHashMonitor import IHashMonitor
from fileValidation.IFileValidation import IFileValidation

class CreateHashService():
    def __init__(self, repo:IHashRepo, hashMonitor:IHashMonitor,validateTxt: IFileValidation ):
        self.repo = repo
        self.hashMonitor = hashMonitor
        self.validateTxt = validateTxt
    def add_new_hash(self,txt_file_path:str):
        #validate that the path to the txt file exist
        self.validateTxt.validate(txt_file_path)
        hash = self.hashMonitor.calculate_hash(txt_file_path)
        print('the hash produced is: ', hash)
        self.repo.post_file_hash(hash,txt_file_path)
