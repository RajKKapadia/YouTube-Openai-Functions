tools = [
    {
        "type": "function",
        "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
        },
    },
    {
        "type": "function",
        "function": {
                "name": "get_current_weather_for_ndays",
                "description": "Get the current weather in a given location for n number of days.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                        "n_days": {
                            "type": "number",
                            "description": "number of days to forecaste the weather, e.g. 5"
                        }
                    },
                    "required": ["location", "n_days"],
                },
        },
    }
]
