# https://stackoverflow.com/questions/55719743/accessing-the-contents-of-a-public-google-sheet-as-csv-using-requests-or-other
import requests as rs
import pandas as pd

# Public google sheet that contains our results
csv_url="https://docs.google.com/spreadsheets/d/e/2PACX-1vSQTlUMZ3zA543Gs4fHJvPvEO4Ld2xV_bQJyH5qmZ6X5melHeWa5nugeZXWA23acj0u5phl1E7OuTqL/pub?output=csv"

def get_sheets_data(csv):
    res=rs.get(url=csv)
    open("results.csv","wb").write(res.content)
    df_unsorted = pd.read_csv("results.csv")
    df_sorted = df_unsorted.loc[::-1]
    html_table = df_sorted.to_html()
    print(html_table)
