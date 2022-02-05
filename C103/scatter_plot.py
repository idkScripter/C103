from turtle import color
from numpy import size
import pandas as pd
import plotly.express as px

df = pd.read_csv("csv files/data.csv")
print(df.head())

fig = px.scatter(df, x="Population", y="Per capita", color="Country", size_max=60, size="Percentage")
fig.show()