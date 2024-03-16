import csv
from .IHashRepo import IHashRepo
from .Hash import Hash
from .errors import WrongRowFormatErr, RowNotFoundByIdErr
from baselineCsv.CsvFile import Csv_File
from fileValidation.IFileValidation import IFileValidation



class Csv_Repo(IHashRepo):


    def __init__(self, csv_file: Csv_File, validateFile: IFileValidation):
        self.csv_file = csv_file
        self.validateFile = validateFile

    def post_file_hash(self, hash:str, txt_file_path:str)-> None:
       
        self.validateFile.validate()
        last_id = 0
        with open(self.csv_file.path, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                last_id = int(row[0])
        new_id = last_id + 1

        with open( self.csv_file.path , mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, txt_file_path, hash])

    def retrieve_all_hashes(self) -> list:
        self.validateFile.validate()
        hashArray = []
        with open(self.csv_file.path, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != self.csv_file.length:
                    print("Invalid row format:", row)
                    raise WrongRowFormatErr(f"Invalid row format: {row}")

                id, path, stored_hash = row
                hashInstance = Hash(path, stored_hash)
                hashArray.append(hashInstance)
        return hashArray
    
    def retrieve_by_id(self,lookForId: int)->Hash:
        self.validateFile.validate()
        with open(self.csv_file.path, mode='r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader: 
                if len(row) != self.csv_file.length:
                    print("Invalid row format:", row)
                    raise WrongRowFormatErr(f"Invalid row format: {row}")
                row_id, path, hash = row
                if row_id == lookForId:
                    return Hash(path,hash)
        raise RowNotFoundByIdErr(f'the hash could not be found by id: {lookForId}')
                    
                


        

                

    



    
    
