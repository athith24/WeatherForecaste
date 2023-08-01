import requests

#API endpoint to get hourly weather forecast data for London
WEATHER_API_ENDPOINT = 'https://samples.openweathermap.org/data/2.5/forecast/hourly'

def get_weather(date):
    try:
        response = requests.get(WEATHER_API_ENDPOINT, params={'q': 'London,uk', 'appid': 'b6907d289e10d714a6e88b30761fae22'})
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        data = response.json()
        weather_data = next((entry for entry in data['list'] if entry['dt_txt'].startswith(date)), None)
        if weather_data:
            return weather_data['main']['temp']
        else:
            print(f"No weather data available for date {date}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except KeyError:
        print(f"Error: Invalid API response format.")
        return None

def get_wind_speed(date):
    try:
        response = requests.get(WEATHER_API_ENDPOINT, params={'q': 'London,uk', 'appid': 'b6907d289e10d714a6e88b30761fae22'})
        response.raise_for_status()
        data = response.json()
        weather_data = next((entry for entry in data['list'] if entry['dt_txt'].startswith(date)), None)
        if weather_data:
            return weather_data['wind']['speed']
        else:
            print(f"No wind speed data available for {date}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except KeyError:
        print(f"Error: Invalid API response format.")
        return None

def get_pressure(date):
    try:
        response = requests.get(WEATHER_API_ENDPOINT, params={'q': 'London,uk', 'appid': 'b6907d289e10d714a6e88b30761fae22'})
        response.raise_for_status()
        data = response.json()
        weather_data = next((entry for entry in data['list'] if entry['dt_txt'].startswith(date)), None)
        if weather_data:
            return weather_data['main']['pressure']
        else:
            print(f"No pressure data available for {date}.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except KeyError:
        print(f"Error: Invalid API response format.")
        return None

def get_user_choice():
    print("\n1. Get weather\n2. Get Wind Speed\n3. Get Pressure\n0. Exit")
    return input("Enter your choice: ")

def get_user_date():
    return input("Enter the date (YYYY-MM-DD): ")

def print_weather(date):
    temp = get_weather(date)
    if temp is not None:
        print(f"The temperature on {date} is {temp} degrees Celsius.")

def print_wind_speed(date):
    wind_speed = get_wind_speed(date)
    if wind_speed is not None:
        print(f"The wind speed on {date} is {wind_speed} m/s.")

def print_pressure(date):
    pressure = get_pressure(date)
    if pressure is not None:
        print(f"The pressure on {date} is {pressure} hPa.")

def main():
    while True:
        choice = get_user_choice()

        if choice == '1':
            date = get_user_date()
            print_weather(date)
        elif choice == '2':
            date = get_user_date()
            print_wind_speed(date)
        elif choice == '3':
            date = get_user_date()
            print_pressure(date)
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, Please try again.")

if __name__ == "__main__":
    main()