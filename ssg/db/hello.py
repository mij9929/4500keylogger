import sqlite3, os




con =sqlite3.connect('./db.sqlite3')







with open('dump.sql','w') as f:
	for line in con.iterdump():
		f.write('%s\n' %line)
