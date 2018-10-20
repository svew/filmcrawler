
import pymysql

# DB commands
DB_INSERT = "INSERT INTO {} ({}) VALUES {}"

MOVIE_GENERAL_FIELDS = "movie_id, title, year, runtime, cover_url"
PERSON_GENERAL_FIELDS = "person_id, name, headshot_url"
USER_MOVIES_FIELDS = "movie_id, retention, rating"


class DBManager(object):

	INSERT_COMMAND = 'INSERT INTO {} ({}) VALUES {}'

	DB_HOST = 'localhost'
	DB_USER = 'root'
	DB_PASSWORD = 'GottaGetThatThingFixed'
	DB_NAME = 'film_crawler_db'

	def __init__(self):
		self.db = pymysql.connect(
				self.DB_HOST,
				self.DB_USER,
				self.DB_PASSWORD,
				self.DB_NAME)
		self.db_cursor = self.db.cursor()

	def __del__(self):
		self.db.close()

	def insert(self, table, fields, values):
		command = self.INSERT_COMMAND.format(table, fields, values)
		self.db_cursor.execute(command)

	def select(self, table):
		pass


class FilmCrawlerDB(object):
	def __init__(self, manager):
		self.manager = manager

	def get_cast(self, movie_id):
		pass

	def get_movie(self, movie_id):
		pass

	def get_person(self, person_id):
		pass


class Movie:
	def __init__(self, movie_id, title, release_year, synopsis="", poster_url="", rating_imdb=None,
														watched=None, want_to_see=None):
		self.id = movie_id
		self.title = title
		self.release_year = release_year
		self.synopsis = synopsis
		self.poster_url = poster_url
		self.rating_imdb = rating_imdb
		self.watched = watched
		self.want_to_see = want_to_see


class MoviePersonEdge:
	def __init__(self, movie_id, person_id):
		self.movie_id = movie_id
		self.person_id = person_id
		self.data = {}


class Person:
	def __init__(self, person_id, name, portrait_url=None):
		self.id = person_id
		self.name = name
		self.portrait_url = portrait_url

