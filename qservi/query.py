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
    q.query("SELECT dr.id, f.filter FROM deepCoadd_meas AS dm, deepCoadd_ref AS dr, filter as f WHERE dm.deepcoadd_measId=dr.deepcoadd_refId AND dm.filter_fkId=f.filterId AND f.filter='g';")
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

    def close(self):
        """Close the connection to the DB"""
        self.db.close()

    def dbinfo(self):
        print("INFO: Connected to")
        for key, val in self.db_info.items():
            print(' - %s: %s' % (key, val))

    def query(self, sqlquery, save=True, verbose=False):

        nrows = self.cursor.execute(sqlquery)
        if verbose:
            print("Current query is")
            print("  ", sqlquery)
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

    def get_all_tables(self, **kwargs):
        if self.tables is None:
            self.tables = self.query("SHOW TABLES", **kwargs)
        return self.tables

    def describe_table(self, table, **kwargs):
        self._check_table(table)
        return self.query("DESCRIBE %s" % table, **kwargs)

    def key_in_table(self, key, table):
        d = self.describe_table(table)
        return key in d['Field']

    def get_from_table(self, what, table, **kwargs):
        self._check_table(table)
        return self.query("SELECT %s from %s" % (what, table), **kwargs)


class QueryCatalogs(Query):

    def __init__(self, **kwargs):

        super(**kwargs).__init__()

    def complex_query(self):
        """TBF"""
        qq = {'deepCoadd_forced_src': {'and': ['modelfit_CModel_flux>0',
                                               'modelfit_CModel_flag=0'],
                                       'keys': ['modelfit_CModel_flux'],
                                       'or': []},
              'deepCoadd_meas': {'and': ['base_ClassificationExtendedness_flag=0',
                                         'base_ClassificationExtendedness_value>=0.5',
                                         'ext_shapeHSM_HsmShapeRegauss_flag=0',
                                         'detect_isPrimary=1'],
                                 'keys': ['ext_shapeHSM_HsmShapeRegauss_flag'],
                                 'or': []},
              'filter': {'keys': ['filter']}}
        what = ', '.join(['%s.%s' % (t, k) for t in qq for k in qq[t]['keys']])
        fromt = ', '.join(qq.keys())
        where_and = ' AND '
        where_and += ' AND '.join(['%s.%s' % (t, k) for t in qq if 'and' in qq[t] for k in qq[t]['and']])
        where_or = ' OR '.join(['%s.%s' % (t, k) for t in qq if 'or' in qq[t] for k in qq[t]['or']])
        

    def select_galaxies(self):
        """Apply a few quality filters on the data tables."""
        # == Get the initial number of filter
        filters = self.query("SELECT * FROM filter")
        nfilt = len(filters)

        # == Filter the deepCoadd catalogs

        query = "SELECT * from deepCoadd_meas as dm, deepCoadd_forced_src as dfs WHERE dm.deepCoadd_ref_fkId=dfs.deepCoadd_ref_fkId "
        # Select galaxies (and reject stars)
        # keep galaxy
        query += "AND dm.base_ClassificationExtendedness_flag=0 "
        #filt = cats['deepCoadd_meas']['base_ClassificationExtendedness_flag'] == 0

        # keep galaxy
        query += "AND dm.base_ClassificationExtendedness_value >= 0.5 "
        #filt &= cats['deepCoadd_meas']['base_ClassificationExtendedness_value'] >= 0.

        # Gauss regulerarization flag
        query += "AND dm.ext_shapeHSM_HsmShapeRegauss_flag=0 "
        #filt &= cats['deepCoadd_meas']['ext_shapeHSM_HsmShapeRegauss_flag'] == 0

        # Make sure to keep primary sources
        query += "AND dm.detect_isPrimary=1 "
        #filt &= cats['deepCoadd_meas']['detect_isPrimary'] == 1

        # Check the flux value, which must be > 0
        query += "AND dfs.modelfit_CModel_flux>0 "
        #filt &= cats['deepCoadd_forced_src']['modelfit_CModel_flux'] > 0

        # Select sources which have a proper flux value
        query += "AND dfs.modelfit_CModel_flag=0 "
        filt &= cats['deepCoadd_forced_src']['modelfit_CModel_flag'] == 0

        # Check the signal to noise (stn) value, which must be > 10
        query += "AND (dfs.modelfit_CModel_flux/dfs.modelfit_CModel_fluxSigma)>10 "
        #filt &= (cats['deepCoadd_forced_src']['modelfit_CModel_flux'] /
        #         cats['deepCoadd_forced_src']['modelfit_CModel_fluxSigma']) > 10

        return self.query(query)
 #
 ## == Only keeps sources with the 'nfilt' filters
 #dmg = cats['deepCoadd_meas'][filt].group_by('id')
 #dfg = cats['deepCoadd_forced_src'][filt].group_by(
 #    'id' if 'id' in cats['deepCoadd_forced_src'].keys() else 'objectId')
 #
 ## Indices difference is a quick way to get the lenght of each group
 #filt = (dmg.groups.indices[1:] - dmg.groups.indices[:-1]) == nfilt
 #
 #output = {'deepCoadd_meas': dmg.groups[filt],
 #          'deepCoadd_forced_src': dfg.groups[filt], 'wcs': cats['wcs']}
 #
 ## == Filter the forced_src catalog: only keep objects present in the other catalogs
 #if "forced_src" not in cats.keys():
 #    return output
 #
 #filt = np.where(np.in1d(cats['forced_src']['objectId'],
 #                        output['deepCoadd_meas']['id']))[0]
 #output['forced_src'] = cats['forced_src'][filt]
 #
 #return output
