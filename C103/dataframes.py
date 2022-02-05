#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
import pandas as pd

#empty dataframe
df = pd.DataFrame()
print(df)

#list
data = [34,56,78]
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

#dictionary
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

#loc attribute to return one or more specified row(s)
print(df.loc[1])
print(df.loc[[1,2]])

#With the index argument, you can name your own indexes
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

#Use the named index in the loc attribute to return the specified row(s).
print(df.loc["day2"])

#loading csv file into DataFrame (CSV files (comma separated files))
df = pd.read_csv('csv files/data.csv')
print(df) 
#If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows
df = pd.read_csv('csv files/line_chart.csv')
print(df) 



