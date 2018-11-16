'''
Ein Python Skript, welches unsere RWS Inhalte nach Vorkommen von RS Nummern durchsucht und diese ausgibt.
'''

# for Schleife dann entsprechenden Zeile in Datei schreiben

import lxml.etree as et
import os
import re

def readRsNumbers(data):
	e = et.parse(data)
	body_texts = e.xpath('/*/body//text()')

	rs_nummer_regex = re.compile(r'RS\d{7}')
	for text in body_texts:
		hits = rs_nummer_regex.findall(text)

		if hits:
			print("HITS:", hits)
			print('#'*20)



def traverseFiles():
	#for subdir, dirs, files in os.walk("C:\\tempAlleRWS_seit2015"):
	for subdir, dirs, files in os.walk("C:\\work\\entscheidungs-datenbank\\entscheidungen"):
	#for subdir, dirs, files in os.walk(os.getcwd()):
		for file in files:
			filepath = subdir + os.sep + file

			if filepath.endswith(".xml"):
				readRsNumbers(filepath)



if __name__ == '__main__':
	traverseFiles()
