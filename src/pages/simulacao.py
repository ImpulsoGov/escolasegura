import streamlit as st
import session
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout
import utils
import amplitude
from model.get_school_return_data import entrypoint
from utils import load_markdown_content
import pages.snippet as tm
import pages.header as he
import pages.footer as foo
import matplotlib.pyplot as plt
from math import floor, ceil

@st.cache(suppress_st_warning=True)
def get_data(session_state):
    """ 
    This function return a dataframe with all data

    Parameters: 
        config (type): doc config.yaml

    Returns:
        df (type): 2019 school census dataframe
    """
    # url = "http://datasource.coronacidades.org/br/cities/safeschools/main?state_id="+session_state.state_id
    url = "http://datasource.coronacidades.org/br/cities/safeschools/main"
    df = pd.read_csv(url)
    return df


def genSelectBox(df, session_state):
    """ 
    This function generates select boxes for choosing the school network

    Parameters: 
        df (type): 2019 school census dataframe
        session_state (type): section dataset
        user_analytics (type): user data by amplitude
    """
    col1, col2, col3, col4 = st.beta_columns([0.3, 0.5, 0.5, 1])

    with col1:
        session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
        session_state.state_name = utils.set_state_name(df,session_state.state_id)
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



def genSimulationResult(params, config):
    """ 
    This is a function that returns the simulation result

    Parameters: 
        params (type): parameters for simulation
        config (type): doc config.yaml
              
    """

    result = entrypoint(params, config)

    teacher_icon = utils.load_image("imgs/simulation_teacher_icon.png")
    student_icon = utils.load_image("imgs/student_icons.png")
    mask_icon = utils.load_image("imgs/simulation_mask_icon.png")
    sanitizer_icon = utils.load_image("imgs/simulation_sanitizer_icon.png")
    thermometer_icon = utils.load_image("imgs/simulation_thermometer_icon.png")

    st.write(
        f"""
        <div class="conteudo" style="padding-top:5px;">
            <div style="background:#DDFBF0; padding:20px;">
                <span class="title-section" style="color:#2b14ff"><b>RESULTADO DA SIMULAÇÃO</b></span><br>
                <span class="title-section" style="color:#ff9147; font-size:1.5rem;">Turmas</span><br>
                Quantidade de turmas: <b>{result["limite_turmas"]}</b> </br>
                Dias letivos necessários para cumprir as horas totais anuais (800 horas): <b>{result["diasletivos"]}</b> </br>
                <br>
                <span class="title-section" style="color:#ff9147; font-size:1.5rem;">Organização</span><br>
                Número de alunos que retornariam às aulas presenciais: <b>{result["number_alunos_retornantes"]}</b> </br>
                <span style="font-size:0.85rem">Numero de alunos que não poderiam retornar: <b>{result["alunoslivres"]}</b></span></br>
                <br>Número de professores que retornariam às aulas presenciais: <b>{result["number_professores_retornantes"]}</b> </br>
                <span style="font-size:0.85rem">Numero de professores que não precisariam retornar: <b>{result["professoreslivres"]}</b></span></br>
                <br>Numero de salas que estariam ocupadas com aulas presenciais: <b>{result["salasocupadas"]}</b> </br>
                <span style="font-size:0.85rem">Numero de salas livres de aulas presenciais: <b>{result["salaslivres"]}</b></span></br>
                <br>
                <span class="title-section" style="color:#ff9147; font-size:1.5rem;">Materiais</span><br>
                Planeje suas compras! Esses são os materiais necessários por semana:<br>
                Número de máscaras necessárias: <b>{result["total_masks"]}</b> </br>
                Litros de álcool em gel necessários: <b>{result["total_sanitizer"]}</b> </br>
                Número de termômetros necessários: <b>{result["total_thermometers"]}</b> </br>
                <br>Como calcular o número de alunos por sala? <a href="https://www.fe.unicamp.br/salas/" >Veja aqui
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    utils.localCSS("localCSS.css")
    session_state = session.SessionState.get(
        key=session.get_user_id(),
        update=False,
        state_name="Acre",
        state_id="AC",
        city_name="Todos",
        administrative_level="Todos",
        refresh=False,
        reset=False,
        already_generated_user_id=None,
        pages_open=None,
        amplitude_events=None,
        button_styles=dict(),
        continuation_selection=None,
        button_simule=0,
        section1_organize=False,
        section2_manage=False,
    )
    he.genHeader("simulation")
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    df = get_data(session_state)
    data = df[(df["city_name"] == session_state.city_name)& (df["administrative_level"] == session_state.administrative_level)]
    subtitle = """Sabemos que no planejamento da reabertura surgem muitas dúvidas... Quantas turmas podem voltar? Quantos litros de álcool gel preciso comprar? 
<br>
O retorno às atividades presenciais deve ser planejado segundo as condições da sua rede. Simule abaixo o retorno e veja os recursos e materiais necessários para uma reabertura segura!
<br>
<b>Se você é gestor da rede:</b><br>
Preencha os dados da sua rede e obtenha uma simulação geral das condições de retorno. 
<br>
<b>Se você é gestor de uma escola:</b><br>
Preencha os dados específicos da sua escola, por série ou por etapa de ensino, e obtenha as condições e materiais necessários para voltar ás aulas presenciais com segurança.
<br>"""
    utils.main_title(title="<b>Simule o retorno:</b> como organizar a reabertura?", subtitle=subtitle)
    utils.gen_title(title="Selecione sua rede:", subtitle="")
    genSelectBox(df, session_state)
    utils.gen_title(title="<b>1</b>. Quem poderia retornar às aulas presenciais?", subtitle="")
    params = dict()
    params["number_alunos"] = st.number_input(
        "Total de alunos matriculados",
        format="%d",
        min_value=1,
        value=data["number_students"].values[0],
        step=1,
    )
    params["number_alunos_naovoltando"] = st.number_input(
        "Alunos não aptos para a volta presencial às aulas",
        format="%d",
        max_value=params["number_alunos"]-1,
        value=0,
        step=1,
    )
    params["number_professores"] = st.number_input(
        "Total de professores",
        format="%d",
        min_value=1,
        value=data["number_teachers"].values[0],
        step=1,
    )
    params["number_professores_naovoltando"] = st.number_input(
        "Professores não aptos para retornar presencialmente",
        format="%d",
        max_value=params["number_professores"]-1,
        value=0,
        step=1,
    )

    utils.gen_title(title="<b>2</b>. Qual é a disponiblidade de salas?", subtitle="")
    params["number_salas"] = st.number_input(
        "Salas disponíveis",
        format="%d",
        min_value=1,
        value=10,
        step=1,
    )
    params["maxalunossalas"] = st.number_input(
        "Máximo de alunos por sala",
        format="%d",
        min_value=1,
        value=20,
        step=1,
    )

    utils.gen_title(title="<b>3</b>. Como são suas turmas?", subtitle="")
    params["hours_classpresencial"] = st.slider(
        "Horas diárias de aula presencial por turma:", 1, 8, 4, 1
    )
    params["hours_classpremoto"] = st.slider(
        "Horas diárias de aula remota por turma:", 0, 6, 0, 1
    )
    params["turnos"] = st.slider(
        "Número de turnos:", 1, int(18/params["hours_classpresencial"]), 1, 1
    )
    if params["hours_classpresencial"] > 0:
        st.write(
        f"""
            <div class="conteudo" style="margin-top:15px; margin-bottom:40px;">
                <div style="background:#DDFBF0; padding:20px; border-radius: 0.8rem;">
                Na configuracão atual, <b>a escola funcionaria dando
                {params["hours_classpresencial"]*params["turnos"]} horas de aula presenciais por dia</b>, 
                sendo que cada turno (e as turmas do turno) terão 
                <b>{params["hours_classpresencial"]} horas presenciais</b> de aula e <b>{params["hours_classpremoto"]} horas remota</b>, 
                com essa carga horária será necessário <b>{ceil(800/(params["hours_classpresencial"]+params["hours_classpremoto"]))} dias letivos</b> para completar as 800 horas de carga letiva anual.<br>
                Continue a simulacão para saber quantas turmas e professores terão por turno.<br>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    # st.set_option('deprecation.showPyplotGlobalUse', False)
    # lista = dict()
    # for i in range(params["turnos"]):
    #     x = [params["hours_classpresencial"], params["hours_classpresencial"], params["hours_classpresencial"], params["hours_classpresencial"], params["hours_classpresencial"]]
    #     turmalabel = "Turno " + str(i+1)
    #     lista[turmalabel] = x
    # df = pd.DataFrame(data=lista)
    # df.index = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    # ax = df.plot(stacked=True, kind='bar', grid=False, figsize=(12, 8), rot='horizontal', fontsize=14, colormap='Pastel2')
    # ax.xaxis.tick_top()
    # ax.set_ylabel("Horas de Aula Presenciais por Dia", fontsize=14)
    # st.pyplot(ax.figure.savefig('turmas.png'))
    params["professorday"] = st.number_input(
        "Horas aula diárias por professor:",
        format="%d",
        value=6,
        step=1,
    )
    params["horaaula"] = st.number_input(
        "Tempo de hora aula (minutos):",
        format="%d",
        value=50,
        step=1,
    )

    if st.button("simular retorno"):
        genSimulationResult(params, config)

    tm.genGuia()
    foo.genFooter()

if __name__ == "__main__":
    main()
