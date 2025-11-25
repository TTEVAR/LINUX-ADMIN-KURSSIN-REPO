import streamlit as st
import mysql.connector
import pandas as pd

st.markdown(
        """
        <style>
        .stApp {
                background-color: #690202;
        }
        </style>
        """,
        unsafe_allow_html=True
)

# Fetch weather data from MySQL
def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="Yup#2025",
        database="weather_db"
    )
    query = "SELECT * FROM weather_data;"  # modify table name
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Fetch bored data from MySQL
def fetch_bored():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="Yup#2025",
        database="exampledb"
    )
    df = pd.read_sql("SELECT * FROM bored_data ORDER BY timestamp DESC LIMIT 10", conn)
    conn.close()
    return df

# Streamlit UI
st.title("Truly the most riveting of statistics right here")
st.write("The gracious gods at MYSQL have provided this new earth-shattering data on...")

# Weather data
df = fetch_data()
st.dataframe(df)
# Bored data
df_bored = fetch_bored()
st.subheader("You bored?.... here ya go anyway.")
st.dataframe(df_bored)

st.markdown("Cozy winter vibes y'know")
st.video("https://www.youtube.com/watch?v=qjBjal2uPrk")
