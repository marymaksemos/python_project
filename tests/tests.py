import os
import unittest
from src.cobalt import Cobalt


"""
Test Data
"""
test_database = {
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


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.cobalt = Cobalt(db_path='db', db_name='cobalt_test')
        self.cobalt.data.update(test_database)
        #self.cobalt.select()

    # def test_pickle_file_exist(self):
    #     """
    #     [Database file created]:
    #     """
    #     path = self.path
    #     name = self.name
    #     file_path = f'{path}/{name}_db.pkl'

    #     self.assertTrue(os.path.exists(file_path))

    def test_insert(self):
        """
        [Insert new data]:
        """
        data = {'name': 'Saeed',
                'email': 'saeed.sadeghighahroodi@chasacademy.se',
                'role': 'Developer'}
        self.cobalt.insert(data)

    def test_fetch_Wildcard(self):
        """
        [Fetch everything from table]:
        """
        fetch = self.cobalt.fetch

        result = fetch('', '')
        expected = test_database['DEFAULT']

        self.assertEqual(result, expected)

    def test_fetch_item_by_id(self):
        """
        [Fetch item by id]:
        """
        fetch = self.cobalt.fetch
        result = fetch(1, '')
        expected = [{
            'id': 1,
            'name': 'Simon',
            'email': 'simon.wei@chasacademy.se',
            'role': 'Developer'
        }]

        self.assertEqual(result, expected)

    def test_fetch_item_by_value(self):
        """
        [Fetch item by Value]:
        """

        fetch = self.cobalt.fetch
        result = fetch('', 'name')
        expected = [val['name'] for val in test_database['DEFAULT']]

        self.assertEqual(result, expected)

    def tearDown(self):
        self.cobalt.data.clear()
        fs = self.cobalt.fs
        if fs.file_path.endswith('_test.pkl'):
            os.remove(fs.file_path)
        if os.path.exists("db"):
           os.rmdir("db")

if __name__ == '__main__':

    cobalt = Cobalt('db', 'test')
    cobalt.data = test_database

    for i in cobalt.fetch('1', ''):
        print(i)
