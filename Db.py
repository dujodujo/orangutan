import sqlite3
import sys

class Db(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execue_script(self, skript):
        sc = open(skript, 'r').read()
        return self.cursor.executescript(sc)

    def query(self, command):
        comm = '%s;' % command
        self.cursor.execute(comm)
        return self.cursor.fetchall()

    def execute(self, command):
        comm = '%s;' % command
        self.cursor.execute(comm)