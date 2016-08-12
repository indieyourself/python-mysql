#!/usr/bin/python

import MySQLdb
import sys
import getpass

if len(sys.argv) != 4:
        print "please enter the Hostname to connect followed by:"
        print "mysql username;"
        print "mysql db to connect;"
else:
        _host = sys.argv[1]
        _user = sys.argv[2]
        _db   = sys.argv[3]
        while True:
                cham = raw_input('''
                                please enter the command to be executed:- 
                                just punch in 'quit' to exit the activity:-
                                ''')
        #        _pass = raw_input("please enter password:- ")
                

                if cham == "drop table":
                        _pass = getpass.getpass("please enter password:- ") ##password wont be visible
                	db = MySQLdb.connect(host = _host, user = _user,db =  _db, passwd = _pass )
                	cursor = db.cursor()
                	cursor.execute("show tables")
                	for i in cursor.fetchall():
                		try:
                			cursor.execute("drop table" + " " + (i[0]))
                			#print cursor.fetchall()
                		except:
                			cursor.execute("SET FOREIGN_KEY_CHECKS=0")
                			cursor.execute("drop table" + " " + (i[0]))
                			cursor.execute("SET FOREIGN_KEY_CHECKS=1")
        #        		print "all the tables has been deleted"
                	db.close()
                elif cham.lower()  == "quit":
                        sys.exit()
                else:
                        _pass = getpass.getpass("please enter password:- ") ##password wont be visible
                	db = MySQLdb.connect(host = _host, user = _user,db =  _db, passwd = _pass )
                	cursor = db.cursor()
                	cursor.execute(cham)
                	print cursor.fetchall()
                	db.close()





