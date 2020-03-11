import sys
import re
import os
import json
import time
import urllib.request

from bs4 import BeautifulSoup

'''
Make row for sheet
	Find which website -Regex?
		Handle different websites independently?
	Parse Website
		Get Company Name
		Get Job title
	Get Date
	Get URL

	return Record (Company, job title, Date, URL)

Write to Google Sheets
	Do OAuth
		Get key? Might have one already
	Write to spreadsheet
		Get spreadsheet id
			Make new sheet if need be
'''