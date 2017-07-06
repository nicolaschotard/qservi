import sqlite3

import os
import sys
import datetime
import smtplib
import types
import pickle

import pandas as pd

class DBConnection:

    def __init__(self, dbName=":memory:"):

        print "DB name : ",dbName
        self.db=sqlite3.connect(dbName)
        self.cursor=self.db.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
        self.fileDump=False
        self.fileDumpSave=self.fileDump
        self.fileName=""
        
    def Close(self):
        print "-> close connection"
        self.db.close()

    def SetFileName(self, name):
        self.fileDump=True
        self.fileName=name
        f=open(self.fileName,"w")
        f.close()

    def UnSetFileName(self):
        self.fileDumpSave=self.fileDump
        self.fileDump=False

        print "UnSetFileName(self) ",self.fileDump," ",self.fileDumpSave
        

    def ReSetFileName(self):
        self.fileDump=self.fileDumpSave

        print "ReSetFileName(self) ",self.fileDump," ",self.fileDumpSave

    def ExecuteRequest(self,request,paramSet=(),noFileDump=False):

        request=request.strip()

        print "Execute request : ",request,"   dump ",self.fileDump
        
        if not noFileDump and self.fileDump:
            f=open(self.fileName,"a")
            f.write("REQUEST "+request)
            if len(paramSet)>0 :
                s=pickle.dumps(paramSet)
                f.write("NTUPLE"+s)
            f.close()
            return

        print request
        print paramSet
        self.cursor.execute(request,paramSet)
        self.db.commit()
        return 


    def ExecuteManyRequest(self,request,paramSet):

        request=request.strip()
        if self.fileDump:
            f=open(self.fileName,"a")
            f.write("REQUEST "+request)
            if len(paramSet)>0 :
                s=pickle.dumps(paramSet)
                f.write("NTUPLE"+s)
            f.close()
            return

        print "ExecuteManyRequest : ",request
        print paramSet
        self.cursor.executemany(request,paramSet)
        self.db.commit()
        return

    def ExecuteRequest2(self,sRequest,sValues):

        return


    def DropTable(self,tableName):

        request="DROP TABLE IF EXISTS "+tableName+";"
        self.ExecuteRequest(request)

        res=self.cursor.fetchall()


    def DumpTable(self,tableName):

        request="SELECT * FROM "+tableName
        self.ExecuteRequest(request)
        res=self.cursor.fetchall()
        print res


    def CheckIfTableExists(self,tableName,noFileDump=False):

        request="SELECT count(*) FROM sqlite_master WHERE type='table' AND name='%s';"%tableName
        self.ExecuteRequest(request,(),noFileDump)
        res=self.cursor.fetchall()
        return (res!=[] and res[0][0]!=0)


    def CreateTable(self,tableName,paramSet):

        request="CREATE TABLE IF NOT EXISTS "+tableName+"("
        
        paramList=[]
##        fTableKey=None
        foreignKeyList=[]
        primaryKey=""
        for s in paramSet:
            
            p_name,p_type,value=s
            newValue=""
            if type(value) is str: p_list=[value]
            else: p_list=value[:]

            tmp=[]
            iPrimaryKey=-1
            iForeignKey=-1

            for i,v in enumerate(p_list):
                v=v.strip()
                if v.lower().startswith("foreign"):
                    iForeignKey=i
                    newValue=" ".join(tmp)
                    foreignKeyList.append(" ".join([p_type,p_name,newValue]))
                    foreignKeyList.append("FOREIGN KEY(%s) REFERENCES %s" % (p_type, value[iForeignKey].split(" ")[-1]))
                elif v.lower().startswith("primary"):
                    iPrimaryKey=i
                    paramIdName=p_name
                tmp.append(v)

            if iForeignKey>-1:
                pass
            elif iPrimaryKey>-1:
                newValue=" ".join(tmp)
                primaryKey=" ".join([p_name,p_type,newValue])
            else:
                newValue=" ".join(tmp)
                paramList.append(" ".join([p_name,p_type,newValue]))

#            print "PARAMLIST ",paramList
#            print "KEYS ",foreignKeyList," ",primaryKey
#            print ""


        print "-----------------------------------------------"

        print len(foreignKeyList)," ",len(primaryKey)
        if len(primaryKey)>0: paramList.insert(0,primaryKey)
        if len(foreignKeyList)>0:
            for i in range(0,len(foreignKeyList),2):paramList.append(foreignKeyList[i])
            for i in range(1,len(foreignKeyList),2):paramList.append(foreignKeyList[i])
            
        request = request+",".join(paramList)+")"

        print "CREATE TABLE ",request

        self.ExecuteRequest(request)

        bTableExits=self.CheckIfTableExists(tableName)
        if not self.fileDump:
            dbKeyDict=self.GetParamListAndTypes(tableName)
#            print dbKeyDict
            return dbKeyDict

        # In case commands are only dumped
        #   dbKeys hase to be created manually
        dbKeyDict={}
        dbKeyDict["dbName"]=tableName
        dbKeyDict["dbId"]=paramIdName
        dbKeyDict["dbParamType"]=()
        dbKeyDict["dbParamName"]=()
        for v in paramList:
            if v.startswith("FOREIGN"): continue
            tmp=[x for x in v.split(" ") if x!=""]
            dbKeyDict["dbParamType"]=dbKeyDict["dbParamType"]+(tmp[1],)
            dbKeyDict["dbParamName"]=dbKeyDict["dbParamName"]+(tmp[0],)

        return dbKeyDict


    def GetParamListAndTypes(self, tableName):
        
        dbKeyDict={}
        bTableExists=self.CheckIfTableExists(tableName)
        print "GetParamListAndTypes ",tableName," : table exists ",bTableExists

        if not bTableExists: return dbKeyDict
        
        request="PRAGMA table_info('%s');"%tableName

#       Using Panda
#        table=pd.read_sql_query(request, self.db)

        self.cursor.execute(request)
        res=self.cursor.fetchall()

##         request="PRAGMA schema.index_list('%s');"%tableName
##         self.cursor.execute(request)
##         idxList=self.cursor.fetchall()

        paramName=[]
        paramType=[]
        paramName_noId=[]
        paramType_noId=[]
        paramIdName="none"
        for v in res:
            p_name,p_type = v[1],v[2]
            p_name=p_name.encode('ascii','ignore')
            p_type=p_type.encode('ascii','ignore')
            paramName.append(p_name)
            paramType.append(p_type)
            if v[-1]==1:
                paramIdName=p_name

        dbKeyDict["dbName"]=tableName
        dbKeyDict["dbId"]=paramIdName
        dbKeyDict["dbParamType"]=tuple(paramType_noId)
        dbKeyDict["dbParamName"]=tuple(paramName)

        return dbKeyDict


    def InsertList(self,dbKey,paramList):
        ''' Data given as a listD !!!! '''

        paramTuple = tuple(paramList)
        insertTuples(dbKey,paramTuple)
        return

    def BuildDDRequestKeys(self,dbKey,bAutoIncrement):

        dbKeyWord=dbKey["dbName"]+str(dbKey["dbParamName"])
        if bAutoIncrement :
            print dbKey["dbParamName"]," / ",dbKey["dbId"]
            idIndex=dbKey["dbParamName"].index(dbKey["dbId"])
            dbKeyWord=dbKey["dbName"]+str(dbKey["dbParamName"][:idIndex]+dbKey["dbParamName"][idIndex+1:])
        dbKeyWord=dbKeyWord.replace("'","")
        dbKeyWord=dbKeyWord.replace(",)",")")

        return dbKeyWord        

    def InsertTuples(self,dbKey,paramSet,idAutoIncrement=True):
        ''' Insert tuple or list of tuple into the DB'''

        dbKeyWord=self.BuildDDRequestKeys(dbKey,idAutoIncrement)
        
        if type(paramSet) is tuple :
            placeholders=["?"]*len(paramSet)        
            request='INSERT INTO %s VALUES (%s)' % (dbKeyWord,",".join(placeholders))
            self.ExecuteRequest(request,paramSet)
        else:
            placeholders=["?"]*len(paramSet[0])
            request='INSERT INTO %s VALUES (%s)' % (dbKeyWord,",".join(placeholders))
#            print request," ",paramSet," ",type(paramSet)

            print "MANYMANYMANY : ",request

            self.ExecuteManyRequest(request,paramSet)
        
        self.db.commit()

        return


    def ReadDBcontentAsDict(self,tableName,constraint,paramSet=()):

        paramSelect="*"
        paramId=0
        if len(paramSet)==0:
            dbKeys=self.GetParamListAndTypes(tableName)
            paramList=dbKeys["dbParamName"]
            paramSet=tuple(paramList)
        paramSelect=str(paramSet)[1:-1]
        paramSelect=paramSelect.replace("'","")
        
        request="SELECT %s FROM %s" % (paramSelect,tableName)
        if constraint!=None: request=request+" "+constraint
        print request
        self.cursor.execute(request)
        res=self.cursor.fetchall()
        print res

        d={}
        for v in paramSet: d[v]=[]

        for value in res:
            for i,v in enumerate(value):
                d[paramSet[i]].append(v)
        return d
        


if __name__=="__main__":

    dbConnect=DBConnection()
    
    dbConnect.Close()

