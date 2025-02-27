# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import csv

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

app = Dash()

sales = []
dates = []
regions = []

region_choices = ["north", "south", "east", "west", "all"]

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

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel sales over time'),

    dcc.Graph(
        id='example-graph',
    ),

    dcc.RadioItems(
        list(region_choices),
        'North',
        id='region-radio',
    ),
])

@callback(
    Output('example-graph', 'figure'),
    Input('region-radio', 'value'))
def update_figure(region_value):
    if region_value == "all":
        filtered_df = df
    else:
        filtered_df = df[df.Region == region_value]

    fig = px.line(filtered_df, x="Date", y="Sales", color="Region")

    fig.update_layout(transition_duration=500)

    return fig

if __name__ == '__main__':
    app.run(debug=True)