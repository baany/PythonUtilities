#!/usr/bin/env python3

import json
import os
import string
import cx_Oracle

userCred = 'XXXX'
passwordCred = 'XXXX'
dbHostname = 'XXXX'
portNumber = 'XXXX'
nameofDB = 'XXXX'

def oracleDataPush(dataDict):
    name = dataDict['name']
    description = dataDict['description']
    startTime = dataDict['startTime']
    duration = dataDict['duration']
    ##########################################
    con = cx_Oracle.connect(userCred, passwordCred, cx_Oracle.makedsn(dbHostname, portNumber, nameofDB))
    try : 
        cur = con.cursor()
        statement = 'insert into TABLENAME (NAME, DESCRIPTION, STARTTIME, DURATION) values (:2, :3, :4, :5)'
        ## starts from 2 as 1 has been assigned to auto-incremented ID value
        cur.execute(statement, (name, description, startTime, duration))
        con.commit()
        print ({"result":[{"mssg":"Done Successfully"}]})
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print ({"result":[{"mssg":str(error.code),"error":1}]})
    con.close()
    return ()

oracleDataPush({'name':'ABCD','description':'PushDataIntoDB','startTime':'09:30:00','duration':'00:10:00'})
