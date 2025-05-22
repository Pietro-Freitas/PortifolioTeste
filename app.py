import streamlit as st
from PIL import Image
import webbrowser

st.set_page_config(page_title='Portifolio.py', layout='wide', initial_sidebar_state="expanded")

pagina = st.sidebar.selectbox('Escolha uma página:', ['Home', 'Página 1', 'Página 2'])

paginas = {
    'Home': 'home.py',
    'Página 1': 'pagina1.py',
    'Página 2': 'pagina2.py'
}


with open(paginas[pagina], 'r', encoding='utf-8') as arquivo:
    exec(arquivo.read())
