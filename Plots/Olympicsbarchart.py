import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Filtering US Cases
# filtered_df = df[df['NOC'] == 1]

# Removing empty spaces from State column to avoid errors
# filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by Country Column
#new_df = filtered_df.groupby(['NOC'])['Total']

# Sorting values and select first 20 contries
new_df = df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data x axis shows states while the y axis shows confirmed cases
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Total Medals Earn during RIO Olympics 2016', xaxis_title="Countries",
                   yaxis_title="Number of Medals earned")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympicbarchart.html')