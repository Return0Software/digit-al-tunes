import os
import sqlite3

import sys
sys.path.append(sys.path[0] + "/..")
# from .. import Constants
from Constants import DATABASE_NAME


class SQLiteConnection():
    """Provides an easy to use connection to an SQLite instance"""

    __connection = None
    __cursor = None

    def __init__(self):
        self.__connection = sqlite3.connect(DATABASE_NAME)
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute(
            """SELECT name from sqlite_master WHERE type='table' AND name='Configuration'""")
        if self.__cursor.fetchone() is None:
            print("Create db")
    # def get_table_data
