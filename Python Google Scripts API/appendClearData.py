#from __future__ import print_function
#import pickle
import os.path
from googleapiclient.discovery import build
#from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1k2eHtnq9Va3VZnTkIsrQKZLVrd-LcZ4mKnF9HLfD6V4'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

data = [["Anurag", "Bansal", 1978], ["Shipra", "Bansal", 1978], ["Aashka", "Bansal", 2006]]

'''
# Clear the content from given range
request = sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Sheet1!A1:C")
response = request.execute()
'''

# Append data
request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                                range="Sheet1!A1:C1", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":data})
response = request.execute()


print(response)

