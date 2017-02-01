"""Data manager for the qservi package."""

import yaml
import numpy
import h5py
import fitsio
from astropy.wcs import WCS, utils
from astropy.coordinates import SkyCoord, Angle
from astropy.table import Table, Column, vstack
from astropy.units import Quantity
from progressbar import Bar, ProgressBar, Percentage, ETA
from termcolor import colored

import gc
import warnings
warnings.filterwarnings("ignore")

try:
    from lsst.afw import image as afwimage
    from lsst.afw import table as afwtable
    import lsst.daf.persistence as dafPersist
except ImportError:
    print colored("WARNING: LSST stack is probably not installed", "yellow")

from clusters.data import Catalogs


def write_config(configfile="description.yaml"):
    config = {}
    config['tables'] = {'directors' :['deepCoadd_meas'],
                        'partitioned-tables': ['deepCoadd_meas']}
    config['extensions'] = {'data': '.csv',
                            'schema': '.sql'}
    yaml.dump(config, open(configfile, 'w'))

    
def write_catalog(path='testdata/output', catalog="deepCoadd_meas"):
    config = {'keys': {'deepCoadd_meas': ["coord*", "id",
                                          'base_ClassificationExtendedness_flag',
                                          'base_ClassificationExtendedness_value',
                                          'modelfit_CModel_flux*',
                                          'ext_shapeHSM_HsmShapeRegauss_flag',
                                          'detect_isPrimary']}}
    path = "/home/chotard/Work/scripts/analysis/test_Cluster/testdata/output/coadd_dir"
    data = Catalogs(path)
    data.load_catalogs(catalog, **config)
    print "\nINFO: Catalogs loaded"
    dm  = data.catalogs[catalog][:500]
    del dm['tract']
    del dm['patch']
    print "INFO: writing catalogs in %s.csv" % catalog
    dm.write("%s.csv" % catalog, format='csv')
    write_sqlfile(dm, catalog)
    write_cfg(dm.keys())
    return data

    
def clean_catalog(catalog="deepCoadd_meas"):
    f = open("%s.csv" % catalog)
    lines = [l.replace('nan', '\N').replace('True', '1').replace('False', '0') for l in f][1:]
    f.close()
    f = open("%s.csv" % catalog, 'w')
    for l in lines:
        f.write(l)
    f.close()


def write_sqlfile(cat, catalog="deepCoadd_meas"):
    types = {'bool': 'boolean',
             'float32': 'double',
             'float64': 'double',
             'int32': 'bigint(20)',
             'int64': 'bigint(20)',
             'string24': 'char(5)',
             'string8': 'char(5)'}
    print "INFO: writing sql info in %s.sql" % catalog
    f = open("%s.sql" % catalog, 'w')
    f.write("/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;\n")
    f.write("/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;\n")
    f.write("/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;\n")
    f.write("/*!40101 SET NAMES utf8 */;\n")
    f.write("/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;\n")
    f.write("/*!40103 SET TIME_ZONE='+00:00' */;\n")
    f.write("/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='' */;\n")
    f.write("/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;\n")
    f.write("DROP TABLE IF EXISTS `%s`;\n" % catalog)
    f.write("/*!40101 SET @saved_cs_client     = @@character_set_client */;\n")
    f.write("/*!40101 SET character_set_client = utf8 */;\n")
    f.write("CREATE TABLE `%s` (\n" % catalog)
    for k in cat.keys():
        f.write("`%s` %s NULL,\n" % (k, types[cat[k].info.dtype.name]))
    f.write("PRIMARY KEY (`id`),\n")
    #f.write("KEY `IDX_tract_patch_filter` (`tract`,`patch`,`filter`)\n")
    f.write("KEY `IDX_filter` (`filter`)\n")
    f.write(") ENGINE=MyISAM DEFAULT CHARSET=latin1;\n")
    f.write("/*!40101 SET character_set_client = @saved_cs_client */;\n")
    f.write("/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;\n")
    f.write("/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;\n")
    f.write("/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;\n")
    f.write("/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;\n")
    f.write("/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;\n")
    f.close()
    return sorted(cat.keys())

def write_cfg(keys, catalog='deepCoadd_meas'):
    print "INFO: Writing configurations in %s.cfg" % catalog
    cfg = {'id': 'id'}
    cfg['part'] = {'pos': 'coord_ra_deg, coord_dec_deg',
                   'overlap': 0.0001,
                   'subChunks': 1}
    cfg['dirColName'] = "id"
    cfg['in.csv'] = { "field": keys}
    yaml.dump(cfg, open("%s.cfg" % catalog, 'w'))

def write_all():
    write_catalog()
    clean_catalog()
    write_config()
    
if __name__ == "__main__":

    write_all()