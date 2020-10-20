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
           <div class="row">
            <div class="col">
                <div class="text-title-section  minor-padding">Protocolos</div>
                <div class="minor-padding">Encontre uma planilha de procedimentos e adaptações estruturais sanitárias, 
                que une direcionamentos de referências nacionais e internacionais.</div>
            </div>
            <div class="col">
                <div class="text-title-section  minor-padding">Passo-a-passo</div>
                <div class="minor-padding">Quais são as etapas para retomada de atividades presenciais nas escolas da sua rede? 
                Preparamos uma lista a partir da experiência de redes que já estão retornando suas atividades.</div>
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
            <div><br></div>
        </div>
        """,
        unsafe_allow_html=True
    )

def genPrepareContainer():
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"> Prepare </div>
            <div class="text-title-section minor-padding">Ferramenta de verificação</div>
            <div class="minor-padding">Montamos essa ferramenta para reporte do resultado da inspeção da Vigilância Sanitária 
            nas unidades escolares e verifique se é necessário realizar alguma reforma pontual de adequação.</div>
            <div>
            <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
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
            <div class="text-title-section minor-padding">Plano de contigência</div>
            <div class="minor-padding">É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
            da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.</div>
            <div>
            <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
            </div>
            <div class="text-title-section minor-padding">Ferramenta de notificação</div>
            <div class="minor-padding">lorem ipsum.</div>
            <div>
            <iframe class="container" src="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
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