import pandas as pd
import streamlit as st 
import json
import requests
import arrow 


key = st.secrets.key
url = st.secrets.url

mando = {
    'name': 'Mando',
    'lat': st.secrets.mando.lat,
    'lon': st.secrets.mando.lon,
    'alt': st.secrets.mando.alt
}

st.title = "NOAA Passes"

def radioPass(id,lat,lon,alt,days,elev):
    response = requests.get(f'{url}/radiopasses/{id}/{lat}/{lon}/{alt}/{days}/{elev}&apiKey={key}')
    jason = response.json()
    return jason

def noaaPasses():
     noaa18 = radioPass(28654,mando['lat'],mando['lon'],mando['alt'],10,0)
     noaa19 = radioPass(33591,mando['lat'],mando['lon'],mando['alt'],10,0)
     noaa15 = radioPass(25338,mando['lat'],mando['lon'],mando['alt'],10,0)
     
     passes18 = noaa18['passes']
     passes19 = noaa19['passes']
     passes15 = noaa15['passes']
     
     df18 = pd.DataFrame.from_records(passes18)
     df18['ID'] = "NOAA 18"
     df19 = pd.DataFrame.from_records(passes19)
     df19['ID'] = "NOAA 19"
     df15 = pd.DataFrame.from_records(passes15)
     df15['ID'] = "NOAA 15"
     
     dfMain = pd.concat([df18,df19,df15])  
     
     start = dfMain['startUTC']
     max = dfMain['maxUTC']
     end = dfMain['endUTC']
     newStart = start.apply(time)
     newMax = max.apply(time)
     newEnd = end.apply(time)
     dfMain['startUTC'] = newStart
     dfMain['maxUTC'] = newMax
     dfMain['endUTC'] = newEnd
     
     st.write(dfMain)
     return 

def time (x):
    return arrow.get(x).to("US/Eastern").to("US/Eastern").format("YYYY-MM-DD HH:mm:ss")






noaaPasses()

