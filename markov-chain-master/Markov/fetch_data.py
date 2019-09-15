import ssl
import urllib2
from bs4 import BeautifulSoup
context = ssl._create_unverified_context()

def get_data():
	site = raw_input('Enter lyric url here(azlyrics only): ')
	page = urllib2.urlopen(site, context=context)
	html_doc = page.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	a = soup.find_all('div')
	for div in a:
		if div.has_attr('class') == False and div.has_attr('id') == False:
			return div.get_text().encode('UTF-8')
