import json
from datetime import datetime
 
DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

#all done - thanks Hayley
def format_temperature(temp):
    return f"{temp}{DEGREE_SYBMOL}"
    
#all done- thanks again Hayley
def convert_date(iso_string):
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime('%A %d %B %Y')

#if result is 0dp then print int otherwise print float to 1 dp
def convert_f_to_c(temp_in_farenheit):
    temp_in_celcius=((temp_in_farenheit-32)*5/9)
    if temp_in_celcius %1 == 0:
        return float(round(temp_in_celcius,0))
    else:
        return float(round(temp_in_celcius,1))

#if mean result is int print int otherwise print float to 1 dp
def calculate_mean(total, num_items):
    mean=(total/num_items)
    if mean %1 == 0:
        return int(mean)
    else:
        return float(round(mean,1))


def process_weather(forecast_file): 
    with open(forecast_file) as json_file:
        data = json.load(json_file)
   #print(type(data)) #dictionary
   #print(type(data['DailyForecasts'])) #list
    #create empty lists and dictionaries
    Date=[]
    Min_value=[]
    Max_value=[]
    DLongphrase=[]
    DChancerain=[]
    NLongphrase=[]
    NChancerain=[]
    DataMin=dict()
    DataMax=dict() 

    #get json data out of dictionaries and lists and append to lists 
    for forecast in data["DailyForecasts"]:
        Date.append(convert_date(forecast['Date']))
        Min_value.append(convert_f_to_c(forecast['Temperature']['Minimum']['Value']))
        Max_value.append(convert_f_to_c(forecast['Temperature']['Maximum']['Value']))
        DLongphrase.append(forecast['Day']['LongPhrase'])
        DChancerain.append(forecast['Day']['RainProbability'])    
        NLongphrase.append(forecast['Night']['LongPhrase'])
        NChancerain.append(forecast['Night']['RainProbability'])

    # get json data for dictionaries to calculate date with min temp AND date with max temp
    for forecast in data["DailyForecasts"]:
        Date2=(convert_date(forecast['Date']))
        Min_temp=(convert_f_to_c(forecast['Temperature']['Minimum']['Value']))
        Max_temp=(convert_f_to_c(forecast['Temperature']['Maximum']['Value']))
        DataMin[Date2]=Min_temp
        DataMax[Date2]=Max_temp
        
       
    #order dictionaries to get maximum with date and minimum with date
    # def by_value(forecast):
    #     return forecast[1]
    # for k, v in sorted(DataMin.items(), key=by_value):
    #     print(k,'->', v)  
    # for k,v in sorted(DataMax.items(), reverse=True, key=by_value):
    #     print(k, '->', v)
    #import collections
    sorted_min=sorted(DataMin.items(), key=lambda x:x[1])
    #sorted_dictmin=collections.OrderedDict(sorted_min) 

    sorted_max=sorted(DataMax.items(), key=lambda x:x[1], reverse=True)
    #sorted_dictmax=collections.OrderedDict(sorted_max)
    
    date_min_dictmin= sorted_min[0]
    #print(date_min_dictmin[0]) #Friday 19 June 2020
    #print(date_min_dictmin[1]) #8.3
    date_max_dictmax= sorted_max[0]
    #print(date_max_dictmax[0]) #Sunday 21 June 2020
    #print(date_max_dictmax[1]) #22.2
   
    #print(DataMin)
    #print(DataMax)

    #calculate means   
    mean_Min_value=calculate_mean(sum(Min_value),len(Min_value))
    mean_Max_value=calculate_mean(sum(Max_value),len(Max_value))
    
    #time to put it all together
    string=[] 

    write= "{} Day Overview\n".format(len(Date))
    string.append(write)
    write= "    The lowest temperature will be {}{}, and will occur on {}.\n".format(date_min_dictmin[1], DEGREE_SYBMOL, date_min_dictmin[0])
    string.append(write)
    write= "    The highest temperature will be {}{}, and will occur on {}.\n".format(date_max_dictmax[1], DEGREE_SYBMOL, date_max_dictmax[0])
    string.append(write)
    write= "    The average low this week is {}{}.\n".format(mean_Min_value, DEGREE_SYBMOL)
    string.append(write)
    write= "    The average high this week is {}{}.\n\n".format (mean_Max_value, DEGREE_SYBMOL)
    string.append(write)

    
    for temps in range(len(Date)):
        string.append("-------- "+Date[temps]+" --------\n")
        write= "Minimum Temperature: {}{}\n".format(Min_value[temps], DEGREE_SYBMOL)
        string.append(write)
        write="Maximum Temperature: {}{}\n".format(Max_value[temps], DEGREE_SYBMOL)
        string.append(write)
        write= "Daytime: {}\n".format(DLongphrase[temps])
        string.append(write)
        write="    Chance of rain:  {}%\n".format(DChancerain[temps])
        string.append(write)
        write= "Nighttime: {}\n".format(NLongphrase[temps])
        string.append(write)
        write="    Chance of rain:  {}%\n\n".format(NChancerain[temps])
        string.append(write)

    final_string=''.join(string)
    
    return(final_string)

if __name__ == "__main__":
    print(process_weather("data/forecast_5days_b.json"))


