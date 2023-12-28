import streamlit as st 
from streamlit import components
import plotly.express as px
 
st.set_page_config(page_title="Portifolio")


with st.container():
    st.subheader("Meu primeiro site com o streamlit")
    st.title("Dashboard")
    st.write("Informações sobre as eleições")
    st.write("Dashboard Eleições [Clique aqui](https://app.powerbi.com/reportEmbed?reportId=27816bbc-2039-47f7-bf96-44f0d09ea2a6&autoAuth=true&ctid=0d5d7d7a-b007-411f-9929-2091d2189c64)")
    
with st.container():
    st.write("---")
    
    