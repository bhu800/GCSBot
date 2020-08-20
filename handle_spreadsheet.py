import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("GCSBot_Google_API_Credentials.json", scope)

client = gspread.authorize(creds)

sheet = client.open("GCSBot_Live_Data").sheet1  # Open the spreadhseet

# data = sheet.get_all_records()  # Get a list of all records
# sheet.append_row(["hello", "welcome"])
# pprint(data)

def appendDataInSpreadSheet(timestamp, user_data, bot_response):
    data = [timestamp, user_data, bot_response]
    sheet.append_row(data)