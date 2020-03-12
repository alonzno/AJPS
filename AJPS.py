import sys
import job_info_extractor as jin
import google_sheets_writer as gsw

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1IP9n56iRPb5QprBr7CKYtplKMI-0wX4otLLyDLRoiNc' # ToDo Probably not a good way to define this
SAMPLE_RANGE_NAME = "'Sheet1'"

def main():

	if len(sys.argv) < 2:
		print("Provide the url.")
		exit()

	row = jin.get_record(sys.argv[1])
	gsw.write_row_to_spreadsheet(SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, row)



if __name__ == '__main__':
	main()


'''
Instructions for myself from myself

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