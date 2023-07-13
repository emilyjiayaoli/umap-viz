import streamlit as st
import plotly.express as px
import psycopg2
import pandas as pd

@st.cache_resource(hash_funcs={psycopg2.extensions.connection: id})
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5434'")

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
    pid_options = sorted([int(row[0]) for row in cur.fetchall()])  # Convert pids to integers for sorting
    
    # User input for camids and pids
    pids = st.multiselect('Choose pids', pid_options)
    camids = st.multiselect('Choose camids', camid_options)

    selection_query = 'SELECT * FROM UMAPTable'
    
    if camids:
        camids_str = ','.join(["'" + str(e) + "'" for e in camids])  # Treat camids as strings
        selection_query += f' WHERE camid IN ({camids_str})'
    
    if pids:
        pids_str = ','.join(["'" + str(e) + "'" for e in pids])  # Treat pids as strings
        selection_query += (' AND' if 'WHERE' in selection_query else ' WHERE') + f' pid IN ({pids_str})'

    # Sort the data by 'pid' in the SQL query
    selection_query += ' ORDER BY pid'
    
    df = load_data(conn, selection_query)

    # Create 3D scatter plot
    fig = px.scatter_3d(df, x='x', y='y', z='z', color='pid', opacity=1, color_continuous_scale='RdBu', title="Embeddings")
    fig.update_layout(width=800, height=600)

    # Define the limits of your axes
    x_range = [-15, 20]  # Change these values to your preferred limits
    y_range = [-15, 20]
    z_range = [-15, 20]

    # Fix the axes
    fig.update_xaxes(range=x_range)
    fig.update_yaxes(range=y_range)
    fig.update_scenes(xaxis=dict(range=z_range))  # For 3D scatter plots, use update_scenes instead of update_zaxes

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
