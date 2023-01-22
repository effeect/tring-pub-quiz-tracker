# https://stackoverflow.com/questions/55719743/accessing-the-contents-of-a-public-google-sheet-as-csv-using-requests-or-other
import requests as rs
import pandas as pd
def get_sheets_data(csv):
    res=rs.get(url=csv)
    open("results.csv","wb").write(res.content)
    df_unsorted = pd.read_csv("results.csv")
    df_sorted = df_unsorted.loc[::-1]
    html_table = df_sorted.to_html(classes='table table-bordered table-dark" id="myTable')
    print(html_table)
    return html_table
