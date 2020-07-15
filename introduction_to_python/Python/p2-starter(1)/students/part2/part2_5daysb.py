import plotly.express as px
import pandas as pd

import json
from datetime import datetime
with open('C:/Users/cplei/Documents/GitHub/Python-repo/introduction_to_python/Python/p2-starter(1)/students/part2/data/forecast_5days_b.json') as json_file:
    data = json.load(json_file)

def convert_f_to_c(temp_in_farenheit):
    temp_in_celcius=((temp_in_farenheit-32)*5/9)
    if temp_in_celcius %1 == 0:
        return int(temp_in_celcius)
    else:
        return float(round(temp_in_celcius,1))

def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

Date=[]
Min_value=[]
Max_value=[]
Min_feel_value=[]
Min_shade_value=[]
    
   
for forecast in data["DailyForecasts"]:
    Date.append(convert_date(forecast['Date']))
    Min_value.append(convert_f_to_c(forecast['Temperature']['Minimum']['Value']))
    Max_value.append(convert_f_to_c(forecast['Temperature']['Maximum']['Value']))
    Min_feel_value.append(convert_f_to_c(forecast['RealFeelTemperature']['Minimum']['Value']))
    Min_shade_value.append(convert_f_to_c(forecast['RealFeelTemperatureShade']['Minimum']['Value']))
print(Min_value)
print(Max_value)
print(Min_feel_value)
print(Min_shade_value)
print(Date)
        
# Using hard coded data
df = {
    "Min_value": [15, 11.1, 8.9, 11.1, 11.7],
    "Max_value": [21.7, 19.4, 18.9, 20, 18.9],
    "Min_feel_value & Min_shade_value": [11.1, 11.7, 8.3, 10, 10.6],
    #"Min_shade_value": [11.1, 11.7, 8.3, 10, 10.6],
    "Date": ['Monday 22 June 2020', 'Tuesday 23 June 2020', 'Wednesday 24 June 2020', 'Thursday 25 June 2020', 'Friday 26 June 2020']
}


fig = px.line(df, y=["Min_value", "Max_value"], x="Date", title="5 Day Overview")
fig.update_xaxes(tickangle=45)
fig.update_yaxes(tickvals=[0, 2, 4, 6, 8, 10, 12, 14, 16,18,20,22,24])
fig.show()

fig2 = px.line(df, y=["Min_value", "Min_feel_value & Min_shade_value"], x="Date", title="5 Day Overview") 
fig2.update_yaxes(tickvals=[0, 2, 4, 6, 8, 10, 12, 14, 16])
fig2.update_xaxes(tickangle=45)
fig2.show()


