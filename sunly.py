from datetime import datetime, timedelta
from astral import LocationInfo
from astral.sun import sun
import pytz

def compute_sundial_time(latitude, longitude, timezone_str):
    # Get the current time in the given timezone
    tz = pytz.timezone(timezone_str)
    current_time = datetime.now(tz)
    # Define the location
    location = LocationInfo("Custom Location", "", timezone_str, latitude, longitude)

    # Calculate solar noon for the location and date
    s = sun(location.observer, date=current_time.date(), tzinfo=tz)
    solar_noon = s['noon']

    # Calculate the difference from the current time to solar noon
    time_difference = current_time - solar_noon

    # Adjust the current time by the time difference to compute the sundial time
    sundial_time = datetime(solar_noon.year, solar_noon.month, solar_noon.day, 12, 0, 0) + time_difference

    # Return the sundial time in ISO 8601 format
    return sundial_time.isoformat()

# Example usage
latitude = 40.7128  # New York City latitude
longitude = -74.0060  # New York City longitude
timezone_str = "America/New_York"

sundial_time = compute_sundial_time(latitude, longitude, timezone_str)
print(f"Sundial time: {sundial_time}")