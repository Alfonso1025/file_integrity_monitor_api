from .IHashRepo import IHashRepo


class HashServiceLocal():
    def __init__(self, repo:IHashRepo):
        self.repo = repo
        
        
    def get_all_hashes(self):
        
        return self.repo.retrieve_all_hashes()
    
    def get_hash_byId(self, fileId: int):
       
        return self.repo.retrieve_by_id(fileId)