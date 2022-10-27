#!/usr/bin/env python
# (c)2015 John Strickler

# only one connection and one cursor will be created

import sqlite3

class DatabaseConnection(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super.__new__(cls)
        return cls.instance

    def __init__(self):
        # IMPORTANT! One-time setup
        self._db_connection = sqlite3.connect(':memory:')
        self._db_cursor = self._db_connection.cursor()

    @property
    def cursor(self):
        return self._db_cursor

