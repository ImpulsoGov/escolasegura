import streamlit as st
import utils
import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout
import utils
import amplitude
from model.get_school_return_data import entrypoint
from utils import load_markdown_content


def genSimulationResult(params, config):
    """ 
    This is a function that returns the simulation result

    Parameters: 
        params (type): description
        config (type): doc config.yaml
              
    """

    result = entrypoint(params, config)

    teacher_icon = utils.load_image("imgs/simulation_teacher_icon.png")
    student_icon = utils.load_image("imgs/simulation_student_icon.png")
    mask_icon = utils.load_image("imgs/simulation_mask_icon.png")
    sanitizer_icon = utils.load_image("imgs/simulation_sanitizer_icon.png")
    thermometer_icon = utils.load_image("imgs/simulation_thermometer_icon.png")

    st.write(
        f"""
        <div class="container main-padding">
                <div class="text-title-section minor-padding main-orange-span"> RESULTADO DA SIMULAÇÃO </div>
                <p>Com os valores selecionados acima, os resultados da sua rede para os 2 modelos de retorno:</p>
                <p>* Caso os números apresentados não façam sentido, confira novamente se os dados inseridos sobre a sua localidade estão corretos.</p>
                <div class="row">
                    <div class="col main-padding">
                        <div class="card-simulator-up lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span uppercase">EQUITATIVO</div>
                            <div>Todos os alunos retornam ao menos 1 vez por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{student_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number">{result["equitative"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{teacher_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2"> <span class="card-number">{result["equitative"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold"> professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator-bottom light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra </div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{mask_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {result["equitative"]["total_masks"]} </div>
                                <div class="div3 bold"> máscaras por semana</div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{thermometer_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {result["equitative"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{sanitizer_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {int(result["equitative"]["total_sanitizer"])} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana</div>
                            </div>
                        </div> 
                    </div>
                    <div class="col main-padding">
                        <div class="card-simulator-up lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span">PRIORITÁRIO</div>
                            <div>Número limitado de alunos retorna 5 vezes por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{student_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number">{result["priority"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{teacher_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2"> <span class="card-number">{result["priority"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold">  professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator-bottom light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra </div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{mask_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_masks"]} </div>
                                <div class="div3 bold" > máscaras por semana </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{thermometer_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{sanitizer_icon}" alt="Fonte: Flaticon"> </div>
                                <div class="div2 card-number"> {int(result["priority"]["total_sanitizer"])} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>               
            <div class="minor-padding">
                <div class="minor-padding lighter-blue-green-bg" style="border-radius:5px;">
                    <div style="padding:10px;">
                       <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="_blank">
                        <img class = "icon-cards"
                         src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI1NiAwYy0xNDEuMTY0MDYyIDAtMjU2IDExNC44MzU5MzgtMjU2IDI1NnMxMTQuODM1OTM4IDI1NiAyNTYgMjU2IDI1Ni0xMTQuODM1OTM4IDI1Ni0yNTYtMTE0LjgzNTkzOC0yNTYtMjU2LTI1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMjE5NmYzIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtMzY4IDI3Ny4zMzIwMzFoLTkwLjY2Nzk2OXY5MC42Njc5NjljMCAxMS43NzczNDQtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzFzLTIxLjMzMjAzMS05LjU1NDY4Ny0yMS4zMzIwMzEtMjEuMzMyMDMxdi05MC42Njc5NjloLTkwLjY2Nzk2OWMtMTEuNzc3MzQ0IDAtMjEuMzMyMDMxLTkuNTU0Njg3LTIxLjMzMjAzMS0yMS4zMzIwMzFzOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFoOTAuNjY3OTY5di05MC42Njc5NjljMC0xMS43NzczNDQgOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFzMjEuMzMyMDMxIDkuNTU0Njg3IDIxLjMzMjAzMSAyMS4zMzIwMzF2OTAuNjY3OTY5aDkwLjY2Nzk2OWMxMS43NzczNDQgMCAyMS4zMzIwMzEgOS41NTQ2ODcgMjEuMzMyMDMxIDIxLjMzMjAzMXMtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzF6bTAgMCIgZmlsbD0iI2ZhZmFmYSIgZGF0YS1vcmlnaW5hbD0iI2ZhZmFmYSIgc3R5bGU9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                         title="Freepik" /></a> <b>Veja mais materiais necessários para compra 
                        <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="_blank">
                        aqui</a>.</b>
                    </div>
                </div>
            </div>
            <div class="minor-padding" style="margin-left:0.5em;">
                <br><p>ℹ️<i> Para entender como realizamos os cálculos, leia abaixo a metodologia.</p></i>
            </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationContainer(df, config, session_state):
    """ 
    This is a function that returns the "Simulation" session

    Parameters: 
        df (type): 2019 school census dataframe
        config (type): doc config.yaml
        session_state (type): section dataset
              
    """

    main_icon = utils.load_image("imgs/simulation_main_icon.png")

    st.write(
        f"""
        <div class="container main-padding">
            <div class="text-title-section minor-padding main-orange-span"> 
                <img class="icon" src="data:image/png;base64,{main_icon}" alt="Fonte: Flaticon">
                Simule o retorno
            </div>
            <div class="subtitle-section minor-padding"> 
                Qual é o modelo de retorno híbrido mais adequado para mim e qual a melhor logística e materiais necessários para isso?
            </div>
            <div class="minor-padding">
                Conheça os modelos que trazemos, <b>preencha o simulador</b> abaixo para calcular os recursos necessários para a retomada e analise qual o modelo de retorno mais adequado para sua realidade.
                <div class="main-padding">
                    <div class="text-title-section minor-padding main-orange-span" style="font-size:18px"> Entenda os modelos de retorno </div>
                        <div>
                            Uma parte essencial da reabertura é definir 
                            <b>quem pode retornar e como</b> - trazemos 2 modelos possíveis:
                        </div>
                    <div class="row main-padding" style="grid-gap: 1rem;">
                        <div class="col lighter-blue-green-bg card-simulator" style="border-radius:30px;">
                            <div class="row">
                                <div class="col card-title-section">EQUITATIVO</div>
                                <div class="col text-subdescription container">
                                    <b>Todos os alunos têm aula presencial ao menos 1 vez por semana.</b>
                                    <p></p>
                                    Prioriza-se de forma igualitária que alunos voltem para a escola, mesmo  
                                    que somente 1 dia. Atividades podem ser de reforço ou conteúdo.
                                </div>
                            </div>
                        </div>
                        <div class="col light-blue-green-bg card-simulator" style="border-radius:30px">
                        <div class="row">
                            <div class="col card-title-section">PRIORITÁRIO</div>
                            <div class="col text-subdescription container">
                                <b>Número limitado de alunos retorna 5 vezes por semana.</b>
                            <p></p>
                            O modelo prioriza o tempo que o aluno passa na escola, mesmo que para uma quantidade menor de alunos. 
                            Atividades podem ser de reforço ou conteúdo.
                        </div>
                    </div>
                    </div>
                </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        f"""<br>
            <div class="container">
                <div class="text-title-section minor-padding main-orange-span" style="font-size:18px">Defina seu modelo de retorno</div><br>
                <div>
                    <div class="text-padding bold">1) Para qual etapa de ensino você está planejando?</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # TODO: colocar por estado somente também
    # if city_name:
    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]
    col1_1, col1_2 = st.beta_columns([0.25, 1])

    with col1_1:
        education_phase = st.selectbox(
            "", data["education_phase"].sort_values().unique()
        )

        data = data[data["education_phase"] == education_phase]
    with col1_2:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write(
        f"""
            <br><div class="container text-padding bold">2) Utilize os filtros para os dados do Censo Escolar (2019). Caso você queira simular todas as escolas (ex: rurais e urbanas), não selecione nenhuma alternativa:</div>
        """,
        unsafe_allow_html=True,
    )
    if "Rural" in data["school_location"].drop_duplicates().values:
        rural = ["Rural" if st.checkbox("Apenas escolas rurais") else "Todos"][0]

        data = data[(data["school_location"] == rural)]

    if "Sim" in data["school_public_water_supply"].drop_duplicates().values:
        water_supply = [
            "Sim" if st.checkbox("Apenas escolas com água encanada") else "Todos"
        ][0]

        data = data[(data["school_public_water_supply"] == water_supply)]
    st.write(
        f"""
        <div class="container main-padding bold">3) Ou informe seus dados abaixo:</div><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col2_1, col2_2, col2_3, col2_4 = st.beta_columns([0.4, 0.4, 0.4, 0.5])

    params = dict()
    with col2_1:
        params["number_students"] = st.number_input(
            "Qual total de alunos da sua rede?",
            format="%d",
            value=data["number_students"].values[0],
            step=1,
        )

    with col2_2:
        params["number_teachers"] = st.number_input(
            "Qual total de professores da sua rede?",
            format="%d",
            value=data["number_teachers"].values[0],
            step=1,
        )

    with col2_3:
        params["number_classrooms"] = st.number_input(
            "Qual total de sala de aulas na sua rede?",
            format="%d",
            value=data["number_classroms"].values[0],
            step=1,
        )

    with col2_4:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write(
        f"""
        <div class="container main-padding bold">4) Escolha as condições desejadas para o retorno presencial:</div><br>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.beta_columns(
        [0.35, 0.05, 0.4, 0.05, 0.4, 0.3]
    )

    with col3_1:
        perc_students = st.slider(
            "Percentual de alunos que realizarão atividades presenciais:",
            0,
            100,
            100,
            10,
        )
        params["number_students"] = int(perc_students * params["number_students"] / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_students)}% dos alunos</i> - {str(params["number_students"])} alunos no total.<br><hr>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3_2:
        st.write(
            f"""
            <div class="container main-padding">
                <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3_3:
        perc_teachers = st.slider(
            "Percentual de professores que realizarão atividades presenciais:",
            0,
            100,
            100,
            10,
        )
        params["number_teachers"] = int(perc_teachers * params["number_teachers"] / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_teachers)}% dos professores</i> - {str(params["number_teachers"])} professores no total.<br><hr>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3_4 = col3_2

    with col3_5:
        st.write(
            f"""<div class="minor-padding"> </div>""", unsafe_allow_html=True,
        )

        params["max_students_per_class"] = st.slider(
            "Máximo de alunos por sala:", 0, 20, 20, 1
        )

        st.write(
            f"""<div class="container">
                <i>Valor selecionado: {params["max_students_per_class"]} alunos por sala</i><br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )

    with col3_6:
        st.write(
            f"""<div class="container">
                <br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )

    with st.beta_expander("simular retorno"):
        user_analytics = amplitude.gen_user(utils.get_server_session())
        opening_response = user_analytics.safe_log_event(
            "clicked simule retorno", session_state, is_new_page=True
        )
        genSimulationResult(params, config)

    '''if st.button("Simular retorno"):
        if st.button("Esconder"):
            pass
        genSimulationResult()
    utils.stylizeButton(
        name="SIMULAR RETORNO",
        style_string="""
        box-sizing: border-box;
        border-radius: 15px; 
        width: 150px;padding: 0.5em;
        text-transform: uppercase;
        font-family: 'Oswald', sans-serif;
        background-color: #0097A7;
        font-weight: bold;
        text-align: center;
        text-decoration: none;font-size: 18px;
        animation-name: fadein;
        animation-duration: 3s;
        margin-top: 1.5em;""",
        session_state=session_state,
    )'''

    with st.beta_expander("ler metodologia"):
        user_analytics = amplitude.gen_user(utils.get_server_session())
        opening_response = user_analytics.safe_log_event(
            "clicked simule metodologia", session_state, is_new_page=True
        )
        methodology_text = load_markdown_content("methodology.md")
        st.write(methodology_text)


if __name__ == "__main__":
    main()
