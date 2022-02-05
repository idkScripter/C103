import pandas as pd
import plotly.express as px

df = pd.read_csv("csv files/data.csv")
print(df.head())

fig = px.bar(df, x="Country", y="InternetUsers")
fig.show()