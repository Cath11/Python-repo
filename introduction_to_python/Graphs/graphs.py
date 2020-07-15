import plotly.express as px
import pandas as pd

df = pd.read_csv("austpop.csv") #df = dataframe

# Line Graphs
fig = px.line(df, x="year", y="Aust", title="Australia Population")
fig.show()

fig=px.line(df,x="year",y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],
title="AustraliaPopulation by State")
fig.show()

# Scatterplot

fig = px.scatter(df,x=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],y="year") #y=[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000])
fig.show()

# Barchart
fig = px.bar(df, x='year', y=["NSW"])
fig.show()

fig = px.bar(df,x='year',y=["NSW","Vic","Qld","SA","WA","Tas","NT","ACT"],barmode="group")
fig.show()

# Using hard coded data- LINE CHART--  MIGHT BE USEFUL FOR ASSIGNMENT
df_a = {
    "our_data": [123, 132, 654, 345, 125, 498],
    "more_data": [345, 67, 176, 245, 197, 391],
    "columns": ["a", "b", "c", "d", "e", "f"]}
fig = px.line(df, y="our_data", x="columns")
fig.show()

