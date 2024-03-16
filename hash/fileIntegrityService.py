from .IHashRepo import IHashRepo
from .IHashMonitor import IHashMonitor
from fileValidation.IFileValidation import IFileValidation

class File_integrity_service():
    def __init__(self, repo:IHashRepo, hashMonitor:IHashMonitor,validateTxt: IFileValidation ):
        self.repo = repo
        self.hashMonitor = hashMonitor
        self.validateTxt = validateTxt
    def check_single_file_integrity(self, fileId:str)-> bool:
        #retrieve object of type Hash
        hash = self.repo.retrieve_by_id(fileId)
        #check that file path still exists in the local file system
        self.validateTxt.doesFileExists(hash.path)

        return self.hashMonitor.check_file_integrity(hash.fileHash,hash.path)




        


        
