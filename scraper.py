import urllib2
from BeautifulSoup import BeautifulSoup
import re

base_url = 'http://www.thewitchesinn.com/tarot/zoom.pl?value='


def query(ind):
	url = get_query_url(ind)
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)	
	m = soup.find('tr')
	m = m.findAll('td')
	money = m[1]
	
	card_name = get_card_name(money)
	card_desc = get_card_desc(money)
	
	return card_desc

def get_card_name(html):
	m = html.find('b')
	name = m.contents[0]
	name = name.split(r' ', 1)[1]
	return name

def get_card_desc(html):
	m = html.findAll('p')
	desc = []	
	for i in m:
		desc.append(i.contents[0])
	return desc

def get_query_url(ind):
	return base_url + str(ind)

i = 0
#while i < 78:
while i < 3:
	print(query(i))
	i+=1











