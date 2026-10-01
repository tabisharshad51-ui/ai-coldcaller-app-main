import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google-credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("AI Leads").sheet1

st.title("📞 AI Cold Caller Dashboard")

if st.button("Start Listening"):
    st.success("✅ Voice agent is ready (trigger your phone script separately).")

if st.button("View Leads"):
    leads = sheet.get_all_records()
    st.table(leads)
