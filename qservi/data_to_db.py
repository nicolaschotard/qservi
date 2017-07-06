"""Data manager for the qservi package."""

import sys

import yaml
import numpy as np
import math

import argparse
import random

import clusters.data
from clusters.data import Catalogs

from sqliteToolBox import *

import pprint

paramTypes_conversion = {'bool': 'boolean',
                         'float32': 'float',
                         'float64': 'double',
                         'int32': 'int(11)',
                         'int64': 'bigint(20)',
                         'string24': 'char(16)',
                         'string8': 'char(5)'}


def write_config(configfile="description.yaml"):
    config = {}
    config['tables'] = {'directors' :['deepCoadd_meas', 'deepCoadd_forced_src'],
                        'partitioned-tables': ['deepCoadd_meas', 'deepCoadd_forced_src']}
    config['extensions'] = {'data': '.csv',
                            'schema': '.sql'}
    yaml.dump(config, open(configfile, 'w'))


def write_catalog(path='testdata/output', catalog="deepCoadd_meas"):
    config = {'keys': {'deepCoadd_meas': ["coord*", "id",
                                          'base_ClassificationExtendedness_flag',
                                          'base_ClassificationExtendedness_value',
                                          'modelfit_CModel_flux*',
                                          'ext_shapeHSM_HsmShapeRegauss_flag',
                                          'detect_isPrimary']},
#              'patch': ['1,1', '1,3', '1,2', '1,4', '1,5'],
#              'patch': ['1,1', '1,3', '1,2'],
              'patch': ['1,1'],
              }

              
#    path = "/home/chotard/Work/scripts/analysis/test_Cluster/testdata/output/coadd_dir"
    path="/sps/lsst/data/clusters/MACSJ2243.3-0935/output_v1/coadd_dir"

    print "PATH : ",path

    data = Catalogs(path)

    print "Load catalog : ",path
    print "Load catalog - config: "
    print config
    pprint.pprint(config)

    data.load_catalogs(catalog,**config)

    print "\nINFO: Catalogs loaded"
    dm = data.catalogs[catalog]
    
    print "*** dm.keys() *******"
    print dm.keys()

    keyList=dm.keys()[:]
    keyList.sort()

    pprint.pprint(keyList)

    print dm["objectId"]
    print dm["parentObjectId"]

    print dm["tract"].info
    print len(dm["tract"])
    print len(dm["patch"])

    tract, patch = dm['tract'], dm['patch']

    if "," in tract[0]:
        print "*** Swap tract and patch ****"
        del dm['tract']
        del dm['patch']
        dm['patch'] = tract
        dm['tract'] = patch
    if 'id' in dm.keys():
        print "*** Modify id ****"
        dm['%sId' % catalog] = dm['id']
        del dm['id']
        print dm['%sId' % catalog]
    elif 'objectId' in dm.keys():
        print "*** Modify objectId ****"
        dm['%sId' % catalog] = dm['objectId']
        del dm['objectId']
    for k in dm.keys():
        if len(k) > 64:
            print k, "too long, %i character" % len(k)
            del dm[k]

    print "INFO: writing catalogs in %s.csv" % catalog

#    dm.write("%s.csv" % catalog, format='csv')
#    write_sqlfile(dm, catalog)
#    write_cfg(dm.keys(), catalog)

    # Create ptract/patch/filter table
    parameterTypes={}
    for k in dm.keys(): parameterTypes[k]=dm[k].info.dtype.name
    print parameterTypes

#    dataId_Tuple=('tract','patch','filter')
#    dataId_paramType=()
#    for v in dataId_Tuple: dataId_paramType = dataId_paramType+(parameterTypes[v],)
#   dataId_dbId=write_dataids_to_db(data.dataids, dataId_Tuple, dataId_paramType)

    
    if args.level==0:

        dataKeys=('tract',)
        bTableAlreadyExists=dbConnect.CheckIfTableExists('tract',True)
        if not bTableAlreadyExists:
            create_and_write_data_to_db("tract",dataKeys,dm, parameterTypes,catId="tract",dbId="id",unique=('tract'),autoincrement=True)
        else:
            bUpdate_tract=update_data_from_db("tract",dataKeys,dm, parameterTypes,catId="tract",dbId="id",unique=('tract'),autoincrement=True)
            
        dataKeys=('patch',)
        bTableAlreadyExists=dbConnect.CheckIfTableExists('patch',True)        
        if not bTableAlreadyExists:
            create_and_write_data_to_db("patch",dataKeys,dm,parameterTypes,catId="patch",dbId="id",unique=('patch'),autoincrement=True)
        else:
            bUpdatePatch=update_data_from_db("patch",dataKeys,dm, parameterTypes,catId="patch",dbId="id",unique=('patch'),autoincrement=True)
        
        dataKeys=('filter',)
        bTableAlreadyExists=dbConnect.CheckIfTableExists('filter',True)        
        if not bTableAlreadyExists:
            create_and_write_data_to_db("filter",dataKeys,dm,parameterTypes,catId="filter",dbId="id",unique=('filter'),autoincrement=True)
        else:
            bUpdateFilter=data_tract_dbId=update_data_from_db("filter",dataKeys,dm, parameterTypes,catId="filter",dbId="id",unique=('filter'),autoincrement=True)
        
        dataKeys=('deepCoadd_forced_srcId','x_Src','y_Src')
        bTableAlreadyExists=dbConnect.CheckIfTableExists('Reference',True)
        if not bTableAlreadyExists:
            create_and_write_data_to_db("reference",dataKeys,dm, parameterTypes,catId="deepCoadd_forced_srcId",dbId="id",unique=('deepCoadd_forced_srcId'),autoincrement=True)
        else:
            bUpdate_tract=update_data_from_db("reference",dataKeys,dm, parameterTypes,catId="deepCoadd_forced_srcId",dbId="id",unique=('deepCoadd_forced_srcId'),autoincrement=True)

        if not "--file" in sys.argv:
            dbConnect.DumpTable("tract")
            dbConnect.DumpTable("patch")
            dbConnect.DumpTable("filter")


    if args.level==1:

#        dependencies -> (catIdName,tableName, idName in table)
        idTag="%sId"%catalog
        dataKeys=dm.keys()
        data_tract_dbId=create_and_write_data_to_db(catalog,dataKeys,dm, parameterTypes,catId=idTag,dbId="id",
                                                    dependencies=[('tract','tract','tract'),
                                                                  ('filter','filter','filter'),
                                                                  ('patch','patch','patch'),
                                                                  ('deepCoadd_forced_srcId','reference','deepCoadd_forced_srcId')
                                                                  ]
                                                    )

    return 



def update_data_from_db(catalogName, dataTuple, dataDict, dataType, **kwargs):


    print "DB UPDATE : ",catalogName

    # Switch to non file dump mode
    dbConnect.UnSetFileName()

    # Read data already stored in Db
    dbKeys=dbConnect.GetParamListAndTypes(catalogName)
    dbDict=dbConnect.ReadDBcontentAsDict(catalogName,None)        

    print "DB CONTENT ",dbDict
    print dataDict[kwargs["catId"]]
    print dbDict[kwargs["catId"]]

## # reconstruire la suite de param
## # commenter le code

    # Check if db has to be updated
    bVewValue=False
    idCatTag=kwargs["catId"]
    dbTag=kwargs["dbId"]
    for v in dataDict[idCatTag]:
        if not v in dbDict[idCatTag]:
            print "Table ",catalogName," : value undefined in db ",v
            bNewValue=True


    # Switch back to initial mode
    dbConnect.ReSetFileName()

    return bNewValue


def create_and_write_data_to_db(catalogName, dataTuple, dataDict, dataType, **kwargs):

    print ""
    print "**** CATALOG : ",catalogName

    print kwargs

    bTableAlreadyExists=False
    if args.new:
        dbConnect.DropTable(catalogName)
    else:
        bTableAlreadyExists=dbConnect.CheckIfTableExists(catalogName)        

    print "DataTuple : ",dataTuple

    idCatTag=kwargs["catId"]
    print "Catalog identifier : ",idCatTag

    dbId=kwargs["dbId"]
    try:
        idIndex = dataTuple.index(dbId)
    except:
        idIndex=-1
    print "Identifer : ",dbId," ",idIndex
    print "Lg paramType : ",len(dataType),"  ",dataType[idCatTag]

    listId = dataDict[idCatTag][:]
    print len(listId)
    print len(set(listId))
    newList=tuple(set(listId))
    print newList

    # Primary key
    primKeyType="integer"
    if dbId in dataTuple: primKeyType=paramTypes_conversion[dataType[idCatTag]]

    propertyList=["PRIMARY KEY"]
    if kwargs.has_key("autoincrement") and kwargs["autoincrement"]: propertyList.append(" AUTOINCREMENT")
    paramSet=((dbId,primKeyType,propertyList),)

    print paramSet
    
    # Foreign key defined in tables listed in kwargs["dependencies"]]
    dependTable={}
    paramFkeyList=()
    if kwargs.has_key("dependencies"):

        dbConnect.UnSetFileName()

        for v in kwargs["dependencies"]:

            catParamId,tableName,tableId=v

            print "FOREIGN table ",catParamId," ",tableName," ",tableId

            tableKeys=dbConnect.GetParamListAndTypes(tableName)
            paramFkeyList=paramFkeyList+(catParamId,)

            dbParamName=tableKeys["dbParamName"]
            dbIdentifier=tableKeys["dbId"]
            idIndex=dbParamName.index(dbIdentifier)
            listName=dbParamName[:idIndex]+dbParamName[idIndex+1:]
            paramFkeyList=paramFkeyList+listName

            print "Foreign key parameters : ",paramFkeyList
            print tableKeys
            
            foreignKeyTag = "%s_fkId" % (tableName)
            foreignKeyDef = ["FOREIGN KEY %s(%s)" % (tableName, tableKeys["dbId"])]
#            paramSet=paramSet+(("bigint(20)",foreignKeyTag,foreignKeyDef),)
            paramSet=paramSet+(("int",foreignKeyTag,foreignKeyDef),)

        dbConnect.ReSetFileName()

    # Create data table parameter list
    #    remove id and foreign key params

    print "Date tuple : ",dataTuple
        
    paramToWrite=[]
    for i,v in enumerate(dataTuple):
        print "INSERT date tuple : ",i," ",v
        if i==idIndex:
            print "===> remove id ",v
            continue    # primary key
        if v in paramFkeyList:
            print "===> remove foreign key ",v
            continue   # foreign key

        propertyList=[]
        if kwargs.has_key("unique") and v in kwargs["unique"]: propertyList.append("UNIQUE")
        paramSet = paramSet +((v,paramTypes_conversion[dataType[v]],propertyList),)
        paramToWrite.append(v)

    print "dataTuple / paramToWrite ",len(dataTuple)," ",len(paramToWrite)
    print "paramSet / paramToWrite ",len(paramSet),"  / ",len(paramToWrite)

    dbKeys=dbConnect.CreateTable(catalogName,paramSet)
    dbConnect.DumpTable(catalogName)

    # Check case where values should be unique
    if len(dataTuple)==1 and kwargs.has_key("unique") and dataTuple[0] in kwargs["unique"]:
        vList=dataDict[dataTuple[0]][:]
        basicList=tuple(set(vList))
        print basicList
        reducedDataDict={}
        reducedDataDict[dataTuple[0]]=basicList

        write_data_to_db(catalogName,idCatTag,reducedDataDict,dataType,paramToWrite,dbKeys,**kwargs)
        return
    

    write_data_to_db(catalogName,idCatTag,dataDict,dataType,paramToWrite,dbKeys,**kwargs)           



def write_data_to_db(catalogName,idCatTag,dataDict,dataType,paramToWrite,dbKeys,**kwargs):        


    print "PARAM TO WRITE : ",paramToWrite

    bAutoIncrement=True
    if kwargs.has_key("autoincrement"): bAutoIncrement=kwargs["autoincrement"]

    nbEntries=len(dataDict[dataDict.keys()[0]])
    if nbEntries>100: nbEntries=100

    step=250
    firstElt=0
    lastElt=min(firstElt+step,nbEntries)
    

    # Foreign keys : collect data defined in tables linked through a foreign key

    print "*****************************************************"

    foreignDBDict={}
    if kwargs.has_key("dependencies"):
        dbConnect.UnSetFileName()
        for v in kwargs["dependencies"]:
            catParamId,tableName,tableId=v                
            dbDict=dbConnect.ReadDBcontentAsDict(tableName,None)        
            foreignDBDict[tableName]={}
            foreignDBDict[tableName].update(dbDict)
        dbConnect.ReSetFileName()
    
    # Loop over entries to add into DB

    bLastLoop = False
    while not bLastLoop:

        paramTupleList=[]
        for iRecord in range(firstElt,lastElt):

            # Primary key
            paramTuple=()
            if not bAutoIncrement: paramTuple=(dataDict[idCatTag][iRecord],)

            for p in paramToWrite:
                v=dataDict[p][iRecord]

                if dataType[p].startswith("float") or dataType[p].startswith("double"):
                    if math.isnan(v):
                        v=None
                if v==False :
#                    print "FALSE : ",dataType[p]
                    v=0
                elif v==True :
#                    print "TRUE : ",dataType[p]
                    v=1
                
                paramTuple=paramTuple+(v,)

#           Foreign keys
            if kwargs.has_key("dependencies"):
                for v in kwargs["dependencies"]:

                    catParamId,tableName,tableId=v
                    foreignKey=-1
                    for i,value in enumerate(foreignDBDict[tableName][tableId]):
                        if value==dataDict[catParamId][iRecord]: foreignKey=foreignDBDict[tableName]['id'][i]
                
                    if foreignKey>-1: paramTuple=paramTuple+(foreignKey,)
                    else :
                        print "No corresponding foreign key found for ",tableName," ",tableId,"=",dataDict[catParamId][iRecord]
                        sys.exit()

            paramTupleList.append(paramTuple)
    
        dbConnect.InsertTuples(dbKeys,paramTupleList,bAutoIncrement)

        firstElt=lastElt;
        lastElt=min(firstElt+step,nbEntries)
        if firstElt==nbEntries: bLastLoop=True
        
    return


def CheckTaskTable(tableName):

    bTableExists=dbConnect.CheckIfTableExists(tableName)

    if not bTableExists:

        paramSet=()

        paramSet=paramSet+(("id","integer",["PRIMARY KEY","AUTOINCREMENT"]),)
        paramSet=paramSet+(("taskId","integer",[]),)
        paramSet=paramSet+(("name","text",[]),)
        paramSet=paramSet+(("level","integer",[]),)
        paramSet=paramSet+(("user","char[50]",[]),)
        paramSet=paramSet+(("status","char[16]",[" CHECK(status in ('new','ready','done','running','failed')) DEFAULT 'new'"]),)

        print paramSet
        
        dbConnect.CreateTable(tableName,paramSet)

    return


def AddNewTask(taskId,dataName,catalogName):

    tableName="task"

    if args.new: dbConnect.DropTable(tableName)
    CheckTaskTable(tableName)
    dbKey=dbConnect.GetParamListAndTypes(tableName)
        
    paramTuple=((taskId,dataId+" "+catalogName,0,"SES",'new'))
    dbConnect.InsertTuples(dbKey,paramTuple)
    paramTuple=((taskId,dataId+" "+catalogName,1,"SES",'new'))
    dbConnect.InsertTuples(dbKey,paramTuple)

    dbConnect.DumpTable(tableName)


def UpdateTaskStatus(taskId,level,newStatus):

    request="UPDATE task SET status='%s' WHERE taskId=%s AND level=%d"%(newStatus,taskId,level)
    dbConnect.ExecuteRequest(request,(),True)
    return


def FinalizeNewTaskFile(taskId,level,newStatus):

    if not args.file: return
    request="UPDATE task SET status='%s' WHERE taskId=%s AND level=%d"%(newStatus,taskId,level)
    dbConnect.ExecuteRequest(request)
    return


def DumpTable():

    bTableExists=dbConnect.CheckIfTableExists(args.dump)
    if bTableExists:
        dbKey=dbConnect.GetParamListAndTypes(args.dump)
        print dbKey["dbParamType"]
        print dbKey["dbParamName"]
        dbConnect.DumpTable(args.dump)
    else:
        print "Table %s does not exist"%args.dump
    return

def DropTable():
    dbConnect.DropTable(args.drop)
    return

def clean_catalog(catalog="deepCoadd_meas"):
    f = open("%s.csv" % catalog)
    lines = [l.replace('nan', '\N').replace('True', '1').replace('False', '0') for l in f][1:]
    f.close()
    f = open("%s.csv" % catalog, 'w')
    for l in lines:
        f.write(l)
    f.close()


def write_sqlfile(cat, catalog="deepCoadd_meas"):
    
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

    f.write("PRIMARY KEY (`%sId`),\n" % catalog)
    f.write("KEY `IDX_tract_patch_filter` (`tract`,`patch`,`filter`)\n")
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
    cfg = {'id': '%sId' % catalog}
    cfg['part'] = {'pos': 'coord_ra_deg, coord_dec_deg',
                   'overlap': 0.0001,
                   'subChunks': 1}
    cfg['dirColName'] = "%sId" % catalog
    cfg['in.csv'] = {"field": keys}
    yaml.dump(cfg, open("%s.cfg" % catalog, 'w'))


def write_all(catalog):

    print "write_all(catalog) ",catalog

    write_catalog(catalog=catalog)
#    clean_catalog(catalog=catalog)


if __name__ == "__main__":

    print "Hello"

    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--level", type=int, choices=[0, 1, 2, 3],
                        help="DB level")
    parser.add_argument("--new",help="drop DB before update", action="store_true")
    parser.add_argument("--file",help="dump DB commands into command.sql file", action="store_true")
    parser.add_argument("--daemon",help="based on a python daemon interface", action="store_true")
    parser.add_argument("--dump", type=str,help="table name to be dumped")
    parser.add_argument("--drop", type=str,help="table name to be dumped")
    args = parser.parse_args()

    print args

    taskId=12654
    dataId="MACSJ2243.3-0935"
    catalogName="deepCoadd_forced_src"

    dbConnect=DBConnection("data/LSST.sql")    

    if args.dump:
        DumpTable()
        dbConnect.Close()
        sys.exit()

    if args.drop:
        DropTable()
        dbConnect.Close()
        sys.exit()

    if args.file: dbConnect.SetFileName("command_level%s_%d.sql"%(args.level,taskId))

    if args.level==None and args.daemon:
        AddNewTask(taskId,dataId,catalogName)

    if args.level!=None:
        write_all(catalogName)
        UpdateTaskStatus(taskId,args.level,"ready")
        if args.daemon and args.file: FinalizeNewTaskFile(taskId,args.level,"done")
        
    dbConnect.Close()


#    #write_all("forced_src")
#    write_config()



