# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import csv

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

sales = []
dates = []
regions = []

with open('../data/daily_sales_data_combined.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        sales.append(row[0])
        dates.append(row[1])
        regions.append(row[2])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Sales": sales,
    "Date": dates,
    "Region": regions
})

fig = px.line(df, x="Date", y="Sales", color="Region")

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel sales over time'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)