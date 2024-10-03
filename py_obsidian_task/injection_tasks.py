import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks"]


def add_task_test(title, notes):
  """Shows basic usage of the Tasks API.
  Prints the title and ID of the first 10 task lists.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("tasks", "v1", credentials=creds)
    # create new task list
    # new_tasklist = {
    #     'title': 'Test py tasklists creation'
    #     # Puoi aggiungere altri campi opzionali come 'description'
    # }
    # results = service.tasklists().insert(body=new_tasklist).execute()

    # Create new task to add
    new_task = {
        'title': 'My first task created with python',
        'notes': 'These are the notes'
    }
    results = service.tasks().insert(body=new_task, tasklist='RWVZNDZzenI4bVN6X2JGcg').execute()

  except HttpError as err:
    print(err)
