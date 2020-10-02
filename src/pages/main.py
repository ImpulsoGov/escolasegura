import streamlit as st
import yaml

import utils

def genHeroSection(title1: str, title2: str, subtitle: str,header: bool):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-header" style="font-weight:bold;">corona</span><span class="logo-header" style="font-weight:lighter;">cidades</span></a>"""
    else:
        header = """<br>"""

    st.write(
        f"""
        <div class="container">
            {header}
            <div>
                <span class="hero-container-product primary-span">{title1}</span>
                <br>
                <span class="hero-container-product primary-span">{title2}</span>
                <br>
                <span class="hero-container-subtitle dark-span">{subtitle}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

def genSelectBox():
    user_input = dict()
    states = ("Todos","UF1", "UF2")
    options = list(range(len(states)))

    #user_input["state_name"] = st.selectbox("Estado", options, format_func=lambda x: states[x])
    #user_input["city_name"] = st.selectbox("Município", [])
    #user_input["teaching_level"] = st.selectbox("Nível de ensino", [])

    st.write(
        f"""
        <div class="container container-three-columns main-padding">
            <p>Selectbox estado</p>
            <p>Selectbox município</p>
            <p>Selectbox nível de ensino</p>
        </div>
        """,
        unsafe_allow_html=True
    )

def genMainContainer():
    st.write(
        f"""
        <div class="container container-two-columns minor-padding">
            <div class="text-intro">
                <div class="text-title-section">
                    Como retomar as aulas na minha cidade?
                </div>
                <div class="minor-padding">
                    <p>Enquanto ainda estamos em situação de crise, é possível uma retomada gradual  de 
                    momentos presenciais para alunos da sua rede. Mas é preciso priorizar: quero retornar 
                    o máximo de alunos possível mesmo que só alguns dias por semana cada, ou uma quantidade 
                    fixa de alunos em séries terminais pelo máximo de tempo por semana possivel?</p>
                    <p>Explore abaixo diferentes cenários de retomada, calculados <b>usando dados abertos</b> de 
                    educação da sua cidade. Para isso, adotamos as seguintes restrições sanitárias, apontados 
                    como boas práticas para reduzir o risco de contágio de Covid-19 no sistema hospitalar:</p>
                    <ul>
                    <li>no máximo X alunos por metro quadrado</li>
                    <li>Cada grupo de alunos ocupa uma sala por vez, com 1 professor responsável</li>
                    <li>É possível ter dois turnos por dia em cada equipamento escolar</li>
                    </ul>
                </div>
            </div>
            <div class="vis-intro">
                 <div>
                    <img src="https://via.placeholder.com/300">
                    <b class="text-subdescription">estimativas de casos e subnotificação de Covid-19 + 
                    distanciamento social no município (todos dados diários)</b>
                </div>
                <div class="container-two-columns-nested main-padding bold">
                    <div>
                        <span style="font-size: 64px; color:#3E758A">5</span>
                        <br>
                        casos por 100k habitantes
                    </div>
                    <br><br>
                    <div>
                        <span>A situação da doença está estabilizando em moderado no seu município.<span>
                        <br><br>
                        <span class = "uppercase bold">
                            SEU NÍVEL DE ALERTA É <span class = "dark-span" style-"font-size: 42px;">MODERADO</span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genModelContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Implementando um modelo híbrido </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genActualSituationContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Situação atual da rede </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genSimulationContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Os diferentes cenários para sua retomada </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genReturnContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Retorno na prática </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    utils.localCSS("src/style.css")
    genHeroSection(
        title1="Escola",
        title2="Possível",
        subtitle="{subtítulo}",
        header=True,
    )
    genSelectBox()
    genMainContainer()
    genModelContainer()
    genActualSituationContainer()
    genSimulationContainer()
    genReturnContainer()
    

if __name__ == "__main__":
    main()