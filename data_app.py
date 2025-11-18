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
# Fetch data from MySQL
def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="Yup#2025",
        database="exampledb"
    )
    query = "SELECT * FROM v3_data;"  # modify table name
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Streamlit UI
st.title("Truly the most riveting of statistics right here")
st.write("The gracios gods at MYSQL have provided this new earth shattering data on...")

df = fetch_data()
st.dataframe(df)

st.bar_chart(df.select_dtypes(include=['int', 'float']))

st.markdown("Cozy winter vibes y'know")
st.video("https://www.youtube.com/watch?v=qjBjal2uPrk")
