import streamlit as st
import pandas as pd
import snowflake.connector

#testing header on streamlit app
st.header("Zena's Amazing Athleisure Catalog")

conn = snowflake.connector.connect(**st.secrets["snowflake"])


@st.experimental_memo(ttl=600)
def run_query(query):
  with conn.cursor() as cur:
    cur.execute(query)
    return cur.fetchall()
  

catalog_table = run_query("select * from catalog_for_website")
df = pd.DataFrame(catalog_table)
st.write(df)

colors = df[0].values.tolist()
#st.write(colors)

color_options = st.selectbox("Pick a sweatsuit color or style:", list(colors))
