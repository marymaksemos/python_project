import cobalt


def select(self, _table: str = 'DEFAULT'):
    """
    Sets the table variable.
    """
    if not (_table and _table.strip()):
        raise Exception('No table selected')

    cobalt.table = _table
