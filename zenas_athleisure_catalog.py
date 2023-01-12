import streamlit as st
import pandas as pd
import snowflake.connector

#testing header on streamlit app
st.header("Zena's Amazing Athleisure Catalog")
conn = snowflake.connector.connect(**st.secrets["snowflake"])
cur = conn.cursor()
cur.execute("SELECT * FROM CATALOG_FOR_WEBSITE")
data_table = cur.fetchall()
st.dataframe(data_table)
