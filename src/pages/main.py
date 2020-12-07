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
import amplitude



def read_data(country, config, endpoint):
    """ 
    This is function reads the API's data

    Parameters: 
        country (type): data country
        config (type): doc config.yaml
        endpoint (type): endpoint name in API
              
    """

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
    """ 
    This function return a dataframe with all data

    Parameters: 
        config (type): doc config.yaml

    Returns:
        df (type): 2019 school census dataframe
    """
    
    df = read_data("br", config, "br/cities/safeschools/main").replace(
        {"Fundamental I": "Fund. I", "Fundamental II": "Fund. II"}
    )
    return df


def genSelectBox(df, session_state, user_analytics):
    """ 
    This function generates select boxes for choosing the school network

    Parameters: 
        df (type): 2019 school census dataframe
        session_state (type): section dataset
        user_analytics (type): user data by amplitude
    """

    st.write(
        f"""
        <div class="main-padding" id="top">
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
        import pathlib
        from bs4 import BeautifulSoup
        GA_JS = (
            """
        window.dataLayer = window.dataLayer || [];
        function municipio(){dataLayer.push('municipio_value': '%s');}
        """
            % session_state.city_name
        )
        index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
        soup = BeautifulSoup(index_path.read_text())
        script_tag_loader = soup.new_tag("script")
        script_tag_loader.string = GA_JS
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
    changed_place = user_analytics.safe_log_event(
        "picked escolasegura place",
        session_state,
        event_args={"estado_value": session_state.state_id, "municipio_value": session_state.city_name, "administracao_value": session_state.administrative_level},
    )


def main(session_state):
    """ 
    This function generates Escola Segura webpage

    Parameters: 
        session_state (type): section dataset
    """

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
    user_analytics = amplitude.gen_user(utils.get_server_session())
    opening_response = user_analytics.safe_log_event(
        "opened escolasegura", session_state, is_new_page=True
    )
    utils.localCSS("style.css")
    st.write(
        """<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5ZZ5F66" height="0" width="0" style="display:none;visibility:hidden"></iframe>""",
        unsafe_allow_html=True,
    )
    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    data = get_data(config)
    genSelectBox(data, session_state, user_analytics)

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
    
        if session_state.city_name != "Todos":
            message_begin = session_state.city_name +", como"
        else: 
            message_begin = "Como"

        st.write(
                f"""
                <div class="container" style="min-height: 150px;"><br>
                    <div class="text-title-section minor-padding ">{message_begin} <span class="bold main-orange-span">estruturar</span> 
                    a reabertura da sua rede?</div>
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
                user_analytics = amplitude.gen_user(utils.get_server_session())
                opening_response = user_analytics.safe_log_event(
                    "clicked botaoI", session_state, is_new_page=True
                )
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
            user_analytics = amplitude.gen_user(utils.get_server_session())
            opening_response = user_analytics.safe_log_event(
                "clicked botaoII", session_state, is_new_page=True
            )
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
    
    st.write(
        f"""
            <a href="#top" class="float">
                <img class="my-float minor-icon" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMi4xNzEgNTEyLjE3MSIgc3R5bGU9ImVuYWJsZS1iYWNrZ3JvdW5kOm5ldyAwIDAgNTEyIDUxMiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgY2xhc3M9IiI+PGc+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+Cgk8Zz4KCQk8cGF0aCBkPSJNNDc2LjcyMywyMTYuNjRMMjYzLjMwNSwzLjExNUMyNjEuMjk5LDEuMTA5LDI1OC41OSwwLDI1NS43NTMsMGMtMi44MzcsMC01LjU0NywxLjEzMS03LjU1MiwzLjEzNkwzNS40MjIsMjE2LjY0ICAgIGMtMy4wNTEsMy4wNTEtMy45NDcsNy42MzctMi4zMDQsMTEuNjI3YzEuNjY0LDMuOTg5LDUuNTQ3LDYuNTcxLDkuODU2LDYuNTcxaDExNy4zMzN2MjY2LjY2N2MwLDUuODg4LDQuNzc5LDEwLjY2NywxMC42NjcsMTAuNjY3ICAgIGgxNzAuNjY3YzUuODg4LDAsMTAuNjY3LTQuNzc5LDEwLjY2Ny0xMC42NjdWMjM0LjgzN2gxMTYuODg1YzQuMzA5LDAsOC4xOTItMi42MDMsOS44NTYtNi41OTIgICAgQzQ4MC43MTMsMjI0LjI1Niw0NzkuNzc0LDIxOS42OTEsNDc2LjcyMywyMTYuNjR6IiBmaWxsPSIjZmY5MTQ3IiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+Cgk8L2c+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg==" alt="Fonte: Flaticon">
            </a>
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
    rc.genReferencesContainer(session_state)
    fc.genFooterContainer()


if __name__ == "__main__":
    main()
