import json
import time
import re
import urllib.request
from urllib.parse import urlparse

from bs4 import BeautifulSoup

def get_parse_params(domain):
	print(host)
	pass


def get_record(url):
	try:
		domain = urlparse(url).netloc
		print(domain)
		exit()

		content = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(content, 'html.parser')



        # lyrics = str(soup)
        # # lyrics lies between up_partition and down_partition
        # up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        # down_partition = '<!-- MxM banner -->'
        # lyrics = lyrics.split(up_partition)[1]
        # lyrics = lyrics.split(down_partition)[0]
        # lyrics = lyrics.replace('<br>','') \
        #     .replace('</br>','') \
        #     .replace('<br/>', '') \
        #     .replace('<i>', '') \
        #     .replace('</i>', '') \
        #     .replace('</div>','').strip()
        # return lyrics
	except Exception as e:
		return "Woops, can't find that one.\n" +str(e)