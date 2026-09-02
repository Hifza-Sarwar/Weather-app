import requests

API_KEY = "f1dc25b62dd9f88f7b9fca65011af781"
Base_URL = "https://api.openweathermap.org/data/2.5/weather"

while True:
    print("Weather app : Main Menu")
    print("1. Single City Weather")
    print("2. Multiple City Weather")
    print("3. Exit")

    menu_choice = input("Enter your choice(1-3):")
    if menu_choice=="3":
        print("Exiting Weather App.")
        break
    weather = {}
    cities=set()

    if menu_choice=="1":
        while True:
            city=input("\nEnter city name")
            params={
                "q":city,
                "appid":API_KEY,
                "units":"metric"
            }
            print("Fetching wetaher data")
            response = requests.get(Base_URL,params=params)

            if response.status_code == 200:
                data = response.json()
                weather[city] = data
                print("\n==== Weather Summary ====")
                print(f"City:{city}")
                print("-" *30)
                print(f"Temprature {weather[city]['main']['temp']} C")
                print(f"Weather    {weather[city]['weather'][0]['description']}")
                print(f"Humidity   {weather[city]['main']['humidity']}")
                print(f"Wind Speed  {weather[city]['wind']['speed']}")
                print("-" *30)
                break
            else:
                print("City not found")
                continue
    elif menu_choice == "2":
        while True:
            try:
                num_cities = int(input("\nHow many cities to check? (1-4):"))
                if num_cities <1 or num_cities > 4:
                    print("Invalld input! Please enter a  number between 1 and 4.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter the valid number")
                continue
        for num in range(num_cities):
            while True:
                city = input(f"\nEnter city name{num+1}:")
                if not city.strip():
                    print("City name cannot be empty.")
                    continue
                params={
                    "q":city,
                    "appid":API_KEY,
                    "units":"metric"
                }
                print("Fetching weather data")
                response = requests.get(Base_URL,params=params)
                if response.status_code == 200:
                    cities.add(city.strip())

                    data = response.json()
                    weather[city]= data
                    break
                else:
                    print("city not found")
                    continue
            sorted_cities = sorted(cities)
            
           

            print("\n==== Weather Summary ==== ")
            print(f"{'No.': <5}{'City':15}{'Temprature':13}{'Weather':20}{'Humidity':10}{'Wind Speed':10}")
            print("-" * 73)
            for city in sorted_cities:
                print(f"{list(sorted_cities).index(city)+1:<5}",end="")
                print(f"{city:15}",end="")
                print(f"{str(weather[city]['main']['temp']) + 'C':<13}",end="") 
                print(f"{weather[city]['weather'][0]['description']:<20}",end="")
                print(f"{weather[city]['main']['humidity']:<10}",end="")
                print(f"{weather[city]['wind']['speed']:<10}")
                print("-" * 73)
    else:
        print("Invalid chioce! Please select a valid option(1-4).")
        continue

        
