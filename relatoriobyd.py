import streamlit as st

# Centralizar texto com HTML
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Relatório BYD</h1>
        <p><b>Integrantes do Grupo:</b><br>
        Andressa Rocha, Julia Dias, Marcelo Uchôa, Miguel da Costa, Gabriel Yuzo, 
        Felipe Beltrão, Enzo Velasco e Cássio Azevedo</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Centralizar os títulos das seções
st.markdown(
    """
    <div style="text-align: center;">
        <h3>1. Descrição da Organização</h3>
        <h3>2. Ambiente Contextual e Operacional</h3>
        <h3>3. Cultura Organizacional e Gestão</h3>
        <h3>4. Estratégias de Adaptação ao Ambiente</h3>
        <h3>5. Mapa de Stakeholders</h3>
    </div>
    """,
    unsafe_allow_html=True
)
