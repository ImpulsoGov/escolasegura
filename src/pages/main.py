import streamlit as st
import yaml

import utils

def genHeroSection(title1: str, title2: str, subtitle: str,header: bool):

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

def genSelectBox():
    user_input = dict()
    states = ("Todos","UF1", "UF2")
    options = list(range(len(states)))

    #user_input["state_name"] = st.selectbox("Estado", options, format_func=lambda x: states[x])
    #user_input["city_name"] = st.selectbox("Município", [])
    #user_input["teaching_level"] = st.selectbox("Nível de ensino", [])

    st.write(
        f"""
        <div class="container main-padding">
            <div class="text-title-section"> Selecione sua rede </div>
            <div class="row"> 
                <div class="col">
                <div>{"state_name"}</div>
                </div>
                <div class="col">
                <div>{"city_name"}</div>
                </div>
                <div class="col">
                <div>{"teaching_level"}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
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
        </div>
        """,
        unsafe_allow_html=True
    )

def genSimulationContainer():

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
                        <div class="row main-padding">
                            <div class="col blue-bg" style="border-radius:30px;">
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
                            <div class="col dark-blue-bg light-span" style="border-radius:30px">
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
                        <div class="minor-padding">Para qual etapa de ensino você está planejando?</div>
                        <div><b>[box]</b></div>
                        <div class="minor-padding">Quais as restrições que deseja para considerar para o retorno?</div>
                        <div class="minor-padding">[3 cols]</div>
                        <div class="minor-padding blue-bg" style="border-radius:10px">
                            <div class="left-margin">
                                <b> ⚠️ Utilizamos por padrão os dados abertos do Censo Escolar 2019 (INEP).</b>
                                <br>
                                Você pode alterar esses dados abaixo. 
                            </div>
                        </div>
                        <div class="minor-padding">[3 cols]</div>
                        <div>[3 cols]</div>
                    </div>
                    <div>
                        <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                        <div class="row main-padding">
                            <div class="col blue-bg">
                               <div class="card-title-section primary-span">EQUITATIVO</div>
                               <div class="text-small">Todos os alunos têm aula presencial ao menos 1 vez por semana.</div>
                            </div>
                            <div class="col light-blue-bg">
                               <div class="card-title-section primary-span">Materiais para compra</div>
                            </div> 
                        </div>
                        <div class="row minor-padding">
                            <div class="col dark-blue-bg light-span">
                                <div class="card-title-section">PRIORITÁRIO</div>
                               <div class="text-small">Máximo de alunos retorna 5 vezes por semana.</div>
                            </div>
                            <div class="col primary-blue-bg">
                               <div class="card-title-section light-span">Materiais para compra</div>
                            </div>
                        </div>
                    </div>
                    <div class="minor-padding">[veja mais]</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
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
        unsafe_allow_html=True
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
        unsafe_allow_html=True
    )


def genFooterContainer():
    st.write(
        f"""
        <div class="container">
            <div class="text-title-footer main-padding"> Realizado por </div>
            <br>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    utils.localCSS("src/style.css")
    genHeroSection(
        title1="Escola",
        title2="Possível",
        subtitle="{descrição}",
        header=True,
    )
    genSelectBox()
    genPlanContainer()
    genSimulationContainer()
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()
    

if __name__ == "__main__":
    main()