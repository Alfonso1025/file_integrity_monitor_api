import unittest
import os
import csv
from csvRepoClass import Csv_Repo
#from Hash import Hash
from errors import RowNotFoundByIdEr

class TestCsvRepo(unittest.TestCase):
    def setUp(self):
        # Create a CSV file with sample data
        with open('test_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['1', 'path1', 'hash1'])
            writer.writerow(['2', 'path2', 'hash2'])
            writer.writerow(['3', 'path3', 'hash3'])

    def tearDown(self):
        # Clean up the test data after the test
        os.remove('test_data.csv')
    #test the case in which the id is found
    def test_retrieve_by_id_found(self):
        repo = Csv_Repo()
        columns_len = 3
        idToFind = 2
        result = repo.retrieve_by_id('test_data.csv', columns_len, idToFind)
        self.assertIsInstance(result, Hash)
        self.assertEqual(result.path, 'path2')
        self.assertEqual(result.hash, 'hash2')

    def test_retrieve_by_id_not_found(self):
        repo = Csv_Repo()
        columns_len = 3
        idToFind = 2
        with self.assertRaises(RowNotFoundByIdErr):
            repo.retrieve_by_id('test_data.csv', columns_len, idToFind)

if __name__ == '__main__':
    unittest.main()