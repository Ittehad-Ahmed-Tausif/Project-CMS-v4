import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope of the application
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('path/to/your/credentials.json', scope)

# Authorize the clientsheet 
client = gspread.authorize(creds)

# Get the instance of the Spreadsheet
spreadsheet = client.open('Name of your Google Sheet')

# Get the first sheet of the Spreadsheet
sheet = spreadsheet.sheet1

# Read data from the sheet
data = sheet.get_all_records()
print(data)

# Write data to the sheet
sheet.update_cell(2, 2, 'Updated Value')  # Update cell B2 with 'Updated Value'