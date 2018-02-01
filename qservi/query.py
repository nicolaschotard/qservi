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

    def dbinfo(self):
        print("INFO: Connected to")
        for key, val in self.db_info.items():
            print(' - %s: %s' % (key, val))

    def query(self, sqlquery, save=True):

        print("Current query is")
        print("  ", sqlquery)
        nrows = self.cursor.execute("SELECT * from filter")
        print("INFO: %i rows found for this query" % nrows)

        columns_name = np.array(self.cursor.description)[:, 0]
        columns_value = np.array(self.cursor.fetchall())
        table = Table(columns_value, names=columns_name)

        if save:
            results = {"sqlquery": sqlquery, "output": table}
            self.results[len(self.results) + 1] = results

        return table
