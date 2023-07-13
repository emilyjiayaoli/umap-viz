import csv
import psycopg2
import streamlit as st


<<<<<<< HEAD
# @st.cache_resource 
=======
#@st.cache_resource 
>>>>>>> dea813e (fixes)
def get_connection():
    return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='hackathon' port='5435'")

def csv_to_postgresql(csv_filename, table_name):
    # Connect to PostgreSQL database
    conn = get_connection() #psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # Read CSV file
    with open(csv_filename, 'r') as f:
        reader = csv.reader(f)

        # Get the column names from the first line of the CSV
        columns = next(reader)

        # Create a SQL table with these columns (all columns are treated as text)
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        cursor.execute(f"CREATE TABLE {table_name} ({', '.join([f'{column} text' for column in columns])})")

        # Insert the data into the SQL table
        for row in reader:
            cursor.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['%s' for _ in row])})", row)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage
csv_to_postgresql(csv_filename='umap.csv', table_name='UMAPTable')
