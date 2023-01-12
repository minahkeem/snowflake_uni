import streamlit as st
import pandas as pd
import snowflake.connector

#testing header on streamlit app
st.header("Zena's Amazing Athleisure Catalog")
conn = snowflake.connector.connect(**st.secrets["snowflake"])
conn.close()
