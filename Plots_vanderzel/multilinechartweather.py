import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
# Load CSV file from Datasets folder
df = pd.read_csv('Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])

trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='Max Temperature')
trace2 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='Mean Temperature')
trace3 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='Min Temperature')
data = [trace1, trace2, trace3]

layout = go.Layout(title='Mean, Max, and Min Temperatures each month', xaxis_title="month", yaxis_title="Temperature")

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='multilineweather.html')
