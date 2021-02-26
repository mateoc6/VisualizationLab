import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/Weather2014-15.csv')

new_df = df.groupby(['date']).agg(
    {'actual_max_temp': 'max'}).reset_index()

data = [go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Temperature')]

layout = go.Layout(title='Max Temperature of Each Month', xaxis_title="Month",
yaxis_title="Temperature")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherlinechart.html')
