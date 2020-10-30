import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout


def genHeroSection(title1: str, title2: str, subtitle: str, header: bool):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-header" style="font-weight:bold;">corona</span><span class="logo-header" style="font-weight:lighter;">cidades</span></a>"""
    else:
        header = """<br>"""

    st.write(
        f"""
        <div class="container row">
            <div class="col">
                {header}
                <br>
                <span class="hero-container-product main-blue-span">{title1}</span>
                <br>
                <span class="hero-container-product main-blue-span">{title2}</span>
                <br><br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question main-grey-span">Controle a Covid-19 e promova aulas presenciais seguras na rede pública.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def read_data(country, config, endpoint):
    # if os.getenv("IS_LOCAL") == "TRUE":
    #     api_url = config[country]["api"]["local"]
    # else:
    #     api_url = config[country]["api"]["external"]
    api_url = config[country]["api"]["local"]
    url = api_url + endpoint
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
    col1, col2, col3, col4 = st.beta_columns([0.25, 0.5, 0.5, 1])

    with col1:
        session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
    with col2:
        session_state.city_name = st.selectbox(
            "Município", utils.filter_place(df, "city", state_id=session_state.state_id)
        )
    with col3:
        session_state.administrative_level = st.selectbox(
            "Nível de Administração",
            utils.filter_place(
                df, "administrative_level", state_id=session_state.state_id
            ),
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


def genPlanContainer(df, session_state):

    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]

    alert = data["overall_alert"].values[0]
    if alert == 3.0:
        href = "https://imgur.com/CYkwogu"
        url = href + ".jpg"
        caption = f"Seu nível de alerta é: <b>ALTÍSSIMO</b>. Há um crescente número de casos de Covid-19 e grande parte deles não são detectados."

    elif alert == 2.0:
        href = "https://imgur.com/tDJfCji"
        url = href + ".jpg"
        caption = f"Seu nível de alerta é: <b>ALTO</b>. Há muitos casos de Covid-19 com transmissão comunitária. A presença de casos não detectados é provável."

    elif alert == 1.0:
        href = "https://imgur.com/Oc6NzxW"
        url = href + ".jpg"
        caption = f"Seu nível de alerta é: <b>MODERADO</b>. Há um número moderado de casos e a maioria tem uma fonte de transmissão conhecida."

    elif alert == 0.0:
        href = "https://imgur.com/bQwNgo7"
        url = href + ".jpg"
        caption = f"Seu nível de alerta é: <b>NOVO NORMAL</b>. Casos são raros e técnicas de rastreamento de contato e monitoramento de casos suspeitos evitam disseminação."
    else:
        href = "https://imgur.com/CYkwogu"
        url = ""
        caption = "Não há nível de alerta na sua cidade. Sugerimos que confira o nível de risco de seu estado."

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Planeje                
                <p>Acesse ferramentas e conteúdos para planejar uma reabertura organizada e segura.</p>
            </div><br>
            <div class="left-margin">
                <div class="row">
                    <div class="col">
                        <div class="text-title-section  minor-padding"> <img class="icon" src="https://i.imgur.com/y5hUwaG.png"> Passo a passo</div>
                        <div class="minor-padding"><b>O que é?</b> Saiba quais etapas seguir para retomar as atividades presenciais na sua rede escolar.</div>
                    </div>
                    <div class="col">
                        <div class="text-title-section minor-padding"> <img class="icon" src="https://i.imgur.com/RaaOZjA.png"> Protocolos</div>
                        <div class="minor-padding"><b>O que é?</b> Lista de orientações para preparar sua estrutura sanitária e planejar rotinas seguras dentro e fora da sala de aula.</div>
                    </div>
                </div><br>
                <div class="text-title-section"> Régua de protocolo </div>
                <p>{caption}</p>
                </div>
                <div class="minor-padding">
                    <a href={href}>
                        <img class="images" src={url}> 
                    </a>
                </div>
                </div>
            </div>
        </div><br>
        """,
        unsafe_allow_html=True,
    )


def genSimulationResult(number_students, number_teachers, number_classroms):
    st.write(
        f"""
        <div class="container main-padding">
            <div>
                <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                <div class="row main-padding">
                    <div class="col">
                        <div class="card-simulator blue-bg">
                            <div class="card-title-section primary-span uppercase">EQUITATIVO</div>
                            <div class="text-small bold">Todos os alunos têm aula presencial ao menos 1 vez por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://i.imgur.com/8Ih89nm.png"> </div>
                                <div class="div2 card-number">250 </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 2x </div>
                                <div class="div6"> por semana </div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://i.imgur.com/DKFwj7Z.png"> </div>
                                <div class="div2"> <span class="card-number">100</span> </div>
                                <div class="div3 bold">  professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 2x </div>
                                <div class="div6"> por semana (6 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator blue-bg minor-padding">
                            <div class="card-title-section primary-span uppercase">Materiais para compra <img src="https://via.placeholder.com/20"></div>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 350 </div>
                                <div class="div3 bold"> máscaras </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 3 </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 4.2 </div>
                                <div class="div3 bold"> litros de álcool em gel </div>
                            </div>
                        </div> 
                    </div>
                    <div class="col">
                        <div class="card-simulator dark-blue-bg light-span">
                            <div class="card-title-section">PRIORITÁRIO</div>
                            <div class="text-small">Máximo de alunos retorna 5 vezes por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://i.imgur.com/8Ih89nm.png"> </div>
                                <div class="div2 card-number">250 </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 2x </div>
                                <div class="div6"> por semana </div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://i.imgur.com/DKFwj7Z.png"> </div>
                                <div class="div2"> <span class="card-number">100</span> </div>
                                <div class="div3 bold">  professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 2x </div>
                                <div class="div6"> por semana (6 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator primary-blue-bg minor-padding">
                            <div class="card-title-section light-span uppercase">Materiais para compra <img src="https://via.placeholder.com/20"></div>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 350 </div>
                                <div class="div3 bold"> máscaras </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 3 </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://via.placeholder.com/30"> </div>
                                <div class="div2 card-number"> 4.2 </div>
                                <div class="div3 bold"> litros de álcool em gel </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>               
            <div class="minor-padding">
                <div class="minor-padding blue-bg" style="border-radius:5px;">
                    <div style="padding:10px;">
                        <img src="https://via.placeholder.com/40"> <b>Veja mais materiais necessários para compra 
                        <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0">
                        aqui</a>.</b>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationContainer(df, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="subtitle-section"> Simule o retorno </div>
                <div class="left-margin">
                    <div class="minor-padding">Analise qual o modelo de retorno mais adequado para sua realidade e calcule os recursos necessários para a retomada.
                    Abaixo trazemos 2 possíveis modelos:</div>
                    <div class="minor-padding">
                        <div class="text-title-section minor-padding"> Entenda os modelos de retorno </div>
                        <div>
                            Uma parte essencial da reabertura é definir 
                            <b>quem pode retornar e como</b> - trazemos 2 modelos possíveis:
                        </div>
                    <div class="minor-padding">
                        <div class="text-title-section minor-padding"> Entenda os modelos de retorno </div>
                        <div class="row main-padding" style="grid-gap: 1rem;">
                            <div class="col blue-bg card-simulator" style="border-radius:30px;">
                                <div class="two-cols-icon-text">
                                    <div class="card-title-section">EQUITATIVO</div>
                                    <div class="text-subdescription">
                                        <b>Todos os alunos têm aula presencial ao menos 1 vez por semana.</b>
                                        <p></p>
                                        Prioriza-se de forma igualitária que alunos voltem para a escola, mesmo  
                                        que somente 1 dia. Atividades podem ser de reforço ou conteúdo.
                                    </div>
                                </div>
                            </div>
                            <div class="col light-blue-bg light-span card-simulator" style="border-radius:30px">
                            <div class="two-cols-icon-text">
                                <div class="card-title-section">PRIORITÁRIO</div>
                                <div class="text-subdescription">
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
                <div class="text-title-section minor-padding">Defina seu modelo de retorno</div><br>
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
            <br><div class="container text-padding bold">2) Utilize os filtros para os dados do Censo Escolar (2019):</div>
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

    with col2_1:
        number_students = st.number_input(
            "Qual total de alunos da sua rede?",
            format="%d",
            value=data["number_students"].values[0],
            step=1,
        )

    with col2_2:
        number_teachers = st.number_input(
            "Qual total de professores da sua rede?",
            format="%d",
            value=data["number_teachers"].values[0],
            step=1,
        )

    with col2_3:
        number_classroms = st.number_input(
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
        <div class="container main-padding bold">4) Escolha as condições de retorno:</div><br>
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
            "Percentual de alunos realizando atividades presenciais:", 0, 100, 100, 10
        )
        number_students = int(perc_students * number_students / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_students)}% dos alunos</i> - {str(number_students)} alunos no total.<br><hr>
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
            "Percentual de professores realizando atividades presenciais:",
            0,
            100,
            100,
            10,
        )
        number_teachers = int(perc_teachers * number_teachers / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_teachers)}% dos alunos</i> - {str(number_teachers)} professores no total.<br><hr>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3_4 = col3_2

    with col3_5:
        st.write(
            f"""<div class="minor-padding"> </div>""", unsafe_allow_html=True,
        )

        max_students = st.slider("Máximo de alunos por sala:", 0, 20, 20, 1)

        st.write(
            f"""<div class="container">
                <i>Valor selecionado: {max_students} alunos por sala</i><br>
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

    with st.beta_expander("SIMULAR RETORNO"):
        genSimulationResult(number_students, number_teachers, number_classroms)

    '''if st.button("SIMULAR RETORNO"):
        if st.button("Esconder"):
            pass
        genSimulationResult()
    utils.stylizeButton(
        name="SIMULAR RETORNO",
        # style_string="""border: 1px solid var(--main-white);box-sizing: border-box;border-radius: 15px; width: auto;padding: 0.5em;text-transform: uppercase;font-family: var(--main-header-font-family);color: var(--main-white);background-color: var(--main-primary);font-weight: bold;text-align: center;text-decoration: none;font-size: 18px;animation-name: fadein;animation-duration: 3s;margin-top: 1em;""",
        style_string="""box-sizing: border-box;border-radius: 15px; width: 150px;padding: 0.5em;text-transform: uppercase;font-family: 'Oswald', sans-serif;background-color:  #0097A7;font-weight: bold;text-align: center;text-decoration: none;font-size: 18px;animation-name: fadein;animation-duration: 3s;margin-top: 1.5em;""",
        session_state=session_state,
    )'''


def genPrepareContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Prepare 
            <p>Durante a reabertura, avalie se a sua unidade escolar está cumprindo todos os protocolos.</p>
            </div>
                <div class="left-margin">
                    <div class="text-title-section minor-padding"> <img class="icon" src="https://i.imgur.com/goLh8rm.png"> Ferramenta de verificação</div>
                    <div class="minor-padding"><b>O que é?</b> Preencha o formulário para conferir a adequação da sua unidade aos protocolos e receber orientações.</div>
                    <br>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLSer8JIT3wZ5r5FD8vUao1cR8VrnR1cq60iPZfuvqwKENnEhCg/viewform?usp=sf_link" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Carregando...</iframe>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genMonitorContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Monitore
                <p>Após a reabertura, monitore a Covid-19 e saiba o que fazer com o sugrimento de casos.</p>
            </div>
            <div class="left-margin">
                <div class="text-title-section minor-padding"> <img class="icon" src="https://i.imgur.com/RsEH5W0.png"> Plano de contigência</div>
                <div class="minor-padding">É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
                da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.</div>
                <div class="minor-padding">
                <img src="https://via.placeholder.com/300">
                </div>
                <div class="minor-padding">
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Carregando...</iframe>
                </div>
                <div class="text-title-section main-padding"> <img class="icon" src="https://i.imgur.com/goLh8rm.png"> Ferramenta de notificação</div>
                <div class="minor-padding">lorem ipsum.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Carregando...</iframe>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def genFooterContainer():
    st.write(
        f"""
        <div class="container">
            <div class="text-title-footer main-padding"> Realizado por </div>
            <br>
        </div>
        """,
        unsafe_allow_html=True,
    )


def main(session_state):
    utils.localCSS("style.css")
    genHeroSection(
        title1="Escola", title2="Segura", subtitle="{descrição}", header=True,
    )
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    data = get_data(config)
    genSelectBox(data, session_state)
    genPlanContainer(data, session_state)
    genSimulationContainer(data, session_state)
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()


if __name__ == "__main__":
    main()
