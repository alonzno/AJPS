import json
from datetime import datetime, date
import re
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from collections import namedtuple

from bs4 import BeautifulSoup

class SiteNotSupportedException(Exception):
	''' Use this for domains that you have not already written parsing rules for'''
	pass


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
	sf['jobs.lever.co'] = 		 Soup_Functors(lambda x: x.find('h2').text.strip(), 
											   lambda x: x.find('div', class_='main-footer-text page-centered').p.a.text.split('Home Page')[0].strip())
	sf['boards.greenhouse.io'] = Soup_Functors(lambda x: x.find('h1', class_='app-title').text.strip(),
											   lambda x: x.find('span', class_='company-name').text.split('at ')[1].strip())
	sf['jobs.jobvite.com'] = 	 Soup_Functors(lambda x: x.find('h2', class_='jv-header').text.strip(),
											   lambda x: x.find('title').text.split(' - ')[0].strip())
	sf['www.glassdoor.com'] = 	 Soup_Functors(lambda x: x.find('h2', class_='mt-0 margBotXs strong').text.strip(),
											   lambda x: x.find('span', class_='strong ib').text.strip())

	return sf.get(domain, None)

'''
	get_record
	in: url -> String
	out: Str

	This function takes the url for a job posting and returns the JSON encoding that might
	be used for adding to a spreadsheet.
'''
def get_record(url):

	domain = urlparse(url).netloc

	try:
		Soup_Functors = namedtuple('Soup_Functors', ['title', 'company'])

		headers = {'User-Agent': 'Safari/537.3'}
		req = Request(url=url, headers=headers) 

		content = urlopen(req).read()
		soup = BeautifulSoup(content, 'html.parser')

		sf = get_parse_params(domain)

		if not sf:
			raise SiteNotSupportedException

		#ToDo Maybe add different date options
		dt = datetime.now().date()
		date = str(dt.month) + '/' + str(dt.day) + '/' + str(dt.year)

		job_title = sf.title(soup)
		company = sf.company(soup)

		ret_json = json.dumps({'title': job_title,
							  'company': company,
							  'date': date,
							  'url':url})
		return ret_json

		
	except SiteNotSupportedException as e:
		print('Parsing rules have not been written for the domain: ' + domain)
		print('Please take a moment to write the rules and then try again')
		exit(3)
	except Exception as e:
		print(e)
		return "Woops, can't find that one.\n" +str(e)