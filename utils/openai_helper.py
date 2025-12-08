import openai

# Set your OpenAI API key here
openai.api_key = "sk-abc123youractualkey"

# OpenAI helper functions placeholder import gspread
from google.oauth2.service_account import Credentials

# Define the required scopes
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate using the JSON key
creds = Credentials.from_service_account_file(
    "C:/Users/faiz malik/Downloads/my-project-46822-468217-073a81ec7ab7.json",
    scopes=SCOPES
)

# Authorize with gspread
client = gspread.authorize(creds)

# Open a spreadsheet by name (must be shared with the service account)
sheet = client.open("Your Sheet Name").sheet1

# Example: Read all rows
rows = sheet.get_all_records()
print(rows)

# Example: Write to a cell
sheet.update'A1', 'Hello from Cerebro!') import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# === 1. Authenticate ===
SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_file(
    "C:/Users/faiz malik/Downloads/my-project-46822-468217-073a81ec7ab7.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

# === 2. Open CRM Sheet ===
sheet = client.open("Lead_CRM").sheet1  # change to your actual sheet name

# === 3. New Lead Data ===
new_lead = [
    "Rohan Sharma",            # Name
    "9876543210",              # Phone
    "rohan@email.com",         # Email
    "Delhi",                   # City
    "MBA Marketing",           # Specialization
    "78",                      # Score
    "Contacted",               # Status
    datetime.now().strftime("%d-%m-%Y"),  # Follow-Up Date
    "Interested in tier-2 colleges"       # Notes
]

# === 4. Append to Sheet ===
sheet.append_row(new_lead)
print("✅ Lead added to CRM.")
# LeadGPT agent logic placeholder
# ContentGPT agent logic placeholder
# WebGPT agent logic placeholder
# OpenAI helper functions placeholder
# gspread and Google Sheets integration placeholder
# gspread and Google Sheets integration placeholder
# gspread and Google Sheets integration placeholder
# Entry point for Cerebro backend 


