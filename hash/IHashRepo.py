from abc import ABC, abstractmethod
from .Hash import Hash

class IHashRepo(ABC):
    
   
    @abstractmethod
    def post_file_hash(self, hash: str, txt_path:str) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def retrieve_all_hashes(self) -> list:
        raise NotImplementedError
    @abstractmethod
    def retrieve_by_id(self, id: int) -> Hash:
        raise NotImplementedError

class IHashRepoCSV():
    @abstractmethod
    def post_file_hash(self, hash: str,local_file_path:str ,local_csvFile_path: str) -> None:
        raise NotImplementedError
    @abstractmethod
    def retrieve_all_hashes(self, local_csvFile_path: str) -> list:
        raise NotImplementedError
    @abstractmethod
    def retrieve_by_id(self, local_csvFile_path: str, id: int) -> Hash:
        raise NotImplementedError
    