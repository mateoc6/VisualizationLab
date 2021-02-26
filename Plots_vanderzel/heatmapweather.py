import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('Datasets/Weather2014-15.csv')

data = [go.Heatmap(x=df['day'],
y=df['month'],
z=df['actual_max_temp'].values.tolist(),
colorscale='Jet')]

layout = go.Layout(title='2014-15 Max Temp Heatmap', xaxis_title="Day of Week",
yaxis_title="Month")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='heatmapweather.html')
