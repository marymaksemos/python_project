import os
import unittest
import pickle
from src.file_system import FileSystem

class FileSystemTest(unittest.TestCase):
    """
    A class to test all methods of the FileSystem class.
    Including init() and save() methods.
    """
    def setUp(self):
        """
        A method for set FileSystem class paramters and create an instance of the FileSysttem class.
        """
        self.test_path = 'test_path'
        self.test_name = 'test_file'
        self.test_data = {
            'DEFAULT': [
                {'id': 1, 'name': 'Simon', 'email': 'simon.wei@chasacademy.se',
                    'role': 'Developer'},
                {'id': 2, 'name': 'Melina', 'email': 'melina.asplund@chasacademy.se',
                    'role': 'Developer'},
                {'id': 3, 'name': 'Mary', 'email': 'mary.makseu@chasacademy.se',
                    'role': 'Developer'},
                {'id': 4, 'name': 'Jannatul', 'email': 'jannatul.ferdoese@chasacademy.se',
                    'role': 'Developer'}
            ]
        }
        self.file_system = FileSystem(self.test_path, self.test_name)

    def test_init_loads_data_from_file(self):
        """
        A method to test loading data from the database file after creating an instance of the FileSystem class.
        """
        self.file_system.data = self.test_data
        self.file_system.save()
        file_system2 = FileSystem(self.test_path, self.test_name)
        self.assertEqual(file_system2.data, self.test_data)

    def test_init_creates_file_if_not_exists(self):
        """
        A method to test the case that the database file does not exist.
        In this case, the database file must be created when creating an instance of the FileSystem class.

        """
        path = 'test_path'
        name = 'test_file'
        os.remove(f'{path}/{name}.pkl')
        file_system2 = FileSystem(path, name)
        self.assertTrue(os.path.isfile(f'{path}/{name}.pkl'))
        
    def test_save_writes_data_to_file(self):
        """
        A method to test saving data to the database file. The save method of the Filesystem class should do this.
        """
        self.file_system.data = self.test_data
        self.file_system.save()
        with open(self.file_system.file_path, "rb") as file:
            data = pickle.load(file)
        self.assertEqual(data, self.test_data)
        
    def tearDown(self):
        """
        A method to delete the database file and its directory after running all tests.
        """
        try:
            os.remove(f'{self.test_path}/{self.test_name}.pkl')
            os.rmdir(self.test_path)
        except OSError as e:
            print("Error removing file/directory: ", e)

if __name__ == '__main__':
    unittest.main()
