# cobalt-database

A school group project

A very simple database library written in Python

Basic usage:

```python
from cobalt import Cobalt

cobalt = Cobalt(db_path='db', db_name='cobalt') # Init cobalt

cobalt.insert(dict) # Inserts data to table

cobalt.fetch(str, str) -> list # Retrieve data as list from keys (row, column)
```

Installation
 ``` 
To install the cobalt-database package, use the following pip command:
pip install -e git+https://github.com/Sm0rezDev/cobalt-database.git#egg=cobalt_database
 ```
