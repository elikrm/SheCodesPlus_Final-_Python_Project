import json
from datetime import datetime
import plotly.express as px

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees and celcius symbols.
    
    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"
def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.
    
    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year
    """
    d = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    return d.strftime("%A %d %B %Y")
def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    temp_in_celcius = ((temp_in_farenheit - 32) * 5 / 9)
    temp_in_celcius = round(temp_in_celcius, 1)
    return(temp_in_celcius)
    # pass
# df = pd.read_json(r"forecast_5days_a.json",'DailyForecasts')
Minimum_Temperature_array = []
Maximum_Temperature_array = []
Date_in_line_array = []
Real_Feel_Temperature_array = []
Real_Feel_Temperature_Shade_array = []
with open("data/forecast_8days.json") as json_file:
    json_data = json.load(json_file)
    numDays = len(json_data["DailyForecasts"])
    for i in range(numDays):
        Date_in_line = json_data["DailyForecasts"][i]["Date"]
        Date_in_line = convert_date(Date_in_line)
        Date_in_line_array.append(Date_in_line)
    
        Minimum_Temperature = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
        Minimum_Temperature = convert_f_to_c(Minimum_Temperature)
        Minimum_Temperature_array.append(Minimum_Temperature)

        Maximum_Temperature = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
        Maximum_Temperature = convert_f_to_c(Maximum_Temperature)
        Maximum_Temperature_array.append(Maximum_Temperature)

        Real_Feel_Temperature = json_data["DailyForecasts"][i]["RealFeelTemperature"]["Minimum"]["Value"]
        Real_Feel_Temperature = convert_f_to_c(Real_Feel_Temperature)
        Real_Feel_Temperature_array.append(Real_Feel_Temperature)

        Real_Feel_Temperature_Shade = json_data["DailyForecasts"][i]["RealFeelTemperatureShade"]["Minimum"]["Value"]
        Real_Feel_Temperature_Shade = convert_f_to_c(Real_Feel_Temperature_Shade)
        Real_Feel_Temperature_Shade_array.append(Real_Feel_Temperature_Shade)


# print(Minimum_Temperature_array)
# print(Minimum_Temperature_array)
# print(Date_in_line_array)
print(Real_Feel_Temperature_array)
print(Real_Feel_Temperature_Shade_array)

# A single time series graph that contains both the minimum and maximum temperatures for each day.
df = {
"Minimum Temperature": Minimum_Temperature_array,
"Maximum Temperate": Maximum_Temperature_array,
"Days": Date_in_line_array
}
fig = px.line(df, 
y=["Minimum Temperature","Maximum Temperate"],
x="Days",
title= "Forecast Graphs including Daily Minimum and Maximum Temperature",
labels ={"variable": "Temperature", "value": "Temperature in degrees celcius"})
fig.write_html("MyGraph.html")
#A single time series graph that contains 
# the minimum temperatures, 
# minimum “real feel temperatures”, and 
# minimum “real feel shade” temperatures.

df = {
"Minimum Temperature": Minimum_Temperature_array,
"Minimum real feel temperatures": Real_Feel_Temperature_array,
"Minimum real feel shade temperatures": Real_Feel_Temperature_Shade_array,
"Days": Date_in_line_array
}
fig = px.bar(df,
 y=["Minimum Temperature","Minimum real feel temperatures","Minimum real feel shade temperatures"],
  x="Days",
  title= "Forcast Graph including minimum, minimum real feel, minimum real feel shade temperatures",
  labels ={"variable": "Temperature", "value": "Temperature in degrees celcius"},
  barmode="group")
fig.write_html("MyGraph2.html")