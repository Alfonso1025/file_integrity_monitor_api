from abc import ABC, abstractmethod

class IHashMonitor(ABC):
    
    @abstractmethod
    def calculate_hash(self, file_path:str)-> str:
        raise NotImplementedError
    def check_hash_integrity(self, storedHash: str)->bool:
          raise NotImplementedError

