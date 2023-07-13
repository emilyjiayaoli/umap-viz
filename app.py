import streamlit as st
import plotly.express as px
import psycopg2
import pandas as pd

@st.cache_resource
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5435'")

def load_data(conn, selection_query):
    df = pd.read_sql(selection_query, conn)
    return df

# Streamlit app
def main():
    st.title("3D Embeddings Visualization")
    conn = get_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT DISTINCT camid FROM UMAPTable")
    camid_options = sorted([row[0] for row in cur.fetchall()])
    cur.execute("SELECT DISTINCT pid FROM UMAPTable")
    pid_options = sorted([row[0] for row in cur.fetchall()])
    
    # User input for camids and pids
    camids = st.multiselect('Choose camids', camid_options)
    pids = st.multiselect('Choose pids', pid_options)

    selection_query = 'SELECT * FROM UMAPTable'
    
    if camids:
        camids_str = ','.join(["'" + str(e) + "'" for e in camids])  # Treat camids as strings
        selection_query += f' WHERE camid IN ({camids_str})'
    
    if pids:
        pids_str = ','.join(["'" + str(e) + "'" for e in pids])  # Treat pids as strings
        selection_query += (' AND' if 'WHERE' in selection_query else ' WHERE') + f' pid IN ({pids_str})'
    
    df = load_data(conn, selection_query)

    # Create 3D scatter plot
    fig = px.scatter_3d(df, x='x', y='y', z='z', color='pid', opacity=1, color_continuous_scale='RdBu', title="Embeddings")
    fig.update_layout(width=800, height=600)
    fig.update_traces(marker=dict(size=8))

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
