import os
import pickle
import database

directory = "/" # path to search on, need to change to test if it works fully, my list is empty(?)
dictionaries = []

for filename in os.listdir(directory):
    if filename.endswith('.py'): 
        with open(os.path.join(directory, filename)) as file: 
            data = pickle.load(file) 
        dictionaries.append(data) 

print(dictionaries) # Need to change so its saves to database
