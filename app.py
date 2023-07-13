# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Load your data (placeholder until your database is ready)
# This will create a DataFrame with 1000 samples, each with a 3D point, a camid, and a pid.
def load_data():
    np.random.seed(0)
    data = np.random.rand(1000, 3)  # Random 3D points
    camids = np.random.randint(0, 5, 1000)  # Random camids
    pids = np.random.randint(0, 5, 1000)  # Random pids
    df = pd.DataFrame(data, columns=["x", "y", "z"])
    df["camid"] = camids
    df["pid"] = pids
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
                        opacity=0.1, color_continuous_scale='RdBu', title="Embeddings")
    fig.update_layout(width=800, height=600)

    fig.add_trace(px.scatter_3d(df_selected, x='x', y='y', z='z', color='pid',
                        opacity=1, color_continuous_scale='RdBu').data[0])  # Add selected points with full opacity
    fig.update_layout(width=800, height=600)

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
