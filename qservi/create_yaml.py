import yaml
d = {}

# all these tables will have to be cerated in this specific order

# director table
d['deepCoadd_ref'] = {'dependson': None,
                      'cat_id_key': 'id',
                      'primarykey': 'deepCoadd_refId',
                      'autoincrement': False}

# main tables
d['filter'] = {'dependson': None,
               'cat_id_key': 'filter',
               'primarykey': 'filterId',
               'autoincrement': True}
d['patch'] = {'dependson': None,
              'cat_id_key': 'patch',
              'primarykey': 'patchId',
              'autoincrement': True}
d['tract'] = {'dependson': None,
              'cat_id_key': 'tract',
              'primarykey': 'tractId',
              'autoincrement': True}


# dependencies for catalogs (parent, foreign_key)
# the 'cat_id_key' name of the parent table will be used to fill the new column 
dependencies = [['deepCoadd_ref', 'deepCoadd_ref_FK_id'],
                ['filter', 'filter_FK_id'],
                ['patch', 'patch_FK_id'],
                ['tract', 'tract_FK_id']]
d['deepCoadd_meas'] = {'dependson': dependencies,
                       'cat_id_key': 'id',
                       'primarykey': 'deepcoadd_measId',
                       'autoincrement': True}
d['deepCoadd_forced_src'] = {'dependson': dependencies,
                             'cat_id_key': 'id',
                             'primarykey': 'deepCoadd_forced_srcId',
                             'autoincrement': True}
d['forced_src'] = {'dependson': dependencies,
                   'cat_id_key': 'id',
                   'primarykey': 'forced_srcId',
                   'autoincrement': True}

print d
yaml.dump(d, open("DMStack-DataModel.yaml", 'w'))