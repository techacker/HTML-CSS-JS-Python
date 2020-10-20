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
SAMPLE_SPREADSHEET_ID = 'enterKEY'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

# Get method to read the spreadsheet
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="Sheet1!A1:C29").execute()

values = result.get('values', [])

data = [["Anurag", 4/1/1978],["Shipra", 6/26/1978],["Aashka", 8/7/2006],]

# Update method to write to spreadsheet
request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                            range="Sheet2!A1", valueInputOption="USER_ENTERED", body={"values":data})
response = request.execute()

print(response)

