import streamlit as st
from PIL import Image

st.title("🔬 Projeto de Pesquisa")
st.markdown('---')

st.subheader("A dimensão formativa da integridade em pesquisa de Educação (2023 - Atual)")

st.markdown("""
**Situação:** Em andamento  
**Natureza:** Pesquisa  
**Coordenador:** Victor Sporkens Viana  
**Grupo de Pesquisa:** GEPHEB (Grupo de Estudo e Pesquisa em Ética, Política e História da Educação Brasileira – CNPq)

Este projeto investiga como a integridade em pesquisa é abordada na formação de pesquisadores em Educação, especialmente no contexto ético das relações entre pesquisador e participantes (adultos, jovens ou crianças). A pesquisa adota uma metodologia qualitativa, combinando **revisão de literatura** e **grupo focal** com estudantes de graduação, mestrado e doutorado.

**Objetivo:** Desenvolver a consciência de que a integridade vai além das normas legais e deve considerar a alteridade e a devolutiva ética da pesquisa.

**Alunos envolvidos:**  
- Graduação: 3  
- Mestrado: 1  
- Doutorado: 4

**Principais integrantes:**  
- Sônia Aparecida Siquelli  
- Caroline Ferreira do Amaral  
- Beatriz da Silva Correia  
- Luis Roberto Ramos de Sá Filho  
- Fabiola Santini Takayama  
- Ilca dos Santos Freitas  
- Augusto Fagundes dos Santos
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
