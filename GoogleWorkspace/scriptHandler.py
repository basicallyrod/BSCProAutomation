from SpreadsheetDictionary import SCRIPT_FUNCTION, SCRIPT_ID

from oauth2client import file as oauth_file, client, tools

from googleapiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

def scriptExecute(script_id, recipient, clientInfo):
    # Set up the Apps Script API
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('script', 'v1', credentials=creds)

    # Call the Apps Script API
    request = {"function": script_id,
    "parameters": [
        recipient,
        clientInfo]
    }

    try:
        response = service.scripts().run(body=request, scriptId=SCRIPT_ID[0]).execute()

        if 'error' in response:
            # The API executed, but the script returned an error.

            # Extract the first (and only) set of error details. The values of
            # this object are the script's 'errorMessage' and 'errorType', and
            # an list of stack trace elements.
            error = response['error']['details'][0]
            print("Script error message: {0}".format(error['errorMessage']))

            if 'scriptStackTraceElements' in error:
                # There may not be a stacktrace if the script didn't start
                # executing.
                print("Script error stacktrace:")
                for trace in error['scriptStackTraceElements']:
                    print("\t{0}: {1}".format(trace['function'],
                        trace['lineNumber']))
        else:
            # The structure of the result depends upon what the Apps Script
            # function returns. Here, the function returns an Apps Script Object
            # with String keys and values, and so the result is treated as a
            # Python dictionary (folderSet).
            folderSet = response['response'].get('result', {})
            if not folderSet:
                print('No folders returned!')
            else:
                print('Folders under your root folder:')
                for (folderId, folder) in folderSet.items():
                    print("\t{0} ({1})".format(folder, folderId))

            

    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)

