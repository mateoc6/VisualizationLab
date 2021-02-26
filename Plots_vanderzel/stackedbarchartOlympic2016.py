import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/Olympic2016Rio.csv')
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

new_df = df.sort_values(by=['Total'],
    ascending=[False]).head(20).reset_index()

trace1 = go.Bar(x=new_df['NOC'], y=new_df['Bronze'], name='Bronze',
    marker={'color': '#CD7F32'})
trace2 = go.Bar(x=new_df['NOC'], y=new_df['Silver'], name='Silver',
    marker={'color': '#9EA0A1'})
trace3 = go.Bar(x=new_df['NOC'], y=new_df['Gold'], name='Gold',
    marker={'color': '#FFD700'})
data = [trace1, trace2, trace3]

layout = go.Layout(title='Gold, Silver, and Bronze medals of the top 20 Countries of the 2016 Olympics', xaxis_title="Country",
yaxis_title="Number of Medals", barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Olympics2016stackedbarchart.html')
