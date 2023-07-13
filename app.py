# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Load your data (placeholder until your database is ready)
# This will create a DataFrame with 1000 samples, each with a 3D point and a class ID.
def load_data():
    np.random.seed(0)
    data = np.random.rand(1000, 3)  # Random 3D points
    labels = np.random.randint(0, 5, 1000)  # Random class IDs
    df = pd.DataFrame(data, columns=["x", "y", "z"])
    df["class_id"] = labels
    return df

df = load_data()

# Streamlit app
def main():
    st.title("3D Embeddings Visualization")

    # User input for class IDs
    class_ids = st.multiselect('Choose class IDs', df['class_id'].unique())

    # Modify the DataFrame based on user selection
    if class_ids:
        df_selected = df[df['class_id'].isin(class_ids)]
        df_not_selected = df[~df['class_id'].isin(class_ids)]
    else:
        df_selected = df
        df_not_selected = pd.DataFrame(columns=["x", "y", "z", "class_id"])

    # Create 3D scatter plot
    fig = px.scatter_3d(df_not_selected, x='x', y='y', z='z', color='class_id',
                        opacity=0.5, title="Embeddings")

    fig.add_trace(px.scatter_3d(df_selected, x='x', y='y', z='z', color='class_id',
                        opacity=1).data[0])  # Add selected points with full opacity

    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
