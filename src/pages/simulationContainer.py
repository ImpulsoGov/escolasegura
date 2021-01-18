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
        params (type): parameters for simulation
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
        <div class="container main-padding light-green-simulator-bg">
            <div class="text-title-section minor-padding main-orange-span"><b>RESULTADO DA SIMULAÇÃO</b></div>
            <div class="row">
                <div class="col minor-padding">
                    <p>Você pode retornar até <b>10 TURMAS</b> no modelo de <b>AULAS ASSÍNCRONAS POR VÍDEO</b>, totalizando:</p>
                    <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                        <div class="div2 card-number" style="color:#FF934A; width: 30%;"> {result["equitative"]["num_returning_students"]} </div>
                        <div class="div2" style="width: 50%;"><b>estudantes,</b> <br>2 horas por semana</div>
                    </div>
                    <div class="grid-container-simulation-material minor-padding" style="padding: 10px; display: flex; flex-flow: row wrap;">
                        <div class="div2 card-number" style="color:#2B14FF; width: 30%;"> {result["equitative"]["num_returning_teachers"]} </div>
                        <div class="div2" style="width: 50%;"><b>professores,</b> <br>2 horas por sema</div>
                    </div>
                    <div class="card-simulator-bottom light-green-simulator-bg">
                        <div class="grid-container-simulation-type minor-padding">
                            <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{student_icon}" alt="Fonte: Flaticon"> </div>
                        </div>
                        <div class="grid-container-simulation-type">
                            <div class="div1"> <img class="icon-cards" src="data:image/png;base64,{teacher_icon}" alt="Fonte: Flaticon"> </div>
                            <div class="div6">Cada turma possui somente 1 professor(a)</div>
                        </div>
                    </div>
                </div>
                <div class="col minor-padding">
                    <div class="card-simulator-bottom light-green-simulator-bg minor-padding">
                        <p>Considerando <b>protocolos sanitários</b> para o retorno, serão necessários para compra:</p>
                        <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 50%;"> {result["equitative"]["total_thermometers"]} </div>
                            <div class="div2" style="width: 50%;"><b>termômetros</b> (1/100 alunos)</div>
                        </div>
                        <div class="grid-container-simulation-material minor-padding" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 50%;"> {result["equitative"]["total_masks"]} </div>
                            <div class="div2" style="width: 50%;"><b>máscaras  por semana</b> (1/pessoa cada 3 horas)</div>
                        </div>
                        <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 50%;"> {int(result["equitative"]["total_sanitizer"])} </div>
                            <div class="div2" style="width: 50%;"><b>litros de álcool em gel</b> (12ml/pessoa por dia)</div>
                        </div>
                        <div class="container">
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="blank_">
                                <button class="button-protocolos"; style="border-radius: .25rem; font-size:16px;">veja a lista completa ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row main-padding">
                <div class="col minor-padding">
                    <div class="minor-padding" style="font-size: 18px; color:#FF934A; font-weight: bold;">COMO ORGANIZAR AS TURMAS?</div>
                    <div class="minor-padding">
                        Segundo a UNESCO, os <b>sistemas de turnos</b> podem ser uma forma eficaz de distribuir a aprendizagem presencial para a maioria dos estudantes. 
                        <br><br>
                        <b>Reduzir o número de estudantes na escola de forma simultânea</b> ajuda a reduzir o risco de transmissão da Covid-19 no local.
                        <br>
                    </div>
                    <div class="button-position minor-padding" style="padding-bottom: 10px;">
                        <a href="" target="blank_">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:16px;">entenda sobre os turnos ></button><br>
                        </a>
                    </div>
                </div>
                <div class="col minor-padding">
                    <a href="https://imgur.com/a/u8EKYBi" target="_blank">
                        <img class="images" src="https://i.imgur.com/KHVgLLX.jpg"> 
                    </a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationContainer(df, config, session_state):

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
                <br>O retorno às atividades presenciais deve ser pensado em etapas para definir não só <b>quem pode retornar</b>, mas também <b>como</b>. Trazemos abaixo um passo a passo para construir a simulação da sua rede - experimente!
            </div>
             <div class="minor-padding" style="font-size: 20px; color:#FF934A; font-weight: bold;">
                <br>Para qual etapa de ensino você está planejando?
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
    col1, col2 = st.beta_columns([0.9, 0.2])
    with col1:
        education_phase = st.selectbox(
            "", data["education_phase"].sort_values().unique()
        )
        data = data[data["education_phase"] == education_phase]
    with col2:
        st.write(
            f"""<div class="container">
                <br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )

    st.write(
        f"""<br>
            <div class="container">
                <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>1. Escolha o modelo de retorno às atividades</b></div>
                <div class="minor-padding">
                    Existem diversos modelos possíveis de retorno avaliadas de acordo com as etapas de aprendizado. Separamos abaixo 5 opções possíveis indicadas pela UNESCO.
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    UNESCOmodels = ['Totalmente Presencial', 
    'Apenas aulas expositivas presenciais + atividades como tarefa',
    'Aulas por video + exercícios e tarefas presenciais', 
    'Aulas sincronas por video', 
    'Aulas assincronas por video', 
    'Totalmente Remoto']
    col1_1, col1_2 = st.beta_columns([0.9, 0.2])
    with col1_1:
        education_model = st.selectbox(
            "", UNESCOmodels
        )
    with col1_2:
        st.write(
            f"""<div class="container">
                <br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )
    st.write(
        f"""
        <a href="#entenda-modelo">
            <button class="button-protocolos" style="border-radius: .25rem; font-size:16px;">
                entenda cada modelo >
            </button>
        </a>
        <div id="entenda-modelo" class="info-modal-window">
            <div>
                <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                <div style="margin: 10px 15px 15px 15px;">
                <h1 class="main-orange-span bold">Valores de referência</h1>
                <div style="font-size: 14px">
                    Para mais detalhes confira nossa página de Metodologia no <a href="http://farolcovid.coronacidades.org">FarolCovid</a>.</b></a>
                </div><br>
                <div class="info-div-table">
                    <table class="info-table">
                        <tbody>
                        </tbody>
                    </table>
                </div>
                </div>
            </div>
        </div>
        <div class="container">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        f"""
        <a href="#entenda-etapa">
            <button class="button-protocolos" style="border-radius: .25rem; font-size:16px;">
                planeje por etapa de ensino >
            </button>
        </a>
        <div id="entenda-etapa" class="info-modal-window">
            <div>
                <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
                <div style="margin: 10px 15px 15px 15px;">
                <h1 class="main-orange-span bold">Valores de referência</h1>
                <div style="font-size: 14px">
                    Para mais detalhes confira nossa página de Metodologia no <a href="http://farolcovid.coronacidades.org">FarolCovid</a>.</b></a>
                </div><br>
                <div class="info-div-table">
                    <table class="info-table">
                        <tbody>
                        </tbody>
                    </table>
                </div>
                </div>
            </div>
        </div>
        <div class="container">
        </div>
        """,
        unsafe_allow_html=True,
    )



    st.write(
        f"""<br>
            <div class="container">
                <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>2. Escolha quem pode retornar</b></div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    params = dict()
    col2a_1, col2a_2, col2a_3, col2a_4 = st.beta_columns([0.35, 0.05, 0.85, 0.3])
    with col2a_1:
        params["number_students"] = st.number_input(
            "Quantos estudantes retornam na rede?",
            format="%d",
            value=data["number_students"].values[0],
            step=1,
        )
    with col2a_2:
        st.write(
            f"""
            <div class="container main-padding">
                <br>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2a_3:
        st.write(
            f"""
            <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row" style="font-family: 'Roboto Condensed', sans-serif; margin-bottom:0px; padding:10px;">
                    <b>Iniciamos com total de alunos reportados no Censo Escolar 2019 (INEP).</b>
                    <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de alunos podem ser vulneráveis ou ter prioridade.
                </div>
                <div class="button-position" style="padding-bottom: 15px;">
                    <a href="#entenda-etapa">
                        <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
                            como retornar estudantes >
                        </button>
                    </a>
                </div>
            </div>

            """,
            unsafe_allow_html=True,
        )
    with col2a_4:
        st.write(
            f"""<div class="container">
                <br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )
    st.write(
        f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col2b_1, col2b_2, col2b_3, col2b_4 = st.beta_columns([0.35, 0.05, 0.85, 0.3])
    with col2b_1:
        params["number_teachers"] = st.number_input(
            "Quantos professores(as) retornam?",
            format="%d",
            value=data["number_teachers"].values[0],
            step=1,
        )
    col2b_2=col2a_2
    with col2b_3:
        st.write(
            f"""
            <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row" style="font-family: 'Roboto Condensed', sans-serif; margin-bottom:0px; padding:10px;">
                    <b>Iniciamos com total de professores reportados no Censo Escolar 2019 (INEP).</b> 
                    <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de professores podem ser de risco, confortáveis para retorno e outros.
                </div>
                <div class="button-position" style="padding-bottom: 15px;">
                    <a href="#entenda-etapa">
                        <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
                            como retornar professores(as) >
                        </button>
                    </a>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    col2b_4=col2a_4
    st.write(
        f"""
        <br>
        <div class="container">
            <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>3. Defina as restrições de retorno</b></div><br>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )





    col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.beta_columns(
        [0.35, 0.05, 0.4, 0.05, 0.4, 0.3]
    )
    with col3_1:
        params["number_classrooms"] = st.number_input(
            "Quantas salas de aula disponíveis?",
            format="%d",
            value=data["number_classroms"].values[0],
            step=1,
        )
        st.write(
            f"""
            <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
                O número de salas e professores(as) restringem o número de turmas que podem voltar de forma simultânea.
            </div>
        """,
            unsafe_allow_html=True,
        )
    col3_2=col2a_2
    with col3_3:
        params["max_students_per_class"] = st.slider(
            "Quantas salas de aula disponíveis?", 0, 20, 20, 1
        )
        st.write(
            f"""
            <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
                As instituições XX recomendam o máximo de XX alunos por sala para diminuir o risco de transmissão.
            </div>
            """,
            unsafe_allow_html=True,
        )
    col3_4 = col2a_2
    with col3_5:
        hours_classes = st.slider(
            "Selecione o número de horas presenciais na semana por turma:", 0, 4, 2, 1,
        )
        params["hours_classes"] = int(hours_classes)
        st.write(
            f"""
            <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
                As restrições sanitárias limitam a quantidade de tempo e alunos que conseguem retornar à sala de aula.
            </div>

            <div class="container">
            <br>
            </div>
            <br>
            """,
            unsafe_allow_html=True,
        )
    col3_6=col2a_4



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
