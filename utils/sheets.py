import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your sheet
SHEET_NAME = "POC - Work Order Data Logging"
worksheet = client.open(SHEET_NAME).worksheet("Work Order Requests")

def log_work_order(data: dict):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = [
        timestamp,
        data["client_name"],
        data["project_name"],
        data["project_location"],
        data["site_contact"],
        data["site_contact_phone"],
        data["test_type"],
        data["task_description"],
        data["requested_time_date"],
        data["special_instructions"]
    ]
    worksheet.append_row(row)
    print("✅ Work order logged to Google Sheets.")

