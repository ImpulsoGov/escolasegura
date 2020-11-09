import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout

from model.get_school_return_data import entrypoint

import pages.planContainer as pc
import pages.simulationContainer as sc
import pages.prepareContainer as prc
import pages.monitorContainer as mc
import pages.referencesContainer as rc
import pages.footerContainer as fc


def genHeroSection(title1: str, title2: str, subtitle: str, header: bool):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-header" style="font-weight:bold;">corona</span><span class="logo-header" style="font-weight:lighter;">cidades</span> <br></a>"""
    else:
        header = """<br>"""

    st.write(
        f"""
        <div class="container">
            {header}
        <div class="grid-container-header">
            <div class="div1-head">
                <img class="img-logo-header" src="https://i.imgur.com/SJHwG4Z.png">
            </div>
            <div class="div2-head">
                <span class="hero-container-product main-blue-span">{title1}</span>
                <br>
                <span class="hero-container-product main-blue-span">{title2}</span>
                <br><br>
            </div>
            <div class="div3-head">
                <span class="hero-container-question">
                Controle a Covid-19 e promova aulas presenciais seguras na rede pública.
                </span>
            </div>
            <br>
        </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def read_data(country, config, endpoint):

    if os.getenv("IS_LOCAL") == "TRUE":
        api_url = config[country]["api"]["local"]
    else:
        api_url = config[country]["api"]["external"]

    url = api_url + endpoint

    print("\nLoad data from:", url)
    df = pd.read_csv(url)
    return df


@st.cache(suppress_st_warning=True)
def get_data(config):
    df = read_data("br", config, "br/cities/safeschools/main")
    return df


def genSelectBox(df, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="text-title-section"> Selecione sua rede </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4 = st.beta_columns([0.3, 0.5, 0.5, 1])

    with col1:
        session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
    with col2:
        options_city_name = utils.filter_place(
            df, "city", state_id=session_state.state_id
        )
        options_city_name = pd.DataFrame(data=options_city_name, columns=["city_name"])
        x = int(
            options_city_name[options_city_name["city_name"] == "Todos"].index.tolist()[
                0
            ]
        )
        session_state.city_name = st.selectbox("Município", options_city_name, index=x)
    with col3:
        options_adiminlevel = utils.filter_place(
            df,
            "administrative_level",
            state_id=session_state.state_id,
            city_name=session_state.city_name,
        )
        options_adiminlevel = pd.DataFrame(
            data=options_adiminlevel, columns=["adiminlevel"]
        )
        y = int(
            options_adiminlevel[
                options_adiminlevel["adiminlevel"] == "Todos"
            ].index.tolist()[0]
        )
        session_state.administrative_level = st.selectbox(
            "Nível de Administração", options_adiminlevel, index=y
        )
    with col4:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )


def main(session_state):
    utils.localCSS("style.css")
    genHeroSection(
        title1="Escola",
        title2="Segura",
        subtitle="{descrição}",
        header=True,
    )
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    data = get_data(config)
    genSelectBox(data, session_state)

    # to keep track on dev
    print("PLACE SELECTION: \n", 
        "\n=> UF: ", session_state.state_id,
        "\n=> CITY: ", session_state.city_name,
        "\n=> ADM: ", session_state.administrative_level, 
    )
    Botao1 = False
    Botao2 = False
 
    coluna1, coluna2, espaco = st.beta_columns([0.4, 0.4, 0.1])
    with coluna1:
        st.write(
            f"""
            <div class="container" style="min-height: 150px;">
            <div class="text-title-section minor-padding ">Como organizo a reabertura da minha rede escolar?</div>
            <div class="minor-padding">
                1.0 - Como checar o preparo da minha secretaria e rede para a reabertura presencial?<br>
                2.0 - Quais são as principais recomendações sanitárias e protocolos para retomada?<br>
                3.0 - Quais protocolos seguir de acordo com o nível de alerta da minha região?<br>
            </div></br>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Veja como orientar reabertura"):
            Botao1 = True
    with coluna2:
        st.write(
            f"""
            <div class="container" style="min-height: 150px;">
            <div class="text-title-section minor-padding">Como faço a gestão das unidades escolares?</div>
            <div class="minor-padding">
                1.0 - Como verificar e garantir condições para reabertura de escolas por meio de gestores escolares?<br>
                2.0 - O que fazer quando um caso for confirmado em uma unidade escolar?<br>
                3.0 - Como acompanhar a notificação de casos em unidades escolares e orientar ações?<br>
            </div></br>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Veja como gerenciar unidades escolares"):
            Botao2 = True
    with espaco:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )
    if Botao1 == True:
        pc.genPlanContainer(data, config, session_state)
    if Botao2 == True:
        prc.genPrepareContainer()
        mc.genMonitorContainer()
    st.write(
            f"""
    <div class="container main-padding">
        <br>
    </div>
    """,
        unsafe_allow_html=True,
    )
    rc.genReferencesContainer()
    fc.genFooterContainer()


if __name__ == "__main__":
    main()
