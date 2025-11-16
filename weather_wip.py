# Weather_program.py
# This program gives suggestions based on the current temperature.
temperature = input("Please enter the current temperature: ")
temperature = int(temperature)
forecast = input("Please enter the weather forecast (sunny, rainy, cloudy, etc.): ")
forcast = str(forecast)

# Provide suggestions based on the temperature and forecast
if temperature > 95 and forcast == "sunny":
    print("It's really hot and sunny today! Stay inside and drink plenty of water.")
elif 70 <= temperature <85 and forcast == "sunny":
    print("It's a warm and sunny day! Go out and enjoy!")
elif 55 < temperature < 70 and forecast == "sunny":
    print("It's a moderate temperature outside today. A light sweater should be fine.")
elif 40 < temperature < 55 and forecast == "cloudy":
    print("It's a little chilly outside, consider wearing a light jacket if you step out.")
elif 55 < temperature < 70 and forecast == "cloudy":
    print("The weather today is moderate with a touch of clouds. A light sweater should be fine.")
elif 30 < temperature <= 50 and forecast == "rainy":
    print("It's raining cats, dogs, frogs and hogs! Go outside with an umbrella and a raincoat.")
elif temperature <= 30 and forecast == "cloudy" or forecast == "rainy":
    print("It's quite cold and cloudy/rainy today! Better to stay indoors and keep warm." \
    " Don't forget to wear a raincoat if you go outside!")