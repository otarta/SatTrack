import pandas as pd
import streamlit as st 
import json
import requests
import time
import folium
import streamlit_folium


key = st.secrets.key
url = st.secrets.url

mando = {
    'name': 'Mando',
    'lat': st.secrets.mando.lat,
    'lon': st.secrets.mando.lon,
    'alt': st.secrets.mando.alt
}


def above (lat,lon,alt,radius,category):
    response = requests.get(f'{url}/above/{lat}/{lon}/{alt}/{radius}/{category}&apiKey={key}')
    jason = response.json()
    satAbove = jason["above"]
    dataFrame = pd.DataFrame.from_records(satAbove)
    dataFrame.rename(columns={'satlat':'LAT','satlng':'LON'},inplace=True)
    
    return dataFrame

map = st.map(above(mando['lat'],mando['lon'],mando['alt'],45,0))

rerun = st.button("Refresh Map")
if rerun:
    st.rerun()