from sunly import compute_sundial_time
import streamlit as st
from streamlit_geolocation import streamlit_geolocation
import timezonefinder
import time

st.title("Sundial Time")

location = streamlit_geolocation()
print (location)

latitude = location['latitude']
longitude = location['longitude']

if latitude and longitude:
    t = st.empty()
    tf = timezonefinder.TimezoneFinder()
    detected_timezone = tf.timezone_at(lat=latitude, lng=longitude)
    if detected_timezone:
        timezone = detected_timezone

    while True:
        if latitude and longitude and timezone:
            sundial_time = compute_sundial_time(latitude, longitude, timezone)
            # st.write(f"Estimated Sundial Time: {sundial_time}")
            sundial_time = sundial_time.replace('T', ' ')[0:19]
            t.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{sundial_time}</h1>", unsafe_allow_html=True)

        time.sleep(1)