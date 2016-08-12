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

        _pass = getpass.getpass("please enter password:- ") ##password wont be visible
        db = MySQLdb.connect(host = _host, user = _user,db =  _db, passwd = _pass )
        while True:
                cham = raw_input('''
                        please enter the command to be executed:- 
                        to drop a single table punch in 'drop table' and next prompt will ask for table name
                        to drop all tables punch in 'drop table all'
                        just punch in 'quit' to exit the activity:-
                        ''')
                if cham.lower() == "quit":
                        sys.exit()

                if cham.lower() == "drop table all":
                	cursor = db.cursor()
                	cursor.execute("show tables")
                	for i in cursor.fetchall():
                		try:
                			cursor.execute("drop table" + " " + (i[0]))
                		except:
                			cursor.execute("SET FOREIGN_KEY_CHECKS=0")
                			cursor.execute("drop table" + " " + (i[0]))
                			cursor.execute("SET FOREIGN_KEY_CHECKS=1")
                		print "all the tables has been deleted"
                elif cham.lower() == "drop table":
                        _ed = raw_input("please enter the table name:- ")
                        cursor = db.cursor()
                        try:
                                cursor.execute("drop table" + " " + _ed)
                        except:
                                cursor.execute("SET FOREIGN_KEY_CHECKS=0")
                                cursor.execute("drop table" + " " + _ed)
                                cursor.execute("SET FOREIGN_KEY_CHECKS=1")
                        print "Table " + _ed + " has been deleted"

                else:
                	cursor = db.cursor()
                	cursor.execute(cham)
                	print cursor.fetchall()





