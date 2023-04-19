import os
import sys
import pickle


class FileSystem:
    """
    A class for saving  python objects to and from a file on disk.
    The objects are saved and accessed via a key (of type str).
    """
    def __init__(self, path: str, name: str):
        """
        User story #2
        Initialize the database by loading the data from the file,
        If the file does not exist, attempt to create one and initialize it.
        :paramter path: The directory of the database.
        :parameter name: Name of the data file.

        **I want to retrieve python dictionaries previously stored to disk
        with your library**
        """
        if not all((path and path.strip(), name and name.strip())):
            sys.exit('No database filepath defined.')

        self.data = {'DEFAULT': []}
        self.file_path = f'{path}/{name}.pkl'

        try:
            # Tries to read if file exist
            with open(self.file_path, "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            # If file doesnt exist, attempt to create one and initialize it
            # with empty dictionary.
            # Creates following directory if it doesn't already exist.

            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, "wb") as file:
                pickle.dump(self.data, file)
        except EnvironmentError:
            sys.exit('Opps.. something went wrong trying Read from disk.')

    # Write to disk
    def save(self):
        """
        User story #1
        Writes contents from *data* dict to file.

        (Same meaning as in Story #1)
        **I want to save python dictionaries to disk so that my applications
        can save their state for later use**
        """
        try:
            with open(self.file_path, "wb") as file:
                pickle.dump(self.data, file)
        except EnvironmentError:
            sys.exit('Opps.. something went wrong trying Write to disk.')
