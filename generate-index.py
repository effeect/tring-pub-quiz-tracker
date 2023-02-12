from jinja2 import Template

import pubdata
from pubdata import *

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSQTlUMZ3zA543Gs4fHJvPvEO4Ld2xV_bQJyH5qmZ6X5melHeWa5nugeZXWA23acj0u5phl1E7OuTqL/pub?output=csv"
csv_url2 = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRw2kPIQF9YSrR6VJWuSwn95y9eP2oXUIrXZg7uvt8sE4ALLRhBAXTs2Pnhd5XnULZSRmWDJlIGjTOP/pub?output=csv"


with open('index_template.html') as file_:
    template = Template(file_.read())

table_data = pubdata.get_sheets_data(csv_url)
table_data2 = pubdata.get_sheets_data(csv_url2)

output = template.render(table=table_data, table2=table_data2)


def publish_html(data):
    with open("index.html", "w") as file_:
        file_.write(data)
        file_.close()


if __name__ == "__main__":
    publish_html(output)
    print(output)
