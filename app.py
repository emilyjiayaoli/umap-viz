# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import psycopg2

@st.cache(hash_funcs={psycopg2.extensions.connection: id})
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5434'")

def load_data():
    conn = get_connection()
    df = pd.read_sql('SELECT * FROM UMAPTable', conn)
    df[['x', 'y', 'z']] = df[['x', 'y', 'z']].apply(pd.to_numeric)
    df[['camid', 'pid']] = df[['camid', 'pid']].astype(int)
    return df

df = load_data()

# Streamlit app
def main():
    st.title("3D Embeddings Visualization")

    # User input for camids and pids
    camids = st.multiselect('Choose camids', df['camid'].unique())
    pids = st.multiselect('Choose pids', df['pid'].unique())

    # Modify the DataFrame based on user selection
    if camids:
        df_selected_camid = df[df['camid'].isin(camids)]
    else:
        df_selected_camid = df

    if pids:
        df_selected_pid = df[df['pid'].isin(pids)]
    else:
        df_selected_pid = df

    df_selected = pd.merge(df_selected_camid, df_selected_pid)

    df_not_selected = df.drop(df_selected.index)

    # Create 3D scatter plot
    fig = px.scatter_3d(df_not_selected, x='x', y='y', z='z', color='pid',
                        opacity=0.05, color_continuous_scale='RdBu', title="Embeddings")
    fig.update_layout(width=800, height=600)

    fig.add_trace(px.scatter_3d(df_selected, x='x', y='y', z='z', color='pid',
                        opacity=1, color_continuous_scale='RdBu').data[0])  # Add selected points with full opacity
    fig.update_layout(width=800, height=600)

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
