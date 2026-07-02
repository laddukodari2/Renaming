import requests

API_KEY = "ca49e43f2f60fe50d63fe39c88f1bf4c"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print("\n------ Weather Report ------")
        print("City:", city)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Condition:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
    else:
        print("Error:", data.get("message"))

except Exception as e:
    print("Error:", e)
    