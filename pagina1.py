import streamlit as st
from PIL import Image
import webbrowser

st.title('Trajetória e formações :mortar_board::')
st.markdown("---")


st.subheader("Mestrado em Educação (2023–2024)")
st.markdown("""
**Universidade São Francisco (USF)**  
Título da dissertação: *O silenciamento na formação política do ensino médio na visão dos estudantes.*  
Orientadora: Sônia Aparecida Siquelli  
Bolsista CAPES  
**Palavras-chave**: Educação, Formação Política, Ensino Médio, Grupo Focal  
**Grande área**: Ciências Humanas  
**Setor de atividade**: Educação
""")

st.subheader("Graduação em Geografia (2014–2021)")
st.markdown("""
**Universidade Estadual de Campinas (UNICAMP)**  
**Monografia (2020)**: *Variabilidade temporal com ênfase em eventos de precipitação pluvial excessiva, tendências e impactos no município de Itatiba*  
Orientadora: Ana Maria Heuminski de Avila
""")

st.subheader("Curso Técnico em Informática (2011–2012)")
st.markdown("""
**ETE Rosa Perrone Scavone**  
Concomitante ao Ensino Médio
""")

def load_css():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary-color: #1a365d;
                --secondary-color: #2d547d;
                --accent-color: #38bdf8;
                --text-light: #f8fafc;
                --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }


            .project-card {
                background: white;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 0, 0, 0.1);
            }


            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }


            .experience-item {
                padding: 1.5rem;
                background: white;
                border-radius: 10px;
                box-shadow: var(--shadow);
                margin-bottom: 1.5rem;
                transition: all 0.3s ease;
            }


            .experience-item:hover {
                transform: translateY(-3px);
            }
        </style>
    """, unsafe_allow_html=True)

with st.sidebar:
        st.image("Vitor.png", width=130)
        st.markdown("""
        <div style='text-align: center;'>
            <h2>Victor Sporkens</h2>
            <p style='color: var(--accent-color);'>🌎🚀Professor & Pesquisador</p>
        </div>
        """, unsafe_allow_html=True)

        with st.expander("📫 contato", expanded=True):
            st.markdown("""
                    <p><i class = "fas fa-map-marker-alt"></i> Itatiba, São Paulo</p>
                    <p><i class = "fas fa-phone"></i> +55 11 97323-6793</p>
                    <p><i class = "fas fa-envelope"></i> victor.viana18@etec.sp.gov.br</p>
                    
            """, unsafe_allow_html=True)
