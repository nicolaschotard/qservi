"""
Some doc https://mysqlclient.readthedocs.io/index.html
"""


import MySQLdb
import numpy as np
from astropy.table import Table


class Query:

    def __init__(self, user="qsmaster", host="172.18.0.2", port=4040, db="qservTest_case98_qserv"):

        # Connect to the data base
        self.db = MySQLdb.connect(user=user, host=host, port=port, db=db)
        self.db_info = {'user': user,
                        'host': host,
                        'port': port,
                        'db': db}
        self.dbinfo()

        # Create a new cursor
        self.cursor = self.db.cursor()

        # Create an empty dictionary where all restuls will be saved
        self.results = {}
        self.tables = None

    def dbinfo(self):
        print("INFO: Connected to")
        for key, val in self.db_info.items():
            print(' - %s: %s' % (key, val))

    def query(self, sqlquery, save=True):

        print("Current query is")
        print("  ", sqlquery)
        nrows = self.cursor.execute(sqlquery)
        print("INFO: %i rows found for this query" % nrows)

        columns_name = np.array(self.cursor.description)[:, 0]
        columns_value = np.array(self.cursor.fetchall())
        table = Table(columns_value, names=columns_name)

        if save:
            results = {"sqlquery": sqlquery, "output": table}
            self.results[len(self.results) + 1] = results

        return table

    def _check_table(self, table):
        tables = self.get_all_tables()
        if table not in tables[tables.colnames[0]]:
            raise KeyError("%s in not in the available list of tables (see `get_all_tables`)")

    def get_all_tables(self):
        if self.tables in None:
            self.tables = self.query("SHOW TABLES")
        return self.tables

    def describe_table(self, table):
        self._check_table(table)
        return self.query("DESCRIBE %s" % table)

    def get_from_table(self, what, table):
        self._check_table(table)
        return self.query("SELECT %s from %s" % (what, table))