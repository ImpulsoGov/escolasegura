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
# import plotly.graph_objs as go
# import matplotlib.pyplot as plt
# import numpy as np

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
                <span class="title-section" style="color:#ff9147"><b>RESULTADO DA SIMULACÃO</b><br></span>
                <br><b>TURMAS</b><br>
                Quantidade de turmas: {result["limite_turmas"]} </br>
                Dias letivos necessários para cumprir as horas totais anuais (800 horas): {result["diasletivos"]} </br>
                <br><b>ORGANIZAÇÃO</b><br>
                Número de alunos que retornariam às aulas presenciais: {result["number_alunos_retornantes"]} </br>
                <span style="font-size:0.85rem">Numero de alunos que não poderiam retornar: {result["alunoslivres"]}</span></br>
                <br>Número de professores que retornariam às aulas presenciais: {result["number_professores_retornantes"]} </br>
                <span style="font-size:0.85rem">Numero de professores que não precisariam retornar: {result["professoreslivres"]}</span></br>
                <br>Numero de salas que estariam ocupadas com aulas presenciais: {result["salasocupadas"]} </br>
                <span style="font-size:0.85rem">Numero de salas livres de aulas presenciais: {result["salaslivres"]}</span></br>
                <br><b>MATERIAIS</b><br>
                Planeje suas compras! Estos são os materiais necessários por semana:<br>
                Número de máscaras necessárias: {result["total_masks"]} </br>
                Litros de álcool em gel necessários: {result["total_sanitizer"]} </br>
                Número de termômetros necessários: {result["total_thermometers"]} </br>
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
    subtitle = """O retorno às atividades presenciais deve ser pensado em etapas para definir não só quem pode retornar, mas também como. Trazemos abaixo um passo a passo para construir a simulação da sua rede - experimente!"""
    utils.main_title(title="<b>Simulador</b>: como organizar a rebertura?", subtitle=subtitle)
    utils.gen_title(title="Selecione sua rede:", subtitle="")
    genSelectBox(df, session_state)
    utils.gen_title(title="<b>1</b>. Quantos professores e alunos vão retornar?", subtitle="")
    params = dict()
    params["number_alunos"] = st.number_input(
        "Total de alunos matriculados",
        format="%d",
        value=data["number_students"].values[0],
        step=1,
    )
    params["number_alunos_naovoltando"] = st.number_input(
        "Quantidade de alunos que NÃO irão voltar presencialmente",
        format="%d",
        max_value=params["number_alunos"],
        value=0,
        step=1,
    )
    params["number_professores"] = st.number_input(
        "Total de professores",
        format="%d",
        value=data["number_teachers"].values[0],
        step=1,
    )
    params["number_professores_naovoltando"] = st.number_input(
        "Quantidade de professores que NÃO irão voltar presencialmente",
        format="%d",
        max_value=params["number_professores"],
        value=0,
        step=1,
    )

    utils.gen_title(title="<b>2</b>. Informe sobre suas salas", subtitle="")
    params["number_salas"] = st.number_input(
        "Quantidade de Salas disponíveis",
        format="%d",
        value=10,
        step=1,
    )
    params["maxalunossalas"] = st.number_input(
        "Máximo de alunos por sala",
        format="%d",
        value=20,
        step=1,
    )

    utils.gen_title(title="<b>3</b>. Organize suas turmas", subtitle="")
    params["hours_classpresencial"] = st.slider(
        "Horas diárias de aula PRESENCIAL por turma:", 0, 10, 5, 1
    )
    params["hours_classpremoto"] = st.slider(
        "Horas diárias de aula REMOTA por turma:", 0, 10, 0, 1
    )
    params["turnos"] = st.slider(
        "Número de turnos em um dias:", 0, 10, 2, 1
    )
    # A = [4, 4, 4, 4, 4]
    # B = [4, 4, 4, 4, 4]
    # C = [4, 4, 4, 4, 4]
    # D = [4, 4, 4, 4, 4]
    # E = [4, 4, 4, 4, 4]
    # fig = plt.figure(facecolor="white")
    # ax = fig.add_subplot(1, 1, 1)
    # bar_width = 0.5
    # bar_l = np.arange(1, 6)
    # tick_pos = [i + (bar_width / 2) for i in bar_l]

    # ax1 = ax.bar(bar_l, A, width=bar_width, label="A")
    # ax2 = ax.bar(bar_l, B, bottom=A, width=bar_width, label="B")
    # ax3 = ax.bar(bar_l, C, bottom=A, width=bar_width, label="C")
    # # ax4 = ax.bar(bar_l, D, bottom=A, width=bar_width, label="D")
    # # ax5 = ax.bar(bar_l, E, bottom=A, width=bar_width, label="E")
    # ax.set_ylabel("Horas de Aula Presenciais por Dia", fontsize=14)
    # ax.legend(loc="best")
    # ax.xaxis.tick_top() 
    # plt.xticks(tick_pos, ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'], fontsize=16)
    # st.pyplot(fig)
    # A = [4, 4, 4, 4, 4]
    # B = [4, 4, 4, 4, 4]
    # C = [4, 4, 4, 4, 4]
    # mylist = {}
    # mylist["pies_2018"] = A
    # mylist["pies_2019"] = B
    # mylist["pies_2020"] = C
    # plotdataA = pd.DataFrame(A,index=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])
    # plotdataB = pd.DataFrame(A,index=['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'])
    # stacked_data = plotdataA.apply(lambda x: x, axis=1)
    # layout = go.Layout(
    #     # title=title,
    #     #plot_bgcolor="rgba(0,0,0,0)",
    #     # autosize=True,
    #     # width=1000,
    #     height=700,
    #     margin={"l": 100, "r": 100, "t": 30},
    #     xaxis=dict(domain=[0, 0.8]),
    #     xaxis2=dict(domain=[0.85, 1]),
    #     yaxis=dict(tickmode="linear"),
    #     # yaxis2=dict(tickmode="linear", anchor="x2"),
    # )
    # traceA = go.Bar(
    #     x=plotdataA,
    #     y=plotdataA.index,
    #     xaxis="x2",
    #     yaxis="y2",
    #     orientation="h",
    #     hoverinfo="text",
    # )
    # traceB = go.Bar(
    #     x=plotdataB,
    #     y=plotdataB.index,
    #     xaxis="x2",
    #     yaxis="y2",
    #     orientation="h",
    #     hoverinfo="text",
    # )
    # tracedata = [traceA, traceB]
    # fig = go.Figure(data=tracedata, layout=layout)
    # st.plotly_chart(fig, use_container_width=True)
    # st.bar_chart(stacked_data)
    # ax = stacked_data.plot(kind="bar", stacked=True, fontsize=14)
    # ax.patch.set_facecolor('white')
    # ax.xaxis.tick_top() 
    # plt.ylabel("Horas de Aula Presenciais por Dia", fontsize=14)
    # plt.legend(bbox_to_anchor=(1.05, 1))
    # fig = plt.figure()


    params["professorday"] = st.number_input(
        "Horas aula diárias por professor",
        format="%d",
        value=6,
        step=1,
    )
    params["horaaula"] = st.number_input(
        "Tempo de hora aula (minutos)",
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
