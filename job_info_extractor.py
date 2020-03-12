import json
import time
import re
import urllib.request
from urllib.parse import urlparse
from collections import namedtuple

from bs4 import BeautifulSoup


'''
	get_parse_params
	in: domain -> String
	out: Soup_Functors(Lambda, Lambda)?

	This function takes a domain and returns the functors for BeautifulSoup to use for parsing.

	If the domain is not supported, None is returned.
'''
def get_parse_params(domain):
	Soup_Functors = namedtuple('Soup_Functors', ['title', 'company'])

	# Load with functors for parsing known websites 
	sf = {}
	sf['jobs.lever.co'] = Soup_Functors(lambda x: x.find('h2').text, lambda x: x.find('div', class_='main-footer-text page-centered').p.a.text.split('Home Page')[0])

	return sf.get(domain, None)


def get_record(url):
	try:
		Soup_Functors = namedtuple('Soup_Functors', ['title', 'company'])

		domain = urlparse(url).netloc

		print(domain)

		content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(content, 'html.parser')

		sf = get_parse_params(domain)

		print(sf.title(soup) + '@' + sf.company(soup))

	except Exception as e:
		return "Woops, can't find that one.\n" +str(e)