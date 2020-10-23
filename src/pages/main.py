import streamlit as st
import yaml
import utils
import os
import pandas as pd


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
                <span class="hero-container-product primary-span">{title1}</span>
                <br>
                <span class="hero-container-product primary-span">{title2}</span>
                <br><br>
                <span class="hero-container-subtitle dark-span">{subtitle}</span>
                <br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question primary-span">Como preparar a minha rede escolar para um retorno presencial seguro?</span>
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
    session_state.city_name = st.selectbox(
        "Município", utils.filter_place(df, "city", state_id=session_state.state_id)
    )
    session_state.administrative_level = st.selectbox(
        "Nível de Administração",
        utils.filter_place(
            df,
            "administrative_level",
            city_name=session_state.city_name,
            state_id=session_state.state_id,
        ),
    )


def genPlanContainer():
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
                    <div class="text-title-section  minor-padding"> <img src="https://via.placeholder.com/60"> Passo-a-passo</div>
                    <div class="minor-padding">Quais são as etapas para retomada de atividades presenciais nas escolas da sua rede? 
                    Preparamos uma lista a partir da experiência de redes que já estão retornando suas atividades.</div>
                </div>
            </div>
            </div>
            <div class="subtitle-section"> Régua de protocolo </div>
            <div class="minor-padding">
                <img src="https://via.placeholder.com/300">
            </div>
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
                            <br>
                        </div>
                        <div class="card-simulator light-blue-bg minor-padding">
                            <div class="card-title-section primary-span">Materiais para compra</div>
                            <br>
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


def genSimulationContainer(session_state):

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"> Simule o retorno </div>
                <div class="left-margin">
                    <div class="bold minor-padding">Como calcular os recursos necessários para a retomada?</div>
                    <div class="minor-padding">Uma parte essencial da reabertura é contabilizar 
                    quais materiais devem ser providenciados para as escolas.</div>
                    <div class="minor-padding">
                        <div class="subtitle-section minor-padding"> ENTENDA OS MODELOS DE RETORNO </div>
                        <div>
                            Uma parte essencial da reabertura é definir 
                            <b>quem pode retornar e como</b> - trazemos 2 modelos possíveis:
                        </div>
                        <div class="row main-padding" style="grid-gap: 1rem;">
                            <div class="col blue-bg card-simulator" style="border-radius:30px;">
                                <div class="two-cols-icon-text">
                                    <div class="card-title-section">EQUITATIVO</div>
                                    <div>
                                        <b>Todos os alunos têm aula presencial ao menos 1 vez por semana.</b>
                                        <p></p>
                                        Prioriza-se de forma igualitária que alunos voltem para a escola, mesmo  
                                        que somente 1 dia. Atividades podem ser de reforço ou conteúdo.
                                    </div>
                                </div>
                            </div>
                            <div class="col dark-blue-bg light-span card-simulator" style="border-radius:30px">
                            <div class="two-cols-icon-text">
                                <div class="card-title-section">PRIORITÁRIO</div>
                                <div>
                                    <b>Máximo de alunos retorna 5 vezes por semana.</b>
                                    <p></p>
                                    Prioriza-se o fechamento do ciclo escolar, com maior tempo na escola para 
                                    esses alunos. Atividades podem ser de reforço ou conteúdo.
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="subtitle-section minor-padding"> DEFINA SEU MODELO DE RETORNO </div>
                        <div>
                            <div class="minor-padding bold">1. Para qual etapa de ensino você está planejando?</div>
                            <div>[Caixa de seleção]</div>
                        </div>
                        <div>
                        <div class="main-padding bold">2. Utilize os filtros para os dados do Censo Escolar (2019):</div>
                            <div class="row">
                                <div class="col minor-padding">
                                    <input type="checkbox" id="rural_schools">
                                    <label for="rural_schools"> Apenas escolas rurais</label>
                                </div>
                                <div class="col minor-padding">
                                    <input type="checkbox" id="in_water">
                                    <label for="rural_schools"> Apenas escolas com água encanada</label>
                                </div>
                            </div>
                        </div>
                        <div class="main-padding bold">3. Ou informe seus dados abaixo:</div>
                        </div>
                        <div class="minor-padding">
                            <div class="row">
                                <div class="col">
                                    <p>Qual total de alunos da sua rede?</p>
                                    [input textual]
                                </div>
                                <div class="col">
                                    <p>Qual total de professores da sua rede?</p>
                                    [input textual]
                                </div>
                                <div class="col">
                                    <p>Qual total de sala de aulas na sua rede?</p>
                                    [input textual]
                                </div>
                            </div>
                        </div>
                        <div class="main-padding bold">4.Escolha as condições de retorno:</div>
                        <div class="minor-padding">
                            <div class="row">
                                <div class="col">
                                    <p>% de alunos que retornam:</p>
                                    [seletor slide]
                                </div>
                                <div class="col">
                                    % de professores que retornam:
                                    <br>
                                    [seletor slide]
                                </div>
                                <div class="col">
                                    <p>Máximo de alunos por sala:</p>
                                    [seletor slide]
                                </div>
                            </div>
                        </div>
                    </div>             
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
                <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
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
    genPlanContainer()
    genSimulationContainer(session_state)
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()


if __name__ == "__main__":
    main()
