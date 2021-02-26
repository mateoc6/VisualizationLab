import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/Weather2014-15.csv')


new_df = df.groupby(['month']).agg(
    {'actual_max_temp': 'max', 'actual_mean_temp': 'mean', 'actual_min_temp': 'min'}).reset_index()

data = [
go.Scatter(x=new_df['month'], y=new_df['actual_max_temp'], text=new_df['month'],
mode='markers', marker=dict(size=new_df['actual_mean_temp'],color=new_df['actual_min_temp'], showscale=True))]
# Preparing layout

layout = go.Layout(title='Temperature Bubble Map', xaxis_title="Month",
yaxis_title = "Max Temperature", hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bubblechartweather.html')
