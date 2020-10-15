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
        <div class="container row">
            <div class="col">
                {header}
                <span class="hero-container-product primary-span">{title1}</span>
                <br>
                <span class="hero-container-product primary-span">{title2}</span>
                <br><br>
                <span class="hero-container-subtitle dark-span">{subtitle}</span>
                <br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question primary-span">Como preparar a minha rede escolar para um retorno presencial seguro?</span>
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
        <div class="container main-padding">
            <div class="text-title-section"> Selecione sua rede </div>
            <div class="row"> 
                <p class="col">Selectbox estado</p>
                <p class="col">Selectbox município</p>
                <p class="col">Selectbox nível de ensino</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genPlanContainer():
    st.write(
        f"""
        <div class="container main-padding">
           <div class="title-section">Planeje </div>
            <div><br></div>
        </div>
        """,
        unsafe_allow_html=True
    )
def genSimulationContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Simule o retorno </div>
            <div><br></div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genPrepareContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Prepare </div>
            <div><br></div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genMonitorContainer():
    st.write(
        f"""
        <div class="container">
            <div class="title-section main-padding"> Monitore </div>
            <div><br></div>
        </div>
        """,
        unsafe_allow_html=True
    )



def genFooterContainer():
    st.write(
        f"""
        <div class="container">
            <div class="text-title-section main-padding"> Realizado por </div>
            <br>
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
    genPlanContainer()
    genSimulationContainer()
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()
    

if __name__ == "__main__":
    main()