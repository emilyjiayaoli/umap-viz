import streamlit as st
import psycopg2 # db python lib

st.title("DB")


@st.cache_resource 
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5434'")


conn = get_connection()
cur = conn.cursor() # way to execute python commands

cur.execute("SELECT * FROM TrackLog")
query_results = cur.fetchall()

# Get the column names
column_names = [desc[0] for desc in cur.description]

# We're converting the rows to a list of dictionaries for easier processing
data = [dict(zip(column_names, row)) for row in query_results]

st.write(data)
