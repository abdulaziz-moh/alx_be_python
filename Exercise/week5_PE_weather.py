import requests
import json
resopnse = requests.get("https://api.open-meteo.com/v1/forecast?latitude=9.025&longitude=38.7469&hourly=rain,apparent_temperature&timezone=auto&forecast_days=1")

json_format_data = resopnse.text  # it returns text(str) after decoding it internally
                     # if it was response.content it returns the request as a raw byte and we can manuplate it further
data = json.loads(json_format_data)   # Load the JSON string into a Python dictionary

# Extract the time stamps and temperatures
time_stamps = data['hourly']['time']
temperatures = data['hourly']['apparent_temperature']
rains = data['hourly']['rain']

temperature_unit = data['hourly_units']['apparent_temperature'] # Get the unit for printing

length = len(time_stamps)

print("|-------------------------------------------------------------------------------------------------------------------------------------|")
print("|                                              WHETHER OF THE DAY FROM 12:00 TO 11:00                                                 |")
print("|-------------------------------------------------------------------------------------------------------------------------------------|")
print("|-------------------------------------------------------------------------------------------------------------------------------------|")
print("| HOUR        |  12:00       01:00     02:00     03:00     04:00     05:00    06:00     07:00     08:00     09:00     10:00     11:00 |")
print("|-------------------------------------------------------------------------------------------------------------------------------------|")
print("| TEMPERATURE |", end = "")

for i in range(12):
    print(f" {temperatures[i]} {temperature_unit} ", end = "|")
print()
print("|-------------------------------------------------------------------------------------------------------------------------------------|")
print("| RAIN        |", end = "")
for i in range(12):
    print(f"   {rains[i]}   ",end = "|")
print()
print("|_____________________________________________________________________________________________________________________________________|")