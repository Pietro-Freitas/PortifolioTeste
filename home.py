import streamlit as st
from PIL import Image

imagem_local = "Vitor.png"
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

def main():
    load_css()
    
    with st.sidebar:
        st.image("https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPO/main/Vitor.png", width=130)
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

    st.title('Victor Sporkens')
    st.subheader('Educador | Pesquisador')
    st.markdown("---")
    st.subheader(":computer: Sobre mim")
    st.write("Mestre em Educação pela Universidade São Francisco - campus Itatiba - pelo Programa de Pós-Graduação Stricto Sensu em Educação, com financiamento CAPES.Graduado em Geografia (Bacharelado) pela Universidade Estadual de Campinas (2019), e licenciado em Geografia na mesma instituição (2021).Formado também no curso técnico de informática pela ETE Rosa Perrone Scavone (2012). Integrante do Grupo de Pesquisa em Ética, Política e Historia da Educação Brasileira - GEPHEB/CNPQ-USF. Professor na rede pública estadual de São Paulo, lecionando aulas de Geografia.Possui experiência na área de Geociências, com ênfase em Climatologia Geográfica e também em Administração Pública.Além de prática na área de computação, principalmente no uso básico de linguagens C, C++, e linguagem R.")
    st.subheader('Informações')


    col1, col2 = st.columns(2)
    with col1:
        st.header(':mortar_board: Formação:')
        st.markdown("""
    - **Mestrado em Política Científica e Tecnológica** – Universidade Estadual de Campinas (UNICAMP)  
    • Dissertação: *"Uma reflexão sobre o papel das plataformas digitais de mobilidade urbana na promoção da sustentabilidade"*  
    • Orientadora: Profª. Dra. Flávia Consoni

    - **Bacharelado e Licenciatura em Geografia** – Universidade Estadual de Campinas (UNICAMP)

    - **Técnico em Informática** – ETEC Rosa Perrone Scavone (Itatiba/SP)
    """)

    with col2:
        st.header(' 🛠️ Habilidades técnicas:')
        st.markdown("""
    - Análise de políticas públicas em ciência, tecnologia e inovação  
    - Pesquisa qualitativa e quantitativa  
    - Desenvolvimento de projetos educacionais e tecnológicos  
    - Plataformas digitais de mobilidade urbana  
    - Sistemas de informação geográfica (SIG)  
    - Redação acadêmica e produção científica  
    - Comunicação interdisciplinar e metodologias ativas  
    """)
        
        
        
if __name__ == '__main__':
    main()
