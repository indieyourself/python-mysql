#!/usr/bin/python

import MySQLdb
import sys

if len(sys.argv) != 4:
        print "please enter the Hostname to connect followed by:"
        print "mysql username;"
        print "mysql db to connect;"
else:
        _host = sys.argv[1]
        _user = sys.argv[2]
#       _pass = sys.argv[3]
        _db   = sys.argv[3]
        cham = raw_input("please enter the command to be executed:- ")
        _pass = raw_input("please enter password:- ")

        if cham == "drop table":
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
        else:
        	db = MySQLdb.connect(host = _host, user = _user,db =  _db, passwd = _pass )
        	cursor = db.cursor()
        	cursor.execute(cham)
        	print cursor.fetchall()
        	db.close()




'''
import MySQLdb


if len(sys.argv) != 4:
	print "please enter the Hostname to connect followed by:"
	print "mysql username;"
	print "mysql db to connect;"
else:
	_host = sys.argv[1]
	_user = sys.argv[2]
#	_pass = sys.argv[3]
	_db   = sys.argv[3]
	cham = raw_input("please enter the command to be executed:- ")

db = MySQLdb.connect("_host, _user, _db")

cursor = db.cursor()

cursor.execute("show tables")
print cursor.fetchall()

db.close()
'''


'''
import sys 
import subprocess
import shlex

#print sys.argv[1]

if len(sys.argv) != 4:
	print "please enter the Hostname to connect followed by:"
	print "mysql username;"
	print "mysql db to connect;"
else:
	_host = sys.argv[1]
	_user = sys.argv[2]
#	_pass = sys.argv[3]
	_db   = sys.argv[3]
	cham = raw_input("please enter the command to be executed:- ")
	#_comm = sys.argv[5]
	#a = "mysql -h" + str(_host) + " -u" + str(_user) + " -p" + str(_pass) + " " + str(_db)
	a = "mysql -h" + str(_host) + " -u" + str(_user) + " " + str(_db)+ " -p"
	b = shlex.split(a)
	c = subprocess.Popen(b,shell=False, stdin=subprocess.PIPE)
	c.communicate(cham)
'''



