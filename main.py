
"""
WHAT IS ITHIS?

It's a python script which extracts data from a .tsv file (tab seperated values) given
by IMdB with general information about all their movies, and stores it into a local 
SQLite database. It currently cannot do queries, that's in the future.

WHERE TO GET THE DATA:

Follow the link under "Data Location" at this website:

https://www.imdb.com/interfaces/

then download the "title.basics.tsv.gz" file. This file is currently zipped up not as
a .zip file, but as a ,gz file, but can be unzipped similarly. 7zip or winrar should be
able to handle it. This datatable can be opened in notepad or excel, though it's probably
better handled in excel. Be warned, this thing is HUGE, and more programs aren't designed
to handle files this large.

HOW TO USE:

Put that title.basics.tsv file into the data/ folder, and run this script with the command:

python main.py

"""

import csv
import sqlite3
from sqlite3 import Error

#DB commands
DB_INSERT = 'INSERT INTO {} ({}) VALUES {}'

#For future use
MOVIE_GENERAL_FIELDS = "movie_id, title, year, runtime, cover_url"
PERSON_GENERAL_FIELDS = "person_id, name, headshot_url"
USER_MOVIES_FIELDS = "movie_id, retention, rating"

def create_connection(db_file):
	"""Create a database connection to a database that resides in memory
	If database does not exist, create a new one"""
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None

def create_title_basics_table(conn):
	try:
		c = conn.cursor()
		c.execute('''CREATE TABLE IF NOT EXISTS title_basics (
			tconst integer PRIMARY KEY,
			titleType text NOT NULL,
			primaryTitle text NOT NULL,
			originalTitle text NOT NULL,
			isAdult integer NOT NULL,
			startYear integer,
			endYear integer,
			runtimeMinutes integer,
			genres text
		)''')
	except Error as e:
		print(e)

def add_title_basic(conn, title_basic):
	sql = '''INSERT INTO title_basics(tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres)
				VALUES(?,?,?,?,?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, title_basic)
	return cur.lastrowid

def main():
	database = 'db/data.db'
	conn = create_connection(database) #Open a new 'connection' to the database
	create_title_basics_table(conn) #If table 'title_basics' doesn't exist, create it
	with open('data/title.basics.tsv', encoding='utf-8') as tsvfile: #Open up the IMdB data, read above on where to get this
		reader = csv.reader(tsvfile, delimiter='\t') #Create a 'reader' to read through each row
		i = 0
		print('Opened tsv file')
		for row in reader:
			i += 1
			if i is 1:
				continue #First row describes each column, and isn't data, skip it

			try:
				data = ( #Assemble the new row to be inserted into a tuple
					int(row[0][2:]),
					str(row[1]),
					str(row[2]),
					str(row[3]),
					int(row[4]),
					None if row[5] == '\\N' else int(row[5]),
					None if row[6] == '\\N' else int(row[6]),
					None if row[7] == '\\N' else int(row[7]),
					str(row[8])
				)
				add_title_basic(conn, data) #Ingest new row into database
				if i % 10000 is 0:
					print(i, " rows transferred")
			except Exception as e:
				print(e)
				print('Error occured at tconst=' + row[0])
				
	conn.commit() #Save changes to database

if __name__ == '__main__':
	main()
