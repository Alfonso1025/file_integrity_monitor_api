from flask import Blueprint, jsonify, request
from .dependencies import hash_service_local,createHashService,file_integrity_service
from .errors import WrongRowFormatErr, RowNotFoundByIdErr
from fileValidation.fileErrors import FileNotFoundErr,WrongFileExtensionErr
from baselineCsv.CsvFile import Csv_File


# Create a Blueprint for the hash routes
hash_routes = Blueprint('hash_routes', __name__)

# Define a route to get all hashes
@hash_routes.route('/all_hashes', methods=['GET'])
def get_all_hashes():

    try:
        hashes = hash_service_local.get_all_hashes()
        return jsonify(hashes)
    
    except RowNotFoundByIdErr as e:
        return jsonify({'error':str(e)}), 404
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Handle other exceptions gracefully

@hash_routes.route('/get_hash_by_id', methods=['POST'])
def get_hash_byId():
    data = request.json
    path = data.get('csv_path')
    fileId = data.get('fileId')
   
    try:
        hash = hash_service_local.get_hash_byId(fileId)
        return jsonify(hash)
    
    except RowNotFoundByIdErr as e:
        return jsonify({'error':str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500 
    
@hash_routes.route('/add_new_hash', methods=['POST'])   
def add_hash():
    data = request.json
    txt_file_path = data.get('txt_path')
    try:
        createHashService.add_new_hash(txt_file_path)
        return jsonify('file path and hash added to data storage')
    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500 
@hash_routes.route('/single_file_integrity',methods=['POST'])
def check_file_integrity():
    data = request.json
    fileId = data.get('fileId')
    try:
        result = file_integrity_service.check_single_file_integrity(fileId)
        if result:
            return jsonify({"message": "File integrity intact"})
        else:
            return jsonify({"message": "The file has been modified"})
    except Exception as e:
        return jsonify({"message": "An error occurred while checking for file integrity: " + str(e)})



    


    


