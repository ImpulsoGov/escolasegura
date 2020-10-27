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
                <span class="hero-container-product main-blue-span">{title1}</span>
                <br>
                <span class="hero-container-product main-blue-span">{title2}</span>
                <br><br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question main-grey-span">Como preparar a minha rede escolar para um retorno presencial seguro?</span>
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
    session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
    session_state.city_name = st.selectbox("Município", utils.filter_place(df, "city", state_id=session_state.state_id))
    session_state.administrative_level = st.selectbox("Nível de Administração",utils.filter_place(df,"administrative_level",state_id=session_state.state_id), index=2) 
  


def genPlanContainer(df, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">Planeje </div>
            <div class="left-margin">
                <div class="row">
                <div class="col">
                    <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Protocolos</div>
                    <div class="minor-padding">Encontre uma planilha de procedimentos e adaptações estruturais sanitárias, 
                    que une direcionamentos de referências nacionais e internacionais.</div>
                </div>
                <div class="col">
                    <div class="text-title-section  minor-padding"> <img src="https://via.placeholder.com/60"> Passo a passo</div>
                    <div class="minor-padding">Quais são as etapas para retomada de atividades presenciais nas escolas da sua rede? 
                    Preparamos uma lista a partir da experiência de redes que já estão retornando suas atividades.</div>
                </div>
            </div>
            </div>
            <div class="subtitle-section"> Régua de protocolo </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]
    alert = data["overall_alert"].values[0]
    if alert == "altíssimo":
        url = "https://via.placeholder.com/300"
        caption = f"Seu nível de alerta é: <b>{alert}</b>. Há um crescente número de casos de Covid-19 e grande parte deles não são detectados."
    elif alert == "alto":
        url = "https://via.placeholder.com/300"
        caption = f"Seu nível de alerta é: <b>{alert}</b>. Há muitos casos de Covid-19 com transmissão comunitária. A presença de casos não detectados é provável."
    elif alert == "moderado":
        url = "https://via.placeholder.com/300"
        caption = f"Seu nível de alerta é: <b>{alert}</b>. Há um número moderado de casos e a maioria tem uma fonte de transmissão conhecida."
    elif alert == "novo normal":
        url = "https://via.placeholder.com/300"
        caption = f"Seu nível de alerta é: <b>{alert}</b>. Casos são raros e técnicas de rastreamento de contato e monitoramento de casos suspeitos evitam disseminação."
    else:
        url = "https://via.placeholder.com/300"
        caption = "Não há nível de alerta na sua cidade. Sugerimos que confira o nível de risco de seu estado."

    st.write(
        f"""
        <div class="container minor-padding">
            <div class="text-title-section">{caption}</div>
        </div>
        <div class="minor-padding">
            <img src={url}> 
        </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationResult():
    st.write(
        f"""
        <div class="container main-padding">
            <div>
                <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                <div class="row main-padding">
                    <div class="col">
                        <div class="card-simulator blue-bg">
                            <div class="card-title-section primary-span">EQUITATIVO</div>
                            <div class="text-small">Todos os alunos têm aula presencial ao menos 1 vez por semana.</div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">250</span> alunos retonam às aulas
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">100</span> professores retornam
                            </div>
                            <br>
                        </div>
                        <div class="card-simulator blue-bg minor-padding">
                            <div class="card-title-section primary-span">Materiais para compra</div>
                            <br>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">350</span> máscaras
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">3</span> termômetros
                            </div>
                            <div class="bold">
                                <img src="https://via.placeholder.com/30">
                                <span class="card-number">4.2</span> litros de álcool em gel
                            </div>
                        </div> 
                    </div>
                    <div class="col">
                        <div class="card-simulator dark-blue-bg light-span">
                            <div class="card-title-section">PRIORITÁRIO</div>
                            <div class="text-small">Máximo de alunos retorna 5 vezes por semana.</div>
                            <br>
                        </div>
                        <div class="card-simulator primary-blue-bg minor-padding">
                            <div class="card-title-section light-span">Materiais para compra</div>
                            <br>
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
                        <div>
                            Uma parte essencial da reabertura é definir <b>quem pode retornar e como</b> - trazemos abaixo 2 modelos possíveis.
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
                                        que por 1 dia. Atividades podem ser de reforço ou conteúdo.
                                    </div>
                                </div>
                            </div>
                            <div class="col light-blue-bg light-span card-simulator" style="border-radius:30px">
                            <div class="two-cols-icon-text">
                                <div class="card-title-section">PRIORITÁRIO</div>
                                <div class="text-subdescription">
                                    <b>Máximo de alunos têm aula presencial 5 vezes por semana.</b>
                                    <p></p>
                                    Prioriza-se o fechamento do ciclo escolar, com maior tempo na escola para 
                                    esses alunos. Atividades podem ser de reforço ou conteúdo.
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
        """,
        unsafe_allow_html=True
    )
    st.write(
        f"""
            <div class="text-title-section minor-padding"> Defina seu modelo de retorno </div>
            <div>
                <div class="text-padding bold">1. Para qual etapa de ensino você está planejando?</div>
            </div>
        """,
        unsafe_allow_html=True
    )
    data = df[df["city_name"] == session_state.city_name]
    data = df[df["administrative_level"] == session_state.administrative_level]
    education_phase = st.selectbox("", data["education_phase"].sort_values().unique())
    st.write(
        f"""
            <div class="text-padding bold">2. Utilize os filtros para os dados do Censo Escolar (2019):</div>
        """,
        unsafe_allow_html=True
    )
    rural = st.checkbox('Apenas escolas rurais')
    water_supply = st.checkbox('Apenas escolas com água encanada')
    st.write(
        f"""
        <div class="main-padding bold">3. Ou informe seus dados abaixo:</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    total_alunos = st.number_input('Qual total de alunos da sua rede?', format='%d', value=0, step=1)
    total_professores = st.number_input('Qual total de professores da sua rede?', format='%d', value=0, step=1)
    total_salas = st.number_input('Qual total de sala de aulas na sua rede?', format='%d', value=0, step=1)
    st.write(
        f"""
                <div class="main-padding bold">4.Escolha as condições de retorno:</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    alunos_porcentagem = st.slider('Alunos:', 0, 100)
    st.write(alunos_porcentagem, '% dos alunos retornando')
    
    professores_porcentagem = st.slider('Professores:', 0, 100)
    st.write(professores_porcentagem, '% dos professores retornando')

    alunos_sala = st.slider('Máximo de alunos na sala de aula:', 0, 30)
    st.write(alunos_sala, ' alunos por sala')
    if st.button("SIMULAR RETORNO"):
        if st.button("Esconder"):
            pass
        genSimulationResult()
    utils.stylizeButton(
        name="SIMULAR RETORNO",
        # style_string="""border: 1px solid var(--main-white);box-sizing: border-box;border-radius: 15px; width: auto;padding: 0.5em;text-transform: uppercase;font-family: var(--main-header-font-family);color: var(--main-white);background-color: var(--main-primary);font-weight: bold;text-align: center;text-decoration: none;font-size: 18px;animation-name: fadein;animation-duration: 3s;margin-top: 1em;""",
        style_string="""box-sizing: border-box;border-radius: 15px; width: 150px;padding: 0.5em;text-transform: uppercase;font-family: 'Oswald', sans-serif;background-color:  #0097A7;font-weight: bold;text-align: center;text-decoration: none;font-size: 18px;animation-name: fadein;animation-duration: 3s;margin-top: 1.5em;""",
        session_state=session_state,
    )



def genPrepareContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"> Prepare </div>
                <div class="left-margin">
                <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Ferramenta de verificação</div>
                <div class="minor-padding">Montamos essa ferramenta para reporte do resultado da inspeção da Vigilância Sanitária 
                nas unidades escolares e verifique se é necessário realizar alguma reforma pontual de adequação.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLSer8JIT3wZ5r5FD8vUao1cR8VrnR1cq60iPZfuvqwKENnEhCg/viewform?usp=sf_link" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
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
            <div class="title-section"> Monitore </div>
            <div class="left-margin">
                <div class="text-title-section minor-padding"> <img src="https://via.placeholder.com/60"> Plano de contigência</div>
                <div class="minor-padding">É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
                da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.</div>
                <div class="minor-padding">
                <img src="https://via.placeholder.com/300">
                </div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
                </div>
                <div class="text-title-section main-padding"> <img src="https://via.placeholder.com/60"> Ferramenta de notificação</div>
                <div class="minor-padding">lorem ipsum.</div>
                <div>
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
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
