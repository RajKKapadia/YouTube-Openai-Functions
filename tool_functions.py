def get_current_weather(function_args: dict) -> str:
    """Extract the arguments and do stuff with it.
    """
    print(function_args)
    return "The weather in cith Ahmedabas is 25 degree celcius."


def get_current_weather_for_ndays(function_args: dict) -> str:
    print(function_args)
    return "The weather in cith Ahmedabad for the upcoming 5 days will 25 degree celcius."


available_functions = {
    "get_current_weather": get_current_weather,
    "get_current_weather_for_ndays": get_current_weather_for_ndays
}
