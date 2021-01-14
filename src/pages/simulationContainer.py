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
                    <div class="grid-container-simulation-material" style="padding: 10px;">
                        <div class="div2 card-number" style="color:#FF934A"> {result["equitative"]["num_returning_students"]} </div>
                        <div class="div2">estudantes, <br>2 horas por semana</div>
                    </div>
                    <div class="grid-container-simulation-material minor-padding" style="padding: 10px;">
                        <div class="div2 card-number" style="color:#2B14FF"> {result["equitative"]["num_returning_teachers"]} </div>
                        <div class="div2" >professores, <br>2 horas por sema</div>
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
                        <div class="grid-container-simulation-material" style="padding: 10px;">
                            <div class="div2 card-number"> {result["equitative"]["total_thermometers"]} </div>
                            <div class="div2"><b>termômetros</b> (1/100 alunos)</div>
                        </div>
                        <div class="grid-container-simulation-material minor-padding" style="padding: 10px;">
                            <div class="div2 card-number"> {result["equitative"]["total_masks"]} </div>
                            <div class="div2" ><b>máscaras  por semana</b> (1/pessoa cada 3 horas)</div>
                        </div>
                        <div class="grid-container-simulation-material" style="padding: 10px;">
                            <div class="div2 card-number"> {int(result["equitative"]["total_sanitizer"])} </div>
                            <div class="div2" ><b>litros de álcool em gel</b> (12ml/pessoa por dia)</div>
                        </div>
                        <div class="container">
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="blank_">
                                <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">veja a lista completa ></button><br>
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
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">entenda sobre os turnos ></button><br>
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
    education_phase = st.selectbox(
        "", data["education_phase"].sort_values().unique()
    )
    data = data[data["education_phase"] == education_phase]

    st.write(
        f"""<br>
            <div class="container">
                <div class="minor-padding" style="font-size: 20px; color:#FF934A; font-weight: bold;">1. Escolha o modelo de retorno às atividades</div>
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
    education_model = st.selectbox(
        "", UNESCOmodels
    )
    col1_1, col1_2 = st.beta_columns([0.3, 0.4])
    with col1_1:
        # with st.beta_expander("entenda cada modelo >"):
            # st.write(
            #     f"""
            #         <div class="minor-padding">
            #             <a href="https://i.imgur.com/FyoIFe9.jpg" target="_blank">
            #                 <img class="images" src="https://i.imgur.com/FyoIFe9.jpg"> 
            #             </a>
            #         </div>
            #     """,
            #     unsafe_allow_html=True,
            # )   
        st.write(
            f"""
                <div class="container">
                    <div class="button-position" style="padding-bottom: 10px; text-align:left;">
                        <a href="" target="blank_">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">entenda cada modelo ></button><br>
                        </a>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )
    with col1_2:
        # with st.beta_expander("planeje por etapa de ensino >"):
        #     st.write(
        #         f"""
        #             <div class="minor-padding">
        #                 <a href="https://imgur.com/ZByy47a" target="_blank">
        #                     <img class="images" src="https://i.imgur.com/ZByy47a.jpg"> 
        #                 </a>
        #             </div>
        #         """,
        #         unsafe_allow_html=True,
        # )
        st.write(
            f"""
                <div class="container">
                    <div class="button-position" style="padding-bottom: 10px; text-align:left;">
                        <a href="" target="blank_">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">planeje por etapa de ensino ></button><br>
                        </a>
                    </div>
                </div>
            """,
            unsafe_allow_html=True,
        )


    st.write(
        f"""<br>
            <div class="container">
                <div class="minor-padding" style="font-size: 20px; color:#FF934A; font-weight: bold;">2. Escolha quem pode retornar</div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    params = dict()
    col2a_1, col2a_2 = st.beta_columns([0.4, 0.8])
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
            <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row" style="margin-bottom:0px;">
                    <div class="col text-padding container">
                        <b>Iniciamos com total de alunos reportados no Censo Escolar 2019 (INEP).</b>
                        <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de alunos podem ser <b>vulneráveis</b> ou ter prioridade.
                    </div>
                </div>
                <div class="container">
                    <div class="button-position" style="padding-bottom: 10px;">
                        <a href="" target="blank_">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">como retornar estudantes ></button><br>
                        </a>
                    </div>
                </div>
            </div>
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
    col2b_1, col2b_2 = st.beta_columns([0.4, 0.8])  
    with col2b_1:
        params["number_teachers"] = st.number_input(
            "Quantos professores(as) retornam?",
            format="%d",
            value=data["number_teachers"].values[0],
            step=1,
        )
    with col2b_2:
        st.write(
            f"""
            <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row" style="margin-bottom:0px;">
                    <div class="col text-padding container">
                        <b>Iniciamos com total de professores reportados no Censo Escolar 2019 (INEP).</b> 
                        <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de professores podem ser de <b>risco, confortáveis para retorno e outros.</b>
                    </div>
                </div>
                <div class="container">
                    <div class="button-position" style="padding-bottom: 10px;">
                        <a href="" target="blank_">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:18px;">como retornar professores(as) ></button><br>
                        </a>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )




    st.write(
        f"""
        <br>
        <div class="minor-padding" style="font-size: 20px; color:#FF934A; font-weight: bold;">3. Defina as restrições de retorno</div><br>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col3_1, col3_2, col3_3, col3_4, col3_5 = st.beta_columns(
        [0.35, 0.05, 0.4, 0.05, 0.4]
    )

    with col3_1:
        params["number_classrooms"] = st.number_input(
            "Quantas salas de aula disponíveis?",
            format="%d",
            value=data["number_classroms"].values[0],
            step=1,
        )
        st.write(
            f"""<div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row">
                    <div class="col text-subdescription container">
                        O número de salas e professores(as) restringem o número de turmas que podem voltar de forma simultânea.
                    </div>
                </div>
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
        params["max_students_per_class"] = st.slider(
            "Quantas salas de aula disponíveis?", 0, 20, 20, 1
        )
        st.write(
            f"""
            <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row">
                    <div class="col text-subdescription container">
                        As instituições XX recomendam o máximo de XX alunos por sala para diminuir o risco de transmissão.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3_4 = col3_2

    with col3_5:
        hours_classes = st.slider(
            "Selecione o número de horas presenciais na semana por turma:", 0, 4, 2, 1,
        )
        params["hours_classes"] = int(hours_classes)
        st.write(
            f"""
             <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
                <div class="row">
                    <div class="col text-subdescription container">
                        As restrições sanitárias limitam a quantidade de tempo e alunos que conseguem retornar à sala de aula.
                    </div>
                </div>
            </div>

            <div class="container">
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
