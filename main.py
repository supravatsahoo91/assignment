import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None


def get_temp_by_date(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["temp"]
    return None


def get_wind_speed_by_date(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["wind"]["speed"]
    return None


def get_pressure_by_date(data, date):
    for forecast in data["list"]:
        if forecast["dt_txt"].startswith(date):
            return forecast["main"]["pressure"]
    return None


def main():
    data = get_weather_data()
    if data is None:
        return

    while True:
        print("\nMenu:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_temp_by_date(data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp} Kelvin")
            else:
                print(f"No weather data available for {date}.")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed_by_date(data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print(f"No weather data available for {date}.")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure_by_date(data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print(f"No weather data available for {date}.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
