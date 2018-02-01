"""
Some doc https://mysqlclient.readthedocs.io/index.html
"""


import MySQLdb
import numpy as np
from astropy.table import Table


class Query:
    """
    Simple class to connec to a DB and make queries. All returned queries are Astropy tables.

    Examples:

    import query
    q = query.Query() 
    tables = q.get_all_tables()  # `tables` will be an astropy table
    q.describe_table('filter')  
    d = q.get_from_table('*', 'filter')  # `d` will be an astropy table
    d = q.get_from_table('modelfit_CModel_mag', 'deepCoadd_meas')  # (what, from)
    d = q.query('SELECT * from deepCoadd_meas WHERE modelfit_CModel_mag < 24')
    d = q.query("SELECT * from deepCoadd_meas, filter WHERE filter_fkId=filter.filterId AND filter.filter='i';")
    d = q.query("SELECT * from deepCoadd_meas, patch WHERE patch_fkId=patch.patchId AND patch.patch='1,5';")

    """

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
        self.queries = {}
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
        result = Table(columns_value, names=columns_name)

        if save:
            query = {"sqlquery": sqlquery, "output": result}
            self.queries[len(self.queries) + 1] = query

        return result

    def _check_table(self, table):
        tables = self.get_all_tables()
        if table not in tables[tables.colnames[0]]:
            raise KeyError("%s in not in the available list of tables (see `get_all_tables`)")

    def get_all_tables(self):
        if self.tables is None:
            self.tables = self.query("SHOW TABLES")
        return self.tables

    def describe_table(self, table):
        self._check_table(table)
        return self.query("DESCRIBE %s" % table)

    def get_from_table(self, what, table):
        self._check_table(table)
        return self.query("SELECT %s from %s" % (what, table))


class QueryCatalogs(Query):
            
    def __init__(self, **kwargs):

        super(**kwargs).__init__()