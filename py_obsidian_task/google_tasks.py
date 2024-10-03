import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks.readonly"]


def google_tasks():
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

    # Call the Tasks API
    results = service.tasklists().list().execute()
    items = results.get("items", [])

    if not items:
      print("No task lists found.")
      return

    all_tasks = []
    print("Task lists:")
    for tasklist in items:
        tasks = service.tasks().list(tasklist=tasklist['id']).execute()
        all_tasks.extend(tasks.get('items', []))

    return all_tasks

  except HttpError as err:
    print(err)
