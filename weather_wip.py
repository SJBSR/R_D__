# Weather

temperature = input("Please enter the current temperature: ")
temperature = int(temperature)

if temperature > 80:
    print("It's really hot today! Stay inside and drink plenty of water.")
elif temperature <= 60:
    print("The temperature is too cold today. It's suggested to stay inside and enjoy your day!")
elif temperature < 80 and temperature > 60:
    print("The weather is a bit chilly today. Consider wearing a light jacket if you go outside.")
else:
    print("The weather is perfect today! Go outside and enjoy the sunshine!") 
