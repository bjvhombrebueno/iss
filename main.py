import requests
from datetime import datetime

MY_LAT = -36.733200 # Your latitude
MY_LONG = 174.752000 # Your longitude
def check_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.


    if iss_longitude+5 > MY_LONG and iss_longitude-5 < MY_LONG and iss_latitude+5 > MY_LAT and iss_latitude-5 < MY_LAT:
        print("True")
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def check_time():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)

    time_now = datetime.now()
    print(time_now.hour)
    if int(time_now.hour) >sunset and int(time_now.hour) < sunrise:
        print("True")
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

check_iss_location()
check_time()

