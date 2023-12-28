import streamlit as st 
from streamlit import components
import streamlit as st
import streamlit_authenticator as stauth

# Autenticação do usuário
credentials_file = 'credentials.yaml'  # Substitua pelo caminho do seu arquivo YAML
if not stauth.authenticate(credentials_file):
    st.stop()

 
st.set_page_config(page_title="Portifolio")


with st.container():
    st.subheader("Portifólio")
    st.title("Dashboard - Marcio")
    
    
with st.container():
    st.write("---")
    st.write("Informações sobre as eleições")
    st.write("Dashboard Eleições [Clique aqui](https://app.powerbi.com/reportEmbed?reportId=27816bbc-2039-47f7-bf96-44f0d09ea2a6&autoAuth=true&ctid=0d5d7d7a-b007-411f-9929-2091d2189c64)")

with st.container():
    st.write("---")
