import json
from datetime import datetime

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


def calculate_mean(total, num_items):
    """Calculates the mean.
    
    Args:
        total: integer representing the sum of the numbers.
        num_items: integer representing the number of items counted.
    Returns:
        An integer representing the mean of the numbers.
    """
    # pass
    mean_items = round((total / num_items), 1)
    return(mean_items)


def process_weather(forecast_file):
    """Converts raw weather data into meaningful text.

    Args:
        forecast_file: A string representing the file path to a file
            containing raw weather data.
    Returns:
        A string containing the processed and formatted weather data.
    """
    with open(forecast_file) as json_file:
        json_data = json.load(json_file)
        numDays = len(json_data["DailyForecasts"])
        Lowest_temp = json_data["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]
        Day_Lowest_temp = convert_date(json_data["DailyForecasts"][0]["Date"])
        highest_temp = json_data["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]
        Day_highest_temp = convert_date(json_data["DailyForecasts"][0]["Date"])
        average_low_temp = 0
        total_low = 0
        average_high_temp = 0
        total_high = 0

        for i in range(numDays):
            if(Lowest_temp > json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]):
                Lowest_temp = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
                Day_Lowest_temp = convert_date(json_data["DailyForecasts"][i]["Date"])
            
            if(highest_temp < json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]):
                highest_temp = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
                Day_highest_temp = convert_date(json_data["DailyForecasts"][i]["Date"])

            total_low += json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
            total_high += json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
        average_low_temp = format_temperature(convert_f_to_c(calculate_mean(total_low, numDays)))
        average_high_temp = format_temperature(convert_f_to_c(calculate_mean(total_high, numDays)))
        output_buffer = "{} Day Overview\n".format(numDays)
        output_buffer += "    The lowest temperature will be {}, and will occur on {}.\n".format(format_temperature(convert_f_to_c(Lowest_temp)), Day_Lowest_temp)
        output_buffer += "    The highest temperature will be {}, and will occur on {}.\n".format(format_temperature(convert_f_to_c(highest_temp)), Day_highest_temp)
        output_buffer += "    The average low this week is {}.\n".format(average_low_temp)
        output_buffer += "    The average high this week is {}.\n".format(average_high_temp)
        output_buffer += "\n"
        
        Minimum_Temperature = 0
        Maximum_Temperature = 0
        Day_LongPhrase = 0
        Day_Chance_of_rain = 0
        Night_LongPhrase = 0
        Night_RainProbability = 0
        for i in range(numDays):
            Date_in_line = json_data["DailyForecasts"][i]["Date"]
            Date_in_line = convert_date(Date_in_line)
            Minimum_Temperature = json_data["DailyForecasts"][i]["Temperature"]["Minimum"]["Value"]
            Minimum_Temperature = format_temperature(convert_f_to_c(Minimum_Temperature))
            Maximum_Temperature = json_data["DailyForecasts"][i]["Temperature"]["Maximum"]["Value"]
            Maximum_Temperature = format_temperature(convert_f_to_c(Maximum_Temperature))
            Day_LongPhrase = json_data["DailyForecasts"][i]["Day"]["LongPhrase"]
            Day_Chance_of_rain = json_data["DailyForecasts"][i]["Day"]["RainProbability"]
            Night_LongPhrase =json_data["DailyForecasts"][i]["Night"]["LongPhrase"]
            Night_RainProbability = json_data["DailyForecasts"][i]["Night"]["RainProbability"]

            output_buffer += "-------- {} --------\n".format(Date_in_line)
            output_buffer += "Minimum Temperature: {}\n".format(Minimum_Temperature)
            output_buffer += "Maximum Temperature: {}\n".format(Maximum_Temperature)
            output_buffer += "Daytime: {}\n".format(Day_LongPhrase)
            output_buffer += "    Chance of rain:  {}%\n".format(Day_Chance_of_rain)
            output_buffer += "Nighttime: {}\n".format(Night_LongPhrase)
            output_buffer += "    Chance of rain:  {}%\n".format(Night_RainProbability)
            output_buffer += "\n"

    return(output_buffer)
    
if __name__ == "__main__":
    print(process_weather("data/forecast_5days_a.json"))





