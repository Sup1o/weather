import requests
import tkinter as tk

def get_data(location):
    API = "c702542e4a361637f387ea32ebb9d255" # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API}"
    res = requests.get(url).json()
    return res

def temp(temp):
    celsius = round(temp - 273.15, 2)
    fahrenheit = round((celsius * 9/5) + 32, 2)
    return celsius, fahrenheit

def display_data(data):
    c, f = temp(data["main"]["temp"])
    location_text = f"Location: {data['name']}"
    temp_text = f"Temperature: {c} °C, {f} °F"
    weather_text = f"Weather: {data['weather'][0]['description']}"
    humidity_text = f"Humidity: {data['main']['humidity']}%"
    wind_speed_text = f"Wind Speed: {data['wind']['speed']} m/s"
    weather_info_text = "\n".join([location_text, temp_text, weather_text, humidity_text, wind_speed_text])
    text_widget.delete("1.0", tk.END)  # Clear previous text
    text_widget.insert(tk.END, weather_info_text)

def get_weather():
    location = entry.get()
    if location:
        weather = get_data(location)
        display_data(weather)

root = tk.Tk()
root.title("Weather Forecasting")
root.geometry("400x200")

label = tk.Label(root, text="Enter city name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=get_weather)
button.pack()

text_widget = tk.Text(root, height=10, width=40)
text_widget.pack()

root.mainloop()
