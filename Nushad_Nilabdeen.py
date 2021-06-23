import requests
#import as
from datetime import datetime

api_key = "096f53866a92182f849c9ef1d5f10ac5"
location = input("Enter the city name: ")

complete_api_link ="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data["main"]["temp"]) -273.15)
weather_desc = api_data["weather"][0]["description"]
hmdt = api_data["main"]["humidity"]
wind_spd = api_data["wind"]["speed"]
date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")

title = "Weather stats for- {} || {}".format(location.upper(), date_time)
data1 = "Current temperature is: {:.2f} deg C".format(temp_city)
data2 = "Current weather desc :"+str(weather_desc)
data3 = "Current Humidity     :"+str(hmdt)+'%'
data4 = "Current wind speed   :"+str(wind_spd)+'kmph'
l = "---------------------------------------------------------------"

result = l+"\n"+title+"\n"+l+"\n"+data1+"\n"+data2+"\n"+data3+"\n"+data4

print("---------------------------------------------------------------")
print("Weather stats for- {} || {}".format(location.upper(), date_time))
print("---------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc :",weather_desc)
print("Current Humidity     :",hmdt, '%')
print("Current wind speed   :",wind_spd, 'kmph')

text_file=open("report.txt","w")
text_file.write(result)
text_file.close()
