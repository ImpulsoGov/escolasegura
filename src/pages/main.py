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
import pages.specialistContainer as spc


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
                <a href="" class="logo-link">
                <span class="hero-container-product main-blue-span">{title1}</span>
                <div class="br-hero"></div>
                <span class="hero-container-product main-blue-span">{title2}</span>
                </a>
            </div>
        </div>
        </div><br>
        <div class="hero-container-subtitle">
            Salas <b>abertas</b> para estudantes<br>Portas <b>fechadas</b> para a Covid-19
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
    df = read_data("br", config, "br/cities/safeschools/main").replace(
        {"Fundamental I": "Fund. I", "Fundamental II": "Fund. II"}
    )
    return df


def genSelectBox(df, session_state):
    st.write(
        f"""
        <div class="main-padding">
            <div class="subtitle-section"> Selecione sua rede </div>
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
            <br><br>
        </div>
        """,
            unsafe_allow_html=True,
        )


def main(session_state):
    if os.getenv("IS_DEV") == "FALSE":
        #  ==== GOOGLE ANALYTICS SETUP ====
        GOOGLE_ANALYTICS_CODE = os.getenv("GOOGLE_ANALYTICS_CODE")
        if GOOGLE_ANALYTICS_CODE:
            import pathlib
            from bs4 import BeautifulSoup

            TAG_MANAGER = """
                function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
                new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
                j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
                'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
                })(window,document,'script','dataLayer','GTM-5ZZ5F66');
                """
            GA_JS = (
                """
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '%s');
            """
                % GOOGLE_ANALYTICS_CODE
            )
            index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
            soup = BeautifulSoup(index_path.read_text(), features="lxml")
            if not soup.find(id="google-analytics-loader"):
                script_tag_import = soup.new_tag(
                    "script",
                    src="https://www.googletagmanager.com/gtag/js?id=%s"
                    % GOOGLE_ANALYTICS_CODE,
                )
                soup.head.append(script_tag_import)
                script_tag_loader = soup.new_tag("script", id="google-analytics-loader")
                script_tag_loader.string = GA_JS
                soup.head.append(script_tag_loader)
                script_tag_manager = soup.new_tag("script", id="google-tag-manager")
                script_tag_manager.string = TAG_MANAGER
                soup.head.append(script_tag_manager)
                script_tag_manager_body = soup.new_tag(
                    "script",
                    src="https://www.googletagmanager.com/gtm.js?id=GTM-5ZZ5F66"
                )
                soup.head.append(script_tag_manager_body)
                index_path.write_text(str(soup))
        # ====
    utils.localCSS("style.css")
    st.write(
        """<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5ZZ5F66" height="0" width="0" style="display:none;visibility:hidden"></iframe>""",
        unsafe_allow_html=True,
    )
    genHeroSection(
        title1="Escola", title2="Segura", subtitle="{descrição}", header=True,
    )
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    data = get_data(config)
    genSelectBox(data, session_state)

    # to keep track on dev
    print(
        "PLACE SELECTION: \n",
        "\n=> UF: ",
        session_state.state_id,
        "\n=> CITY: ",
        session_state.city_name,
        "\n=> ADM: ",
        session_state.administrative_level,
    )

    coluna1, coluna2, espaco = st.beta_columns([0.4, 0.4, 0.1])
    with coluna1:
        protocol_icon = utils.load_image("imgs/plan_protocol_icon.png")
        steps_icon = utils.load_image("imgs/plan_steps_icon.png")
        ruler_icon = utils.load_image("imgs/plan_ruler_icon.png")
        simulation_icon = utils.load_image("imgs/simulation_main_icon.png")

        st.write(
            f"""
            <div class="container" style="min-height: 150px;"><br>
                <div class="text-title-section minor-padding ">Como <span class="bold main-orange-span">estruturar</span> a reabertura da minha rede?</div>
                <div class="minor-padding main-orange-span">
                    <div class="minor-padding">
                        <img class="minor-icon" src="data:image/png;base64,{steps_icon}" alt="Fonte: Flaticon">
                        Passo a passo
                    </div>
                    <div class="minor-padding"> 
                        <img class="minor-icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
                        Protocolos
                    </div>
                    <div class="minor-padding"> 
                        <img class="minor-icon" src="data:image/png;base64,{ruler_icon}" alt="Fonte: Flaticon">
                        Régua de protocolo
                    </div>
                    <div class="minor-padding"> 
                        <img class="minor-icon" src="data:image/png;base64,{simulation_icon}" alt="Fonte: Flaticon">
                        Simule o retorno
                    </div>
                </div></br>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("comece aqui >"):
            session_state.section1_organize = True
            session_state.section2_manage = False
    with coluna2:
        verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
        notify_icon = utils.load_image("imgs/monitor_notify_icon.png")
        plan_icon = utils.load_image("imgs/monitor_plan_icon.png")

        st.write(
            f"""
            <div class="container" style="min-height: 150px;"><br>
                <div class="text-title-section minor-padding">Como <span class="bold main-orange-span">gerir</span> as unidades escolares abertas?</div>
                <div class="minor-padding main-orange-span">
                    <div class="minor-padding">
                        <img class="minor-icon" src="data:image/png;base64,{verify_icon}" alt="Fonte: Flaticon">
                        Ferramenta de verificação
                    </div>
                    <div class="minor-padding"> 
                        <img class="minor-icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
                        Plano de contingência
                    </div>
                    <div class="minor-padding"> 
                        <img class="minor-icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
                        Ferramenta de notificação
                    </div>
                </div></br>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("veja ferramentas >"):
            session_state.section2_manage = True
            session_state.section1_organize = False
    with espaco:
        st.write(
            f"""
        <div class="container minor-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )
    if session_state.section1_organize == True:
        pc.genPlanContainer(data, config, session_state)
        sc.genSimulationContainer(data, config, session_state)

    if session_state.section2_manage == True:
        prc.genPrepareContainer()
        mc.genMonitorContainer()
    st.write(
        f"""
    <div class="container minor-padding">
        <br>
    </div>
    """,
        unsafe_allow_html=True,
    )
    spc.genSpecialistContainer()
    rc.genReferencesContainer()
    fc.genFooterContainer()


if __name__ == "__main__":
    main()
