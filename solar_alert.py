import requests

import yagmail

def send_email_alert(subject, contents):
    receiver = "kadamsamrudhi2@gmail.com"  
    sender = "kadamsamrudhi2@gmail.com"     
    password = "obzx srue uxqf lvyz"       

    try:
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

def fetch_solar_flare_data():
    url = "https://services.swpc.noaa.gov/json/goes/primary/xrays-1-day.json"
    response = requests.get(url)
    data = response.json()
    return data

def process_data_and_alert(data, threshold=1.0e-6):
   
    alerts = []
    for record in data:
        print(record)
        time = record.get("time_tag")
        xray_short = float(record.get("flux", 0))
        print(xray_short)
        if xray_short >= threshold:
         send_email_alert("Solar Flare Alert", f"ALERT: High solar flare at {time} with X-ray flux {xray_short}")
         alerts.append(f"ALERT: High solar flare at {time} with X-ray flux {xray_short}")
    return alerts

if __name__ == "__main__":
    solar_data = fetch_solar_flare_data()
    alerts = process_data_and_alert(solar_data, threshold=1.0e-6)  
    for alert in alerts:
        print(alert)


