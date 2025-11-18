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
elif 40 < temperature < 55 and forecast == "sunny":
    print("It's a little chilly outside, consider wearing a light jacket if you step out.")
elif 55 < temperature < 70 and forecast == "sunny":
    print("The weather today is moderate without a cloud in the sky. A light sweater should be fine, but isn't needed.")
elif 30 < temperature <= 50 and forecast == "sunny":
    print("The shining sun is a mirage to distract you from the freezing temp.")
elif temperature > 95 and forcast == "cloudy":
    print("Looks pretty hot and humid out. Better to stay in doors unless you like frizzy hair.")
elif 70 <= temperature <85 and forcast == "cloudy":
    print("Definitely on the warmer side today. May be a possibility for light showers.")
elif 55 < temperature < 70 and forecast == "cloudy":
    print("Moderate temperature today, but bring a sweater just in case.")
elif 40 < temperature < 55 and forecast == "cloudy":
    print("On the colder side today, I wouldn't go outside without a coat.")
elif 30 < temperature <= 50 and forecast == "cloudy":
    print("You won't catch me outside, but you're more than welcome.")
elif temperature > 95 and forcast == "rainy":
    print("Some signs of spotted showers and increased humity today. Inside might be the most comfortable option.")
elif 70 <= temperature <85 and forcast == "rainy":
    print("It's raining cat and dogs and it doesn't look like it's going to slow down anytime soon. Could be a hurricane. *shrugs*")
elif 55 < temperature < 70 and forecast == "rainy":
    print("Light rain, an umbrella should solve most of your problems today.")
elif 40 < temperature < 55 and forecast == "rainy":
    print("This rain is no joke. Have a seat on the couch and put on your fav straming platform.")
elif 30 < temperature <= 50 and forecast == "rainy":
    "If you want to become an ice cube, go outside."
breakpoint
