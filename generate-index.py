from jinja2 import Template

import pubdata
from pubdata import *

csv_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSQTlUMZ3zA543Gs4fHJvPvEO4Ld2xV_bQJyH5qmZ6X5melHeWa5nugeZXWA23acj0u5phl1E7OuTqL/pub?output=csv"

template = "Error"
# output = template.render(title="My Title", headline="My Headline", content="My Content")

with open('index_template.html') as file_:
    template = Template(file_.read())

table_data = pubdata.get_sheets_data(csv_url)
output = template.render(table=table_data)


def publish_html(data):
    with open("index.html", "w") as file_:
        file_.write(data)
        file_.close()


if __name__ == "__main__":
    publish_html(output)
    print(output)
