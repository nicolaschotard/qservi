"""Data manager for the qservi package."""

import sys

import yaml
import numpy as np
import math

from sqliteToolBox import *

import pickle
import pprint


def GetTasksReadyToBeProcessed():

    tableName="task"

    constraint ="WHERE status='ready'"
    dbDict=dbConnect.ReadDBcontentAsDict(tableName,constraint)

    return dbDict

def ProcessCommandFileName(fileName):

    f=open(fileName,"r")
    text=f.read()
    f.close()

    cmdList=[x for x in text.split("REQUEST") if x!=""]
    
    for l in cmdList:
        tmp=[x for x in l.split("NTUPLE") if x!=""]
        request=tmp[0]
        paramSet=()
        if len(tmp)>1:
            paramSet=pickle.loads(tmp[1])
            
        print "*****************************************************"
        print request," ",paramSet," ",type(paramSet)

        if len(paramSet)==0:
            dbConnect.ExecuteRequest(request)
        else:
            dbConnect.ExecuteManyRequest(request,paramSet)
    
if __name__ == "__main__":


    dbConnect=DBConnection("data/LSST.sql")    

    taskList=GetTasksReadyToBeProcessed()
    print taskList

    for i,t in enumerate(taskList['id']):

        print "TASK  id/level : ",taskList["taskId"][i]," ",taskList["level"][i]
        cmdFileName="command_level%s_%d.sql"%(taskList["level"][i],taskList["taskId"][i])
                     
        ProcessCommandFileName(cmdFileName)
        
    dbConnect.Close()




