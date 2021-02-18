import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
df = pd.read_csv('../Datasets/Weather2014-15.csv')
# Removing empty spaces from State column to avoid errors
#df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
# Creating unrecovered column
#df['Average'] = df['actual_max_temp'] - df['actual_min_temp']
# Removing China and Others from data frame
#df = df[(df['Country'] != 'China') & (df['Country'] != 'Others')]
# Creating sum of number of cases group by Country Column
# new_df = df.groupby(['month']).agg(
# {'actual_max_temp': 'max', 'actual_min_temp': 'min', 'Average': 'max'}).reset_index()
# Preparing data scatter data in to clusters of recovered and unrecovered by difference
data = [
go.Scatter(x=df['average_min_temp'],
y=df['average_max_temp'],
text=df['month'],
mode='markers',
marker=dict(size=df['average_max_temp'] / 10,color=df['average_max_temp'] / 10, showscale=True))
]
# Preparing layout
layout = go.Layout(title='Min and Max temperatures per month', xaxis_title="Average Min Temperature",
yaxis_title="Average Max Temperature", hovermode='closest')
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='weatherbubblechart.html')