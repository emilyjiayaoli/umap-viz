import streamlit as st
import psycopg2
from psycopg2 import sql
import folium
from streamlit_folium import st_folium


@st.cache_resource
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5434'")


conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM TrackLog")
query_results = cur.fetchall()

# Get the column names
column_names = [desc[0] for desc in cur.description]

# We're converting the rows to a list of dictionaries for easier processing
data = [dict(zip(column_names, row)) for row in query_results]

st.title('TrackLog CRUD App')

# Initialize a map centered at the first location
m = folium.Map(location=[data[0]['latitude'], data[0]['longitude']], zoom_start=6)

# Add a marker for each location
for row_data in data:
    folium.Marker([row_data['latitude'], row_data['longitude']], popup=row_data['mmsi'], tooltip=row_data['mmsi']).add_to(m)

# Display the map
st_folium(m, width=1024)

for row_data in data:
    cols = st.columns(6)
    logtime = cols[0].text(row_data['logtime'])
    mmsi = cols[1].text_input('MMSI', row_data['mmsi'])
    latitude = cols[2].text_input('Latitude', row_data['latitude'])
    longitude = cols[3].text_input('Longitude', row_data['longitude'])
    if cols[4].button('Update', key=f"d-{row_data['logtime']}"):
        cur.execute(
            sql.SQL("UPDATE TrackLog SET mmsi=%s, latitude=%s, longitude=%s WHERE logtime=%s"),
            (mmsi, latitude, longitude, row_data['logtime'])
        )
        conn.commit()
        cur.close()
        st.experimental_rerun()

    if cols[5].button('Delete', key=f"r-{row_data['logtime']}"):
        cur.execute(
            sql.SQL("DELETE FROM TrackLog WHERE logtime=%s"),
            (row_data['logtime'],)
        )
        conn.commit()
        cur.close()
        st.experimental_rerun()

st.write('Insert new row:')
insert_cols = st.columns(5)
new_logtime = insert_cols[0].text_input('Logtime')
new_mmsi = insert_cols[1].text_input('MMSI')
new_latitude = insert_cols[2].text_input('Latitude')
new_longitude = insert_cols[3].text_input('Longitude')
if insert_cols[4].button('Insert'):
    cur.execute(
        sql.SQL("INSERT INTO TrackLog (logtime, mmsi, latitude, longitude) VALUES (%s, %s, %s, %s)"),
        (new_logtime, new_mmsi, new_latitude, new_longitude)
    )
    conn.commit()
    cur.close()
    st.experimental_rerun()
