import requests

url = "https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json"  
response = requests.get(url)
data = response.json()
print(data[:3])   


for item in data[:3]:
    print("Time:", item.get("time_tag"), "X-ray Short:", item.get("xs"))
