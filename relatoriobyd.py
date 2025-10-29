import streamlit as st

# Configuração da página
st.set_page_config(page_title="Relatório BYD", page_icon="🚗", layout="wide")

# Aplicando fundo branco e texto preto via CSS
st.markdown("""
    <style>
        body {
            background-color: white;
            color: black;
        }
        h1 {
            color: black;
            text-align: center;
        }
        h2, h3, p {
            color: black;
            text-align: left;
        }
        p {
            font-size: 18px;
            text-align: justify;
        }
    </style>
""", unsafe_allow_html=True)

# Título principal
st.markdown("<h1>Relatório BYD</h1>", unsafe_allow_html=True)

# Subtítulo centralizado
st.markdown("""
<p style="text-align: center; font-size: 20px;">
Build Your Dreams (BYD), se mostra como uma empresa high-tech fabricante de veículos,
a qual desde o começo no setor, possui como objetivo criar inovações tecnológicas
referentes à área automobilística.
</p>
""", unsafe_allow_html=True)

# --- 1ª Parte ---
st.markdown("<h3><b>A descrição e organização da BYD se caracteriza por</b></h3>", unsafe_allow_html=True)
st.write("""
A BYD é sem dúvidas uma empresa de grande porte (figura no ranking Fortune Global 500)
por ser uma potência global em ascensão, tudo isso baseado também em seu número de funcionários
e um crescimento exponencial em ações e lucro da empresa nos últimos anos.
Com cerca de 900.000 funcionários no mundo todo, sua receita anual conta com estimadamente
107 bilhões de dólares e um lucro líquido surpreendente de 5,5 bilhões, ultrapassando a Tesla,
empresa concorrente, no ano de 2024, assim tornando-se a maior fabricante no mundo em força
de trabalho na área de P&D (pesquisa e desenvolvimento).
""")

# Parágrafo extra
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

# --- Continuação com parágrafo do ambiente operacional (sem o título antigo) ---
st.write("""
Dentro do contexto de identificação de elementos no ambiente contextual e operacional, fatores como gestão estratégica,
análise de riscos, planejamento de projetos e inteligência empresarial são pilares essenciais para o funcionamento de um projeto.
Contudo, a Build Your Dreams possui e externaliza estes tópicos de forma bem clara, pois atualmente lidera um dos maiores
objetivos tecnológicos do século XXI: a transição energética e a eletrificação veicular.
Por conta de sua alta participação no setor e integração vertical, a empresa não só utiliza destes recursos,
mas também os lidera e influencia de acordo com suas necessidades.
""")

# Citação centralizada
st.markdown("""
<p style="text-align: center; font-weight: bold; font-style: italic; font-size: 18px;">
“Inovações tecnológicas para uma vida melhor”
</p>
""", unsafe_allow_html=True)

# --- Cultura Organizacional (mantida igual, mas sem título numerado) ---
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

# --- Nova seção: Estratégia da BYD ---
st.markdown("<h3>BYD tem como estratégia</h3>", unsafe_allow_html=True)
st.write("""
A BYD tem se destacado por sua capacidade de adaptação às condições do mercado brasileiro e às mudanças do ambiente global.
Desde sua chegada ao país em 2022, a empresa vem ampliando sua atuação e consolidando uma presença industrial cada vez mais
relevante no mercado.

O mercado de carros elétricos no Brasil ainda passa por várias dificuldades que tornam o acesso mais complicado para quem
não tem tanto poder de compra. O preço de aquisição continua alto, a infraestrutura de recarga ainda é limitada e as políticas
públicas de incentivo são poucas, o que afasta boa parte dos consumidores. Mesmo assim, a BYD vem mudando esse cenário no país.
A marca se consolidou rapidamente e hoje domina o segmento de veículos 100% elétricos no Brasil, oferecendo opções que vão
desde modelos mais acessíveis, como o Dolphin Mini, até SUVs e híbridos maiores. Em agosto de 2025, a BYD foi responsável
por 74,4% das vendas de carros totalmente elétricos no país, com destaque para os modelos Dolphin Mini, Dolphin e Yuan Pro,
que lideraram o ranking de vendas.

Uma das principais estratégias de adaptação da BYD é o investimento em produção local, atitude a qual favorece diretamente
o Brasil. A empresa lançou a campanha “BYD Quer Conhecer Você” para estimular a nacionalização de componentes e atingir mais
de 50% de peças produzidas no Brasil até 2027. Essa medida reduz a dependência externa e gera empregos (em 2025 foram investidos
R$5,5 bilhões com a meta de gerar, em média, 20 mil empregos diretos e indiretos após a consolidação das operações) e aproxima
a marca das políticas públicas de desenvolvimento industrial sustentável.
""")

# --- Espaço final + Integrantes ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<h3 style="text-align: center;">Integrantes do Grupo:</h3>
<p style="text-align: center;">
Andressa Rocha, Julia Dias, Marcelo Uchôa, Miguel da Costa, Gabriel Yuzo, Felipe Beltrão, Enzo Velasco e Cássio Azevedo.
</p>
""", unsafe_allow_html=True)
