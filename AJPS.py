import sys
import job_info_extractor as jin

def main():

	if len(sys.argv) < 2:
		print("Provide the url.")
		exit()

	print(jin.get_record(sys.argv[1]))


if __name__ == '__main__':
	main()


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