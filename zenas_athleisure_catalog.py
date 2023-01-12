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
  

colors_column = run_query("select color_or_style from catalog_for_website")
df = pd.DataFrame(colors_column)
#st.write(df)

colors = df[0].values.tolist()
#st.write(colors)

color_option = st.selectbox("Pick a sweatsuit color or style:", list(colors))

product_caption = 'Our warm, comfortable, ' + color_option + ' sweatsuit!'
catalog_table = run_query("select direct_url, price, size_list, upsell_product_desc from catalog_for_website where color_or_style = '"+color_option+"';")
df2 = pd.DataFrame(catalog_table)
st.write(df2)

streamlit.image(df2[0],
                width = 400,
                caption = product_caption
               )

streamlit.write('Price: ', df2[1])
streamlit.write('Sizes available: ', df2[2])
streamlit.write(df2[3])
