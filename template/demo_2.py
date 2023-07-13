import streamlit as st

st.title("Input")

cols = st.columns(6)
logtime = cols[0].text_input('logtime', '123')
mmsi = cols[1].text_input('MMSI', '123456789')
latitude = cols[2].text_input('Latitude', '35')
longitude = cols[3].text_input('Longitude', '-76')

if cols[4].button('Print'):
    st.write(f"{logtime}, {mmsi}, {latitude}, {longitude}")