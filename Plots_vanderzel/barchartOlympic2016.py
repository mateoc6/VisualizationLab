import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('Datasets/Olympic2016Rio.csv')

filtered_df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]
layout = go.Layout(title='Top Countries by Medals in the 2016 Rio Olympics', xaxis_title="Countries",
                   yaxis_title="Medals")


fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchartOlympics.html')
