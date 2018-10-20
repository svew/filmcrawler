
import bs4 as bs
import urllib.request.urlopen as urlopen

IMDB_URLS = {
	'TITLE':				'https://www.imdb.com/title/tt{:07}/',
	'TITLE_FULL_CREDITS':	'https://www.imdb.com/title/tt{:07}/fullcredits',
	'TITLE_RELEASE_INFO':	'https://www.imdb.com/title/tt{:07}/releaseinfo',
	'NAME':					'https://www.imdb.com/name/nm{:07}/',
}

def get_movie(movie_id):
	movie_id = int(str(movie_id).strip('tt'))
	page = urlopen(TITLE_URL.format(movie_id))
	soup = bs.BeautifulSoup(page, 'lxml')
	
