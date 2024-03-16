from hash.csvRepoClass import Csv_Repo
from hash.getHashService import HashServiceLocal
from fileValidation.validateCsv import ValidateCsv
from baselineCsv.CsvFile import Csv_File
from hash.createHashService import CreateHashService
from hash.hashMonitor import HashMonitor
from fileValidation.validateTxt import ValidateTxt
from hash.fileIntegrityService import File_integrity_service

csv_file = Csv_File()
validate_file_csv = ValidateCsv(csv_file)
csv_repo = Csv_Repo(csv_file,validate_file_csv)
hash_service_local = HashServiceLocal(csv_repo)
hash_monitor = HashMonitor()
validate_file_txt = ValidateTxt()
createHashService = CreateHashService(csv_repo,hash_monitor,validate_file_txt)
file_integrity_service = File_integrity_service(csv_repo,hash_monitor,validate_file_txt)




