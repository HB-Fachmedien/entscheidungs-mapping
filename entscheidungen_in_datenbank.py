'''
Ein Skript, welches einen Ordner rekursiv nach Entscheidungen durchsucht und deren Metadaten in eine
sqlite Datenbank schreibt.

'''


import lxml.etree as et
import os
import sqlite3


# create the table
sqlite_file = './neu_prod_entscheidungs_db.sqlite'
con = sqlite3.connect(sqlite_file)
cur = con.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS EntscheidungsTabelle( docid TEXT PRIMARY KEY, title TEXT, instdocdate TEXT, alt_docid1 TEXT, alt_docid2 TEXT, alt_docid3 TEXT, alt_docid4 TEXT, alt_docid5 TEXT, extid TEXT, inst TEXT, instcode TEXT, instdocnote TEXT, instdoctype TEXT, instdocnr1 TEXT, instdocnr2 TEXT, instdocnr3 TEXT, instdocnr4 TEXT, instdocnr5 TEXT, instdocnr6 TEXT, instdocnr7 TEXT, instdocnr8 TEXT, instdocnr9 TEXT, instdocaddnrs TEXT, wird_gemappt INTEGER );''')
con.commit()


def read_xml_fill_db(data):
    
    e = et.parse(data)
    #print(str(e.getroot()))
    title = e.xpath('//metadata/title/text()')
    print(title)

    docid = e.xpath('/*/@docid')
    print(docid)

    alt_docids = e.xpath('/*/@altdocid')
    print(alt_docids)

    alt_docid1 = ''
    alt_docid2 = ''
    alt_docid3 = ''
    alt_docid4 = ''
    alt_docid5 = ''

    wird_gemappt = 0

    if alt_docids:

	    alt_docids_list = alt_docids[0].split(' ')
	    
	    alt_docid1 = alt_docids_list[0]

	    if len(alt_docids_list) >= 2:
	    	alt_docid2 = alt_docids_list[1]

	    if len(alt_docids_list) >= 3:
	    	alt_docid3 = alt_docids_list[2]

	    if len(alt_docids_list) >= 4:
	    	alt_docid4 = alt_docids_list[3]

	    if len(alt_docids_list) >= 5:
	    	alt_docid5 = alt_docids_list[4]


	    #falls eine altdocid enthalten ist, dann wird diese Entscheidung auf jeden Fall gemappt
	    wird_gemappt = 1

    extid = e.xpath('/*/@extid')
    print(extid)

    inst = e.xpath('/*/metadata/instdoc/inst/text()')
    print(inst)

    instdocdate = e.xpath('/*/metadata/instdoc/instdocdate/text()')
    print(instdocdate)

    instcode = e.xpath('/*/metadata/instdoc/inst/@code')
    print(instcode)

    instdocnote = e.xpath('/*/metadata/instdoc/instdocnote/text()')
    print(instdocnote)

    instdoctype = e.xpath('/*/metadata/instdoc/instdoctype/text()')
    print(instdoctype)

    instdocnrs = e.xpath('/*/metadata/instdoc/instdocnrs/instdocnr/text()')
    print(instdocnrs)


    instdocnr1 = ''
    instdocnr2 = ''
    instdocnr3 = ''
    instdocnr4 = ''
    instdocnr5 = ''
    instdocnr6 = ''
    instdocnr7 = ''
    instdocnr8 = ''
    instdocnr9 = ''

    if instdocnrs:
	    instdocnr1 = instdocnrs[0]

	    if len(instdocnrs) >= 2:
	    	instdocnr2 = instdocnrs[1]

	    if len(instdocnrs) >= 3:
	    	instdocnr3 = instdocnrs[2]

	    if len(instdocnrs) >= 4:
	    	instdocnr4 = instdocnrs[3]

	    if len(instdocnrs) >= 5:
	    	instdocnr5 = instdocnrs[4]

	    if len(instdocnrs) >= 6:
	    	instdocnr6 = instdocnrs[5]

	    if len(instdocnrs) >= 7:
	    	instdocnr7 = instdocnrs[6]

	    if len(instdocnrs) >= 8:
	    	instdocnr8 = instdocnrs[7]

	    if len(instdocnrs) >= 9:
	    	instdocnr9 = instdocnrs[8]


    instdocaddnrs = e.xpath('/*/metadata/instdoc/instdocaddnr/text()')
    print(instdocaddnrs)

    print('#'*20)
    print("alt_docid1 zum Debuggen:", alt_docid1)
    
    cur.execute("INSERT OR REPLACE INTO EntscheidungsTabelle VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ", ( ' '.join(docid), ' '.join(title), ' '.join(instdocdate), alt_docid1, alt_docid2, alt_docid3, alt_docid4, alt_docid5, ' '.join(extid), ' '.join(inst), ' '.join(instcode), ' '.join(instdocnote), ' '.join(instdoctype), instdocnr1, instdocnr2, instdocnr3, instdocnr4, instdocnr5, instdocnr6, instdocnr7, instdocnr8, instdocnr9, ' '.join(instdocaddnrs), wird_gemappt))
    con.commit()


def main():

    for subdir, dirs, files in os.walk("C:\\tempEntscheidungen"):
    #for subdir, dirs, files in os.walk(os.getcwd()):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".xml"):
                read_xml_fill_db(filepath)

    #con.close()

def closeDB():
	print("Datenbank ausgeben:")
	cur.execute("SELECT * FROM EntscheidungsTabelle LIMIT 5")
	all_rows = cur.fetchall()
	print('1):', all_rows)
	con.commit()
	print('DATENBANK WIRD GESCHLOSSEN.')
	con.close()


if __name__ == '__main__':
    main()
    closeDB()


