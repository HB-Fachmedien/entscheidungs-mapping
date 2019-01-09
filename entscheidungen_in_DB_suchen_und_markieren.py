import os
import sqlite3

'''
Ein Python Skript, welches die Datenbank nach RSNummern absucht und bei Treffern dementsprechend markiert.

'''

datei = open('zitierte_rs_nummern.txt')
rs_nummern = datei.readlines()
#print("test")

sqlite_file = './neu_prod_entscheidungs_db.sqlite'
con = sqlite3.connect(sqlite_file)
cur = con.cursor()


for rs in rs_nummern:
	#print('"',rs.strip(),'"', sep='')
	#cur.execute("SELECT * FROM EntscheidungsTabelle WHERE docid = ? OR alt_docid1 = ? OR alt_docid2 = ? OR alt_docid3 = ? OR alt_docid4 = ? OR alt_docid5 = ?", (rs.rstrip(),rs.rstrip(),rs.rstrip(),rs.rstrip(),rs.rstrip(),rs.rstrip(),))
	cur.execute("SELECT * FROM EntscheidungsTabelle WHERE ? in (docid,alt_docid1,alt_docid2,alt_docid3,alt_docid4,alt_docid5)", (rs.rstrip(),))

	data=cur.fetchone()
	if data is None:
		print('Component %s not found '%(rs))

	cur.execute("UPDATE EntscheidungsTabelle SET wird_gemappt = 2 WHERE ? in (docid,alt_docid1,alt_docid2,alt_docid3,alt_docid4,alt_docid5)", (rs.rstrip(),) )
	

con.commit()
con.close()