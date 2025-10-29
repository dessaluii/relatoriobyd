import streamlit as st

# Configuração da página
st.set_page_config(page_title="Relatório BYD", page_icon="🚗", layout="wide")

# Aplicando fundo branco via CSS
st.markdown("""
    <style>
        body {
            background-color: white;
            color: black;
        }
        h1, h2, h3 {
            color: black;
            text-align: center;
        }
        p {
            text-align: justify;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1>Relatório BYD</h1>", unsafe_allow_html=True)

# Subtítulo: descrição logo abaixo do título
st.markdown("""
<p style="text-align: center; font-size: 20px;">
Build Your Dreams (BYD), se mostra como uma empresa high-tech fabricante de veículos,
a qual desde o começo no setor, possui como objetivo criar inovações tecnológicas
referentes à área automobilística.
</p>
""", unsafe_allow_html=True)

# Tópico 1 - Descrição
st.markdown("<h2>1. Descrição da Organização</h2>", unsafe_allow_html=True)
st.write("""
A BYD é sem dúvidas uma empresa de grande porte (figura no ranking Fortune Global 500)
por ser uma potência global em ascensão, tudo isso baseado também em seu número de funcionários
e um crescimento exponencial em ações e lucro da empresa nos últimos anos. 
Com cerca de 900.000 funcionários no mundo todo, sua receita anual conta com estimadamente
107 bilhões de dólares e um lucro líquido surpreendente de 5,5 bilhões, ultrapassando a Tesla,
empresa concorrente, no ano de 2024, assim tornando-se a maior fabricante no mundo em força de trabalho
na área de P&D (pesquisa e desenvolvimento).
""")

st.markdown("<h3>Já a Descrição da Organização</h3>", unsafe_allow_html=True)
st.write("""
Mostra-se que ela se mantém situada em duas padronizações de setores: secundário e terciário. 
Sendo majoritariamente pertencente ao setor secundário, que tange a indústria, transformação e construção civil,
a fabricação e montagem de carros reconhecidos como de passeio, ônibus e caminhões (veículos de entrega de alto porte),
a empresa se caracteriza como Indústria Automobilística. 
No entanto, por conta de seus valores ligados ao desenvolvimento sustentável, excelência, pragmatismo, paixão e inovação
na promoção da geração de energia, armazenamento eficiente e mobilidade elétrica, a empresa também se enquadra em segundo plano,
no setor terciário ligado a comércio, serviço, investimento na educação e tecnologia.
""")

# Tópico 2 - Ambiente Contextual e Operacional
st.markdown("<h2>2. Ambiente Contextual e Operacional</h2>", unsafe_allow_html=True)
st.write("""
Dentro do contexto de identificação de elementos no ambiente contextual e operacional, fatores como gestão estratégica,
análise de riscos, planejamento de projetos e inteligência empresarial são pilares essenciais para o funcionamento de um projeto.
Contudo, a Build Your Dreams possui e externaliza estes tópicos de forma bem clara, pois atualmente lidera um dos maiores
objetivos tecnológicos do século XXI: a transição energética e a eletrificação veicular. 
Por conta de sua alta participação no setor e integração vertical, a empresa não só utiliza destes recursos, 
mas também os lidera e influencia de acordo com suas necessidades.
""")

# Citação em destaque
st.markdown("""
<p style="text-align: center; font-weight: bold; font-style: italic; font-size: 18px;">
“Inovações tecnológicas para uma vida melhor”
</p>
""", unsafe_allow_html=True)

# Tópico 3 - Cultura Organizacional
st.markdown("<h2>3. Cultura Organizacional e Gestão</h2>", unsafe_allow_html=True)
st.write("""
A cultura organizacional da BYD é tomada por valores como excelência, paixão e inovação, que representam o espírito da empresa
na sua busca por trazer soluções tecnológicas e sustentáveis para o mundo, como é dito em seu slogan.
A missão da organização reforça o compromisso com a criação de produtos e processos que contribuam para uma sociedade
mais limpa e eficiente, onde exista um mundo em que cidades e natureza coexistam de forma equilibrada.

No Brasil, a BYD busca integrar sua cultura global à realidade local. A empresa enfatiza que “a BYD é do Brasil”,
destacando a importância da geração de empregos, da qualificação técnica e da transferência de tecnologia.
Sendo assim, a empresa traz para o Brasil seu produto sem deixar sua essência e diretrizes estratégicas da matriz na China.

A cultura de inovação também influencia o modo de liderança dentro da organização.
A empresa estimula o desenvolvimento de soluções criativas e o uso de tecnologias avançadas,
incentivando equipes a buscar constantemente melhorias em processos e produtos.
Consequentemente, isso promove um ambiente de trabalho dinâmico e colaborativo,
em que a experimentação e a aprendizagem contínua são valorizadas.
""")

# Espaço final + integrantes
st.markdown("""<br><br>""", unsafe_allow_html=True)
st.markdown("""
<h3 style="text-align: center;">Integrantes do Grupo:</h3>
<p style="text-align: center;">
Andressa Rocha, Julia Dias, Marcelo Uchôa, Miguel da Costa, Gabriel Yuzo, Felipe Beltrão, Enzo Velasco e Cássio Azevedo.
</p>
""", unsafe_allow_html=True)
