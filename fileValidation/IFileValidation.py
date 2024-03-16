from abc import ABC, abstractmethod

class IFileValidation(ABC):
    @abstractmethod
    def doesFileExists(self)-> bool:
        raise NotImplementedError

    @abstractmethod
    def isExtensionValid(self)-> bool:
        raise NotImplementedError
    @abstractmethod
    def validate(self)-> bool:
        raise NotImplementedError
    
