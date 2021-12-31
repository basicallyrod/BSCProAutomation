from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def sheet_data(spreadsheet_id, range_id):
        #SCOPES = ['https://www.googleapis.com/auth/sqlservice.admin']
        SERVICE_ACCOUNT_FILE = 'gkeys.json'

        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        creds = None
        creds = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)

        # def main():
        #     """Shows basic usage of the Sheets API.
        #     Prints values from a sample spreadsheet.
        #     """

        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                range=range_id).execute()
        values = result.get('values', [])

        #print(values[:])
        return values



# if __name__ == '__main__':
#     gspread_quickstart()
