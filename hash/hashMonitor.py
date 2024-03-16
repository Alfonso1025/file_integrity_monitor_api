from .IHashMonitor import IHashMonitor
import hashlib

class HashMonitor(IHashMonitor):

    def calculate_hash(self, local_file_path: str) -> str:
        
        try:
            with open(local_file_path, "rb") as file:
                file_hash = hashlib.sha256()
                while chunk := file.read(4096):
                    file_hash.update(chunk)
            return file_hash.hexdigest()
        except Exception as e:
            # Raise the exception with a custom message
            raise Exception("An error occurred during hash calculation: " + str(e))
    
    def check_file_integrity(self, storedHash: str, local_file_path: str) -> bool:
        calculated_hash = self.calculate_hash(local_file_path)
        if storedHash != calculated_hash:
            return False
        return True

        