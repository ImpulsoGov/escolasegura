import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout

from model.get_school_return_data import entrypoint


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
                <div>
                    <img class="logo-image" src="https://i.imgur.com/9Mq2b7m.png" title="Freepik"> 
                </div>
                <br><br>
            </div>
            <div class="col">
                <br><br><br>
                <span class="hero-container-question main-grey-span">
                Controle a Covid-19 e promova aulas presenciais seguras na rede pública.
                </span>
            </div>
            <br>
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
        options_city_name = utils.filter_place(df, "city", state_id=session_state.state_id)
        options_city_name = pd.DataFrame(data=options_city_name, columns=["city_name"])
        x = int(options_city_name[options_city_name["city_name"] == "Todos"].index.tolist()[0]) 
        session_state.city_name = st.selectbox(
            "Município", options_city_name, index=x
        )
    with col3:
        options_adiminlevel = utils.filter_place(df, "administrative_level", state_id=session_state.state_id, city_name=session_state.city_name)
        options_adiminlevel = pd.DataFrame(data=options_adiminlevel, columns=["adiminlevel"])
        y = int(options_adiminlevel[options_adiminlevel["adiminlevel"] == "Todos"].index.tolist()[0]) 
        session_state.administrative_level = st.selectbox(
            "Nível de Administração", options_adiminlevel, index=y
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


def genPlanContainer(df, config, session_state):

    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]

    if len(data["overall_alert"]) > 0:
        alert = data["overall_alert"].values[0]
        if session_state.city_name != "Todos":
            cidade = session_state.city_name
        else:
            cidade = session_state.state_id
        if alert == 3.0:
            href = "https://imgur.com/CYkwogu"
            url = href + ".jpg"
            caption = f"Em <b>{cidade}</b>, o nível de alerta é: <b>ALTÍSSIMO</b>. Há um crescente número de casos de Covid-19 e grande parte deles não são detectados."

        elif alert == 2.0:
            href = "https://imgur.com/tDJfCji"
            url = href + ".jpg"
            caption = f"Em <b>{cidade}</b>, nível de alerta é: <b>ALTO</b>. Há muitos casos de Covid-19 com transmissão comunitária. A presença de casos não detectados é provável."

        elif alert == 1.0:
            href = "https://imgur.com/Oc6NzxW"
            url = href + ".jpg"
            caption = f"Em <b>{cidade}</b>, nível de alerta é: <b>MODERADO</b>. Há um número moderado de casos e a maioria tem uma fonte de transmissão conhecida."

        elif alert == 0.0:
            href = "https://imgur.com/bQwNgo7"
            url = href + ".jpg"
            caption = f"Em <b>{cidade}</b>, nível de alerta é: <b>NOVO NORMAL</b>. Casos são raros e técnicas de rastreamento de contato e monitoramento de casos suspeitos evitam disseminação."
    else:
        href = "https://imgur.com/CYkwogu"
        url = ""
        caption = "Não há nível de alerta na sua cidade. Sugerimos que confira o nível de risco de seu estado."


    farol_covid = utils.get_config(config["br"]["farolcovid"]["config"])["br"]["farolcovid"]
    
    situation_classification = farol_covid["rules"]["situation_classification"]["cuts"]
    control_classification = farol_covid["rules"]["control_classification"]["cuts"]
    capacity_classification = farol_covid["rules"]["capacity_classification"]["cuts"]
    trust_classification = farol_covid["rules"]["trust_classification"]["cuts"]

    date_update = farol_covid["date_update"]

    modal = f"""
    <a href="#entenda-mais" class="info-btn">Entenda a classificação dos níveis</a>
    <div id="entenda-mais" class="info-modal-window">
        <div>
            <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
            <div style="margin: 10px 15px 15px 15px;">
            <h1 class="primary-span">Valores de referência</h1>
            <div style="font-size: 12px">
                <b>Atualizado em</b>: {date_update}<br>
            </div>
            <div class="info-div-table">
            <table class="info-table">
            <tbody>
                <tr>
                    <td class="grey-bg"><strong>Dimensão</strong></td>
                    <td class="grey-bg"><strong>Indicador</strong></td>
                    <td class="grey-bg"><strong>Novo Normal</strong></td>
                    <td class="grey-bg"><strong>Risco Moderado</strong></td>
                    <td class="grey-bg"><strong>Risco Alto</strong></td>
                    <td class="grey-bg"><strong>Risco Altíssimo</strong></td>
                </tr>
                <tr>
                    <td rowspan="2">
                    <p><span>Situação da doença</span></p><br/>
                    </td>
                    <td><span>Novos casos diários (Média móvel 7 dias)</span></td>
                    <td class="light-blue-bg bold"><span>x&lt;={situation_classification[1]}</span></td>
                    <td class="light-yellow-bg bold"><span>{situation_classification[1]}&lt;x&lt;={situation_classification[2]}</span></td>
                    <td class="light-orange-bg bold"><span>{situation_classification[2]}&lt;=x&lt;={situation_classification[3]}</span></td>
                    <td class="light-red-bg bold"><span>x &gt;= {situation_classification[3]} </span></td>
                </tr>
                <tr>
                    <td><span>Tendência de novos casos diários</span></td>
                    <td class="lightgrey-bg" colspan="4"><span>Se crescendo*, mover para o nível mais alto</span></td>
                </tr>
                <tr>
                    <td><span>Controle da doença</span></td>
                    <td><span>Número de reprodução efetiva</span></td>
                    <td class="light-blue-bg bold"><span>&lt;{control_classification[1]}</span></td>
                    <td class="light-yellow-bg bold"><span>&lt;{control_classification[1]} - {control_classification[2]}&gt;</span></td>
                    <td class="light-orange-bg bold"><span>&lt;{control_classification[2]} - {control_classification[3]}&gt;</span>&nbsp;</td>
                    <td class="light-red-bg bold"><span>&gt;{control_classification[3]}</span></td>
                </tr>
                <tr>
                    <td><span>Capacidade de respostas do sistema de saúde</span></td>
                    <td><span>Projeção de tempo para ocupação total de leitos UTI</span></td>
                    <td class="light-blue-bg bold">{capacity_classification[3]} - 90 dias</td>
                    <td class="light-yellow-bg bold"><span>{capacity_classification[2]} - {capacity_classification[3]} dias</span></td>
                    <td class="light-orange-bg bold"><span>{capacity_classification[1]} - {capacity_classification[2]} dias</span></td>
                    <td class="light-red-bg bold"><span>{capacity_classification[0]} - {capacity_classification[1]} dias</span></td>
                </tr>
                <tr>
                    <td><span>Confiança dos dados</span></td>
                    <td><span>Subnotificação (casos <b>não</b> diagnosticados a cada 10 infectados)</span></td>
                    <td class="light-blue-bg bold"><span>{int(trust_classification[0]*10)}&lt;=x&lt;{int(trust_classification[1]*10)}</span></td>
                    <td class="light-yellow-bg bold"><span>{int(trust_classification[1]*10)}&lt;=x&lt;{int(trust_classification[2]*10)}</span></td>
                    <td class="light-orange-bg bold"><span>{int(trust_classification[2]*10)}&lt;=x&lt;{int(trust_classification[3]*10)}</span></td>
                    <td class="light-red-bg bold"><span>{int(trust_classification[3]*10)}&lt;=x&lt;=10</span></td>
                </tr>
            </tbody>
            </table>
            </div>
            <div style="font-size: 12px">
                * Como determinamos a tendência:
                <ul class="sub"> 
                    <li> Crescendo: caso o aumento de novos casos esteja acontecendo por pelo menos 5 dias. </li>
                    <li> Descrescendo: caso a diminuição de novos casos esteja acontecendo por pelo menos 14 dias. </li>
                    <li> Estabilizando: qualquer outra mudança. </li>
                </ul>
            </div>
            <div style="font-size: 14px">
                Para mais detalhes confira nossa página de Metodologia no FarolCovid</a>.
            </div>
            </div>
        </div>
    </div>"""

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"> <img class="square" src="https://i.imgur.com/gGIFS5N.png">Planeje  
             <p>Planeje antecipadamente os principais passos para a reabertura da rede escolar.</p>              
            </div>
            <p><b>A fase de planejamento é essencial para uma reabertura segura.</b>
            Devem ser incluídos os diversos atores do dia-a-dia das escolas 
            para diálogo e formulação dos protocolos.</p>
            <div class="left-margin">
                <div class="row">
                    <div class="col">
                        <div class="text-title-section minor-padding"> 
                        <img class="icon" 
                        src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zOTUuMTMzLDIwMC4zNDhjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZWMTE2Ljg3YzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTYgIHMxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NnY2Ni43ODNDNDExLjgyOCwxOTIuODc1LDQwNC4zNTYsMjAwLjM0OCwzOTUuMTMzLDIwMC4zNDh6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjNWM1ZjY2Ij48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQxMS44MjgsMTgzLjY1MlYxMTYuODdjMC05LjIyMy03LjQ3My0xNi42OTYtMTYuNjk2LTE2LjY5NnYxMDAuMTc0ICBDNDA0LjM1NiwyMDAuMzQ4LDQxMS44MjgsMTkyLjg3NSw0MTEuODI4LDE4My42NTJ6IiBmaWxsPSIjNTM1NjVjIiBkYXRhLW9yaWdpbmFsPSIjNTM1NjVjIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQ0NS4yMiwxMzMuNTY1SDMyOC4zNWMtOS4yMjMsMC0xNi42OTYtNy40NzMtMTYuNjk2LTE2LjY5NlYxNi42OTYgIEMzMTEuNjU0LDcuNDczLDMxOS4xMjcsMCwzMjguMzUsMGgxMTYuODdjMzYuODIxLDAsNjYuNzc3LDI5Ljk1Niw2Ni43NzcsNjYuNzgzUzQ4Mi4wNCwxMzMuNTY1LDQ0NS4yMiwxMzMuNTY1eiIgZmlsbD0iIzVhNWE1ZiIgZGF0YS1vcmlnaW5hbD0iI2ZmZGUzMyIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00NDUuMjIsMGgtNTAuMDg3djEzMy41NjVoNTAuMDg3YzM2LjgyMSwwLDY2Ljc3Ny0yOS45NTYsNjYuNzc3LTY2Ljc4M1M0ODIuMDQsMCw0NDUuMjIsMHoiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiNmZmJjMzMiIGNsYXNzPSIiPjwvcGF0aD4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0yOTQuOTU5LDI2Ny4xM0gxODMuNjU0Yy05LjIyMywwLTE2LjY5Ni03LjQ3My0xNi42OTYtMTYuNjk2czcuNDczLTE2LjY5NiwxNi42OTYtMTYuNjk2aDExMS4zMDQgICBjOS4yMjMsMCwxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NlMzMDQuMTgzLDI2Ny4xMywyOTQuOTU5LDI2Ny4xM3oiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiM1YzVmNjYiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0xMDAuMTc2LDIwMC4zNDhjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZWMTE2Ljg3YzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTYgICBzMTYuNjk2LDcuNDczLDE2LjY5NiwxNi42OTZ2NjYuNzgzQzExNi44NzIsMTkyLjg3NSwxMDkuNCwyMDAuMzQ4LDEwMC4xNzYsMjAwLjM0OHoiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiM1YzVmNjYiPjwvcGF0aD4KPC9nPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xMTYuODcyLDE4My42NTJWMTE2Ljg3YzAtOS4yMjMtNy40NzMtMTYuNjk2LTE2LjY5Ni0xNi42OTZ2MTAwLjE3NCAgQzEwOS40LDIwMC4zNDgsMTE2Ljg3MiwxOTIuODc1LDExNi44NzIsMTgzLjY1MnoiIGZpbGw9IiM1MzU2NWMiIGRhdGEtb3JpZ2luYWw9IiM1MzU2NWMiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTAwLjE3Niw0MzQuMDg3Yy05LjIyMywwLTE2LjY5Ni03LjQ3My0xNi42OTYtMTYuNjk2di02Ni43ODNjMC05LjIyMyw3LjQ3My0xNi42OTYsMTYuNjk2LTE2LjY5NiAgczE2LjY5Niw3LjQ3MywxNi42OTYsMTYuNjk2djY2Ljc4M0MxMTYuODcyLDQyNi42MTQsMTA5LjQsNDM0LjA4NywxMDAuMTc2LDQzNC4wODd6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjNWM1ZjY2Ij48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTExNi44NzIsNDE3LjM5MXYtNjYuNzgzYzAtOS4yMjMtNy40NzMtMTYuNjk2LTE2LjY5Ni0xNi42OTZ2MTAwLjE3NCAgQzEwOS40LDQzNC4wODcsMTE2Ljg3Miw0MjYuNjE0LDExNi44NzIsNDE3LjM5MXoiIGZpbGw9IiM1MzU2NWMiIGRhdGEtb3JpZ2luYWw9IiM1MzU2NWMiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTgzLjY1NCwxMzMuNTY1SDE2LjY5OGMtOS4yMjMsMC0xNi42OTYtNy40NzMtMTYuNjk2LTE2LjY5NlYxNi42OTZDMC4wMDIsNy40NzMsNy40NzUsMCwxNi42OTgsMCAgaDE2Ni45NTdjOS4yMjMsMCwxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NlYxMTYuODdDMjAwLjM1LDEyNi4wOTIsMTkyLjg3OCwxMzMuNTY1LDE4My42NTQsMTMzLjU2NXoiIGZpbGw9IiMyYjE0ZjAiIGRhdGEtb3JpZ2luYWw9IiM1MGI5ZmYiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTAwLjE3NiwzNjcuMzA0Yy01NS4yMzQsMC0xMDAuMTc0LTQ0Ljk0LTEwMC4xNzQtMTAwLjE3NHM0NC45NC0xMDAuMTc0LDEwMC4xNzQtMTAwLjE3NCAgUzIwMC4zNSwyMTEuODk3LDIwMC4zNSwyNjcuMTNTMTU1LjQxLDM2Ny4zMDQsMTAwLjE3NiwzNjcuMzA0eiIgZmlsbD0iI2ZmOTE0MCIgZGF0YS1vcmlnaW5hbD0iI2VjNzgzOCIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xODMuNjU0LDUxMkgxNi42OThjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZ2LTc3LjkxMyAgYzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTZoMTY2Ljk1N2M5LjIyMywwLDE2LjY5Niw3LjQ3MywxNi42OTYsMTYuNjk2djc3LjkxM0MyMDAuMzUsNTA0LjUyNywxOTIuODc4LDUxMiwxODMuNjU0LDUxMnoiIGZpbGw9IiMyYjE0ZjAiIGRhdGEtb3JpZ2luYWw9IiM1MGI5ZmYiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTgzLjY1NCw0MDAuNjk2aC04My40NzhWNTEyaDgzLjQ3OGM5LjIyMywwLDE2LjY5Ni03LjQ3MywxNi42OTYtMTYuNjk2di03Ny45MTMgIEMyMDAuMzUsNDA4LjE2OSwxOTIuODc4LDQwMC42OTYsMTgzLjY1NCw0MDAuNjk2eiIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzQ4YTdlNiIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0yMDAuMzUsMjY3LjEzYzAtNTUuMjM0LTQ0Ljk0LTEwMC4xNzQtMTAwLjE3NC0xMDAuMTc0djIwMC4zNDggIEMxNTUuNDEsMzY3LjMwNCwyMDAuMzUsMzIyLjM2NCwyMDAuMzUsMjY3LjEzeiIgZmlsbD0iI2ZmOTE0NyIgZGF0YS1vcmlnaW5hbD0iI2RiNjMyYyIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xODMuNjU0LDBoLTgzLjQ3OHYxMzMuNTY1aDgzLjQ3OGM5LjIyMywwLDE2LjY5Ni03LjQ3MywxNi42OTYtMTYuNjk2VjE2LjY5NiAgQzIwMC4zNSw3LjQ3MywxOTIuODc4LDAsMTgzLjY1NCwweiIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzQ4YTdlNiIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zOTUuMTMzLDMzMy45MTNjLTMuMjI4LDAtNi40NTctMC45MzUtOS4yNjEtMi44MDVsLTEwMC4xNzQtNjYuNzgzICBjLTQuNjQ3LTMuMDk4LTcuNDM1LTguMzEtNy40MzUtMTMuODkxYzAtNS41ODEsMi43ODgtMTAuNzkzLDcuNDM1LTEzLjg5MWwxMDAuMTc0LTY2Ljc4M2M1LjYwOS0zLjczOSwxMi45MTQtMy43MzksMTguNTIyLDAgIGwxMDAuMTY4LDY2Ljc4M2M0LjY0MSwzLjA5OCw3LjQzNSw4LjMxLDcuNDM1LDEzLjg5MWMwLDUuNTgxLTIuNzk0LDEwLjc5My03LjQzNSwxMy44OTFsLTEwMC4xNjgsNjYuNzgzICBDNDAxLjU4OSwzMzIuOTc4LDM5OC4zNjIsMzMzLjkxMywzOTUuMTMzLDMzMy45MTN6IiBmaWxsPSIjOTlmZmRmIiBkYXRhLW9yaWdpbmFsPSIjN2JjYzI5IiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQwNC4zOTQsMzMxLjEwOGwxMDAuMTY4LTY2Ljc4M2M0LjY0MS0zLjA5OCw3LjQzNS04LjMxLDcuNDM1LTEzLjg5MSAgYzAtNS41ODEtMi43OTQtMTAuNzkzLTcuNDM1LTEzLjg5MWwtMTAwLjE2OC02Ni43ODNjLTIuODA1LTEuODctNi4wMzMtMi44MDUtOS4yNjEtMi44MDV2MTY2Ljk1NiAgQzM5OC4zNjIsMzMzLjkxMyw0MDEuNTg5LDMzMi45NzgsNDA0LjM5NCwzMzEuMTA4eiIgZmlsbD0iIzk5ZmZkNCIgZGF0YS1vcmlnaW5hbD0iIzZlYjgyNSIgY2xhc3M9IiI+PC9wYXRoPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8L2c+PC9zdmc+" 
                        title="Freepik" />
                         Passo a passo</div>
                        <div class="minor-padding"><br>
                        <b><i>O que é?</i><br>
                        Guia com 10 passos para uma reabertura segura da sua rede.</b> A ferramenta auxilia na criação de um plano de retomada com a inclusão da Secretaria de Saúde, comunidade escolar e outros atores.<br><br>
                        <b><i>Quem usa?</i></b>
                        <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br>
                        </div>
                    </div>
                    <div class="col">
                        <div class="text-title-section minor-padding"> 
                        <img class="icon" 
                        src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDQ2NCA0NjQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00MjAuNDc0LDEyNC44bC00Mi40LTIwLjh2MzUybDU5LjItMjk2QzQ0MC40NzQsMTQ1LjYsNDMzLjI3NCwxMzEuMiw0MjAuNDc0LDEyNC44eiIgZmlsbD0iIzk5ZmZkNCIgZGF0YS1vcmlnaW5hbD0iIzAwZjJhOSIgY2xhc3M9IiI+PC9wYXRoPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPHBhdGggc3R5bGU9IiIgZD0iTTQyMy42NzQsODUuNmwtMzguNC0xOS4yYy0yLjQtMTkuMi0xOS4yLTM0LjQtMzkuMi0zNC40aC0xODQuOGMtNC0xOC40LTIwLTMyLTM5LjItMzJoLTMyICAgYy0xOS4yLDAtMzYsMTQuNC0zOS4yLDMyLjhjLTE4LjQsMy4yLTMyLjgsMjAtMzIuOCwzOS4ydjM1MmMwLDIyLjQsMTcuNiw0MCw0MCw0MGgyODhjMjEuNiwwLDQwLTE2LjgsNDAtMzguNGwwLDBsNTkuMi0yOTYgICBDNDQ4LjQ3NCwxMTIsNDM5LjY3NCw5My42LDQyMy42NzQsODUuNnogTTkwLjA3NCwxNmgzMmMxMC40LDAsMTkuMiw2LjQsMjIuNCwxNmgtNzYuOEM3MC44NzQsMjIuNCw3OS42NzQsMTYsOTAuMDc0LDE2eiAgICBNMzcwLjA3NCw0MjRjMCwxMy42LTEwLjQsMjQtMjQsMjRoLTg4di0yNGMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYyNGgtMTZ2LTU2YzAtNC44LTMuMi04LTgtOHMtOCwzLjItOCw4djU2aC0xNnYtMjQgICBjMC00LjgtMy4yLTgtOC04cy04LDMuMi04LDh2MjRoLTgwdi0yNGMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYyNGgtMjRjLTEzLjYsMC0yNC0xMC40LTI0LTI0VjcyYzAtMTMuNiwxMC40LTI0LDI0LTI0aDg4djE1MiAgIGMwLDEzLjYtMTAuNCwyNC0yNCwyNHMtMjQtMTAuNC0yNC0yNFY3MmMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYxMjhjMCwyMi40LDE3LjYsNDAsNDAsNDBzNDAtMTcuNiw0MC00MFY0OGgxODQgICBjMTMuNiwwLDI0LDEwLjQsMjQsMjRWNDI0eiBNNDI5LjI3NCwxMjYuNGwtNDMuMiwyMTYuOFY4NC44bDMwLjQsMTUuMkM0MjYuMDc0LDEwNC44LDQzMS42NzQsMTE2LDQyOS4yNzQsMTI2LjR6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCw5NmgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsOTYsMzE0LjA3NCw5NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0zMTQuMDc0LDE2MGgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsMTYwLDMxNC4wNzQsMTYweiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTIxOC4wNzQsMjQwaDMyYzQuOCwwLDgtMy4yLDgtOHMtMy4yLTgtOC04aC0zMmMtNC44LDAtOCwzLjItOCw4ICAgQzIxMC4wNzQsMjM2LjgsMjEzLjI3NCwyNDAsMjE4LjA3NCwyNDB6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwyMjRoLTMyYy00LjgsMC04LDMuMi04LDhjMCw0LjgsMy4yLDgsOCw4aDMyYzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDIyNCwzMTQuMDc0LDIyNHoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0xODYuMDc0LDMyMGgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzE5MC44NzQsMzIwLDE4Ni4wNzQsMzIweiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTMxNC4wNzQsMzIwaC05NmMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGg5NmM0LjgsMCw4LTMuMiw4LThTMzE4Ljg3NCwzMjAsMzE0LjA3NCwzMjB6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwxOTJoLTk2Yy00LjgsMC04LDMuMi04LDhzMy4yLDgsOCw4aDk2YzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDE5MiwzMTQuMDc0LDE5MnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0yNTguMDc0LDI5NmMwLTQuOC0zLjItOC04LThoLTE2MGMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGgxNjAgICBDMjU0Ljg3NCwzMDQsMjU4LjA3NCwzMDAuOCwyNTguMDc0LDI5NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0zMTQuMDc0LDI4OGgtMzJjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoMzJjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsMjg4LDMxNC4wNzQsMjg4eiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTIxOC4wNzQsMTQ0aDMyYzQuOCwwLDgtMy4yLDgtOHMtMy4yLTgtOC04aC0zMmMtNC44LDAtOCwzLjItOCw4UzIxMy4yNzQsMTQ0LDIxOC4wNzQsMTQ0eiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTMxNC4wNzQsMTI4aC0zMmMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGgzMmM0LjgsMCw4LTMuMiw4LThTMzE4Ljg3NCwxMjgsMzE0LjA3NCwxMjh6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwyNTZoLTk2Yy00LjgsMC04LDMuMi04LDhzMy4yLDgsOCw4aDk2YzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDI1NiwzMTQuMDc0LDI1NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8L2c+PC9zdmc+"
                        title="Freepik" />
                         Protocolos</div>
                        <div class="minor-padding"><br>
                            <b><i>O que é?</i><br>
                            Listas de orientações para planejar a estrutura sanitária nas escolas</b>
                            A ferramenta fornece também rotinas a serem seguidas dentro e fora da sala de aula.<br><br>
                            <b><i>Quem usa?</i></b>
                            <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual
                            <li> Diretores(as) de escolas.
                        </div>
                    </div>
                </div><br>
                <div class="text-title-section"> Régua de protocolo </div>
                <div class="minor-padding">
                    <b><i>O que é?</i> Ferramenta de indicação das principais ações a serem tomadas no ambiente escolar para cada nível de alerta.<br><br>
                </div>
                <p>{caption}</p>{modal}
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

def genSimulationResult(params, config):

    result = entrypoint(params, config)

    st.write(
        f"""
        <div class="container main-padding">
                <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                <div class="bold"> Metodologia </div>
                <div class="row">
                    <div class="col main-padding">
                        <div class="card-simulator lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span uppercase">EQUITATIVO</div>
                            <div>Todos os alunos têm aula presencial ao menos 1 vez por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087166.svg" title="Freepik"> </div>
                                <div class="div2 card-number">{result["equitative"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087177.svg" title="Freepik"> </div>
                                <div class="div2"> <span class="card-number">{result["equitative"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold"> professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra 
                            <img style="width:1rem;"
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI1NiAwYy0xNDEuMTY0MDYyIDAtMjU2IDExNC44MzU5MzgtMjU2IDI1NnMxMTQuODM1OTM4IDI1NiAyNTYgMjU2IDI1Ni0xMTQuODM1OTM4IDI1Ni0yNTYtMTE0LjgzNTkzOC0yNTYtMjU2LTI1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMjE5NmYzIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtMzY4IDI3Ny4zMzIwMzFoLTkwLjY2Nzk2OXY5MC42Njc5NjljMCAxMS43NzczNDQtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzFzLTIxLjMzMjAzMS05LjU1NDY4Ny0yMS4zMzIwMzEtMjEuMzMyMDMxdi05MC42Njc5NjloLTkwLjY2Nzk2OWMtMTEuNzc3MzQ0IDAtMjEuMzMyMDMxLTkuNTU0Njg3LTIxLjMzMjAzMS0yMS4zMzIwMzFzOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFoOTAuNjY3OTY5di05MC42Njc5NjljMC0xMS43NzczNDQgOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFzMjEuMzMyMDMxIDkuNTU0Njg3IDIxLjMzMjAzMSAyMS4zMzIwMzF2OTAuNjY3OTY5aDkwLjY2Nzk2OWMxMS43NzczNDQgMCAyMS4zMzIwMzEgOS41NTQ2ODcgMjEuMzMyMDMxIDIxLjMzMjAzMXMtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzF6bTAgMCIgZmlsbD0iI2ZhZmFmYSIgZGF0YS1vcmlnaW5hbD0iI2ZhZmFmYSIgc3R5bGU9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                            title="Freepik" />
                            </div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937325.svg" title="Freepik"></div>
                                <div class="div2 card-number"> {result["equitative"]["total_masks"]} </div>
                                <div class="div3 bold"> máscaras por semana</div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2622/2622386.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["equitative"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937355.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["equitative"]["total_sanitizer"]} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana</div>
                            </div>
                        </div> 
                    </div>
                    <div class="col main-padding">
                        <div class="card-simulator lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span">PRIORITÁRIO</div>
                            <div>Máximo de alunos retorna 5 vezes por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087166.svg" title="Freepik"> </div>
                                <div class="div2 card-number">{result["priority"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087177.svg" title="Freepik"> </div>
                                <div class="div2"> <span class="card-number">{result["priority"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold">  professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra 
                            <img style="width:1rem;"
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI1NiAwYy0xNDEuMTY0MDYyIDAtMjU2IDExNC44MzU5MzgtMjU2IDI1NnMxMTQuODM1OTM4IDI1NiAyNTYgMjU2IDI1Ni0xMTQuODM1OTM4IDI1Ni0yNTYtMTE0LjgzNTkzOC0yNTYtMjU2LTI1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMjE5NmYzIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtMzY4IDI3Ny4zMzIwMzFoLTkwLjY2Nzk2OXY5MC42Njc5NjljMCAxMS43NzczNDQtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzFzLTIxLjMzMjAzMS05LjU1NDY4Ny0yMS4zMzIwMzEtMjEuMzMyMDMxdi05MC42Njc5NjloLTkwLjY2Nzk2OWMtMTEuNzc3MzQ0IDAtMjEuMzMyMDMxLTkuNTU0Njg3LTIxLjMzMjAzMS0yMS4zMzIwMzFzOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFoOTAuNjY3OTY5di05MC42Njc5NjljMC0xMS43NzczNDQgOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFzMjEuMzMyMDMxIDkuNTU0Njg3IDIxLjMzMjAzMSAyMS4zMzIwMzF2OTAuNjY3OTY5aDkwLjY2Nzk2OWMxMS43NzczNDQgMCAyMS4zMzIwMzEgOS41NTQ2ODcgMjEuMzMyMDMxIDIxLjMzMjAzMXMtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzF6bTAgMCIgZmlsbD0iI2ZhZmFmYSIgZGF0YS1vcmlnaW5hbD0iI2ZhZmFmYSIgc3R5bGU9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                            title="Freepik" /></div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937325.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_masks"]} </div>
                                <div class="div3 bold" > máscaras por semana </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2622/2622386.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937355.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_sanitizer"]} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>               
            <div class="minor-padding">
                <div class="minor-padding lighter-blue-green-bg" style="border-radius:5px;">
                    <div style="padding:10px;">
                        <img class = "icon-cards"
                         src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI1NiAwYy0xNDEuMTY0MDYyIDAtMjU2IDExNC44MzU5MzgtMjU2IDI1NnMxMTQuODM1OTM4IDI1NiAyNTYgMjU2IDI1Ni0xMTQuODM1OTM4IDI1Ni0yNTYtMTE0LjgzNTkzOC0yNTYtMjU2LTI1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMjE5NmYzIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtMzY4IDI3Ny4zMzIwMzFoLTkwLjY2Nzk2OXY5MC42Njc5NjljMCAxMS43NzczNDQtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzFzLTIxLjMzMjAzMS05LjU1NDY4Ny0yMS4zMzIwMzEtMjEuMzMyMDMxdi05MC42Njc5NjloLTkwLjY2Nzk2OWMtMTEuNzc3MzQ0IDAtMjEuMzMyMDMxLTkuNTU0Njg3LTIxLjMzMjAzMS0yMS4zMzIwMzFzOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFoOTAuNjY3OTY5di05MC42Njc5NjljMC0xMS43NzczNDQgOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFzMjEuMzMyMDMxIDkuNTU0Njg3IDIxLjMzMjAzMSAyMS4zMzIwMzF2OTAuNjY3OTY5aDkwLjY2Nzk2OWMxMS43NzczNDQgMCAyMS4zMzIwMzEgOS41NTQ2ODcgMjEuMzMyMDMxIDIxLjMzMjAzMXMtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzF6bTAgMCIgZmlsbD0iI2ZhZmFmYSIgZGF0YS1vcmlnaW5hbD0iI2ZhZmFmYSIgc3R5bGU9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                         title="Freepik" /> <b>Veja mais materiais necessários para compra 
                        <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0">
                        aqui</a>.</b>
                    </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )


def genSimulationContainer(df, config, session_state):
    st.write(
        f"""
        <div class="container main-padding">
            <div class="text-title-section"> Simule o retorno </div>
                <div >
                    <div class="minor-padding">Analise qual o modelo de retorno mais adequado para sua realidade e calcule os recursos necessários para a retomada.
                    </div>
                    <div class="minor-padding">
                        <div class="text-title-section minor-padding" style="font-size:20px"> Entenda os modelos de retorno </div>
                            <div>
                                Uma parte essencial da reabertura é definir 
                                <b>quem pode retornar e como</b> - trazemos 2 modelos possíveis:
                            </div>
                        <div class="row main-padding" style="grid-gap: 1rem;">
                            <div class="col lighter-blue-green-bg card-simulator" style="border-radius:30px;">
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
                            <div class="col light-blue-green-bg card-simulator" style="border-radius:30px">
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
                <div class="text-title-section minor-padding" style="font-size:20px">Defina seu modelo de retorno</div><br>
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
            "Percentual de professores realizando atividades presenciais:",
            0,
            100,
            100,
            10,
        )
        params["number_teachers"] = int(perc_teachers * params["number_teachers"] / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_teachers)}% dos alunos</i> - {str(params["number_teachers"])} professores no total.<br><hr>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3_4 = col3_2

    with col3_5:
        st.write(
            f"""<div class="minor-padding"> </div>""", unsafe_allow_html=True,
        )

        params["max_students_per_class"] = st.slider("Máximo de alunos por sala:", 0, 20, 20, 1)

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

    with st.beta_expander("SIMULAR RETORNO"):
        genSimulationResult(params, config)

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
            <div class="title-section"><img class="square" src="https://i.imgur.com/gGIFS5N.png">Prepare 
            <p>Prepare os protocolos de segurança, de acompanhamento e canais de comunicação para a reabertura das escolas.</p>
            </div>
            <p><b>A fase de preparação é onde os protocolos de segurança das escolas são discutidas e pactuadas.</b> 
            Durante a reabertura, é importante que seja estabelecida uma rotina de verificação das unidades escolares 
            para acompanhar o cumprimento dos protocolos estabelecidos.</p>
                <div class="left-margin">
                    <div class="text-title-section minor-padding"> 
                    <img class="icon"
                    src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zNTQuNjY5LDE2NC4wNTVjLTY1LjMyNiwwLTUwLjIyOC0yOS43NDMtOTguNjY5LTI5Ljc0M3MtMzMuMzQzLDI5Ljc0My05OC42NjksMjkuNzQzICBsMzAuNjQ5LDExMi4wNDloMTM2LjAzOEwzNTQuNjY5LDE2NC4wNTV6IiBmaWxsPSIjM2M0NzRkIiBkYXRhLW9yaWdpbmFsPSIjM2M0NzRkIiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iMTExLjY4MiIgY3k9IjI2Ni4wMDciIHI9IjExMS42ODIiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiM0NjUwNTkiIGNsYXNzPSIiPjwvY2lyY2xlPgo8Y2lyY2xlIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgY3g9IjExMS42ODIiIGN5PSIyNjYuMDA3IiByPSI3Ni4yOTUiIGZpbGw9IiM5OWZmZDQiIGRhdGEtb3JpZ2luYWw9IiMzYWM3YjQiIGNsYXNzPSIiPjwvY2lyY2xlPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xMzIuMjg5LDMyMS43MDRjLTQyLjEzNywwLTc2LjI5Ni0zNC4xNTktNzYuMjk2LTc2LjI5NmMwLTE1LjgwMiw0LjgwNS0zMC40ODMsMTMuMDMyLTQyLjY2MSAgYy0yMC4yOTQsMTMuNzEyLTMzLjYzNSwzNi45My0zMy42MzUsNjMuMjY0YzAsNDIuMTM3LDM0LjE1OSw3Ni4yOTYsNzYuMjk2LDc2LjI5NmMyNi4zMzUsMCw0OS41NTMtMTMuMzQyLDYzLjI2NC0zMy42MzUgIEMxNjIuNzcyLDMxNi45LDE0OC4wOTEsMzIxLjcwNCwxMzIuMjg5LDMyMS43MDR6IiBmaWxsPSIjMDBhZDk0IiBkYXRhLW9yaWdpbmFsPSIjMDBhZDk0IiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iNDAwLjMxOCIgY3k9IjI2Ni4wMDciIHI9IjExMS42ODIiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiM0NjUwNTkiIGNsYXNzPSIiPjwvY2lyY2xlPgo8Y2lyY2xlIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgY3g9IjQwMC4zMTgiIGN5PSIyNjYuMDA3IiByPSI3Ni4yOTUiIGZpbGw9IiM5OWZmZDQiIGRhdGEtb3JpZ2luYWw9IiMzYWM3YjQiIGNsYXNzPSIiPjwvY2lyY2xlPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00MjAuOTE5LDMyMS43MDRjLTQyLjEzNywwLTc2LjI5Ni0zNC4xNTktNzYuMjk2LTc2LjI5NmMwLTE1LjgwMiw0LjgwNS0zMC40ODMsMTMuMDMyLTQyLjY2MSAgYy0yMC4yOTQsMTMuNzEyLTMzLjYzNSwzNi45My0zMy42MzUsNjMuMjY0YzAsNDIuMTM3LDM0LjE1OSw3Ni4yOTYsNzYuMjk2LDc2LjI5NmMyNi4zMzUsMCw0OS41NTMtMTMuMzQyLDYzLjI2NC0zMy42MzUgIEM0NTEuNDAyLDMxNi45LDQzNi43MjIsMzIxLjcwNCw0MjAuOTE5LDMyMS43MDR6IiBmaWxsPSIjMDBhZDk0IiBkYXRhLW9yaWdpbmFsPSIjMDBhZDk0IiBjbGFzcz0iIj48L3BhdGg+CjxjaXJjbGUgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBjeD0iMjU2IiBjeT0iMTg2LjE5OSIgcj0iMTYuMzE1IiBmaWxsPSIjZmY5MTQ3IiBkYXRhLW9yaWdpbmFsPSIjZGE1YjY1IiBjbGFzcz0iIj48L2NpcmNsZT4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg=="
                    title="Freepik" />
                     Ferramenta de verificação</div>
                    <br>
                    <div class="grid-container-verification">
                        <div class="div1-verification">
                            <div>
                            <b><i>O que é?</b></i><br>
                            Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
                            <br><br>
                            <b><i>Quem usa?</b></i>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).
                            <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.
                            </div>
                        </div>
                        <div class="div2-verification">
                            <a href="https://docs.google.com/forms/u/3/d/e/1FAIpQLSer8JIT3wZ5r5FD8vUao1cR8VrnR1cq60iPZfuvqwKENnEhCg/viewform">
                            <img class="img-forms" src="https://i.imgur.com/gRSIBoh.png"> 
                            </a>
                        </div>
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
            <div class="title-section">
            <img class="square" src="https://i.imgur.com/gGIFS5N.png">Monitore
                <p>Após a reabertura, monitore a Covid-19 nas escolas e saiba o que fazer com o surgimento de algum caso.</p>
            </div>
            <div class="left-margin">
                <div class="text-title-section minor-padding"> 
                    <img class="icon"
                    src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDQ4MCA0ODAiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPHBvbHlnb24gc3R5bGU9IiIgcG9pbnRzPSIzNDQsNDAgMjcyLDQwIDI3Miw3MiAzMTIsNzIgMzEyLDQ0MCA1Niw0NDAgNTYsNzIgOTYsNzIgOTYsNDAgMjQsNDAgMjQsNDcyIDM0NCw0NzIgICIgZmlsbD0iIzVhNWE1YSIgZGF0YS1vcmlnaW5hbD0iI2JjYmNiYyIgY2xhc3M9IiI+PC9wb2x5Z29uPgoJPHBhdGggc3R5bGU9IiIgZD0iTTk2LDgwaDE3NnYtOFY0MGgtNTZjMC0xNy42NzItMTQuMzI4LTMyLTMyLTMycy0zMiwxNC4zMjgtMzIsMzJIOTZ2MzJWODB6IiBmaWxsPSIjNWE1YTVhIiBkYXRhLW9yaWdpbmFsPSIjYmNiY2JjIiBjbGFzcz0iIj48L3BhdGg+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik05Niw4MHYtOEg1NnYzNjhoMjU2VjcyaC00MHY4SDk2eiBNODgsMzc2aDE5Mkg4OHogTTI4MCwyMjRjMCw1My4wMTYtNDIuOTg0LDk2LTk2LDk2ICAgcy05Ni00Mi45ODQtOTYtOTZzNDIuOTg0LTk2LDk2LTk2UzI4MCwxNzAuOTg0LDI4MCwyMjR6IiBmaWxsPSIjZmZmZmZmIiBkYXRhLW9yaWdpbmFsPSIjZmZmZmZmIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMTg0LDEyOGMtNTMuMDE2LDAtOTYsNDIuOTg0LTk2LDk2czQyLjk4NCw5Niw5Niw5NnM5Ni00Mi45ODQsOTYtOTZTMjM3LjAxNiwxMjgsMTg0LDEyOHogTTI0OCwyNDggICBoLTQwdjQwaC00OHYtNDBoLTQwdi00OGg0MHYtNDBoNDh2NDBoNDBWMjQ4eiIgZmlsbD0iI2ZmZmZmZiIgZGF0YS1vcmlnaW5hbD0iI2ZmZmZmZiIgY2xhc3M9IiI+PC9wYXRoPgo8L2c+Cjxwb2x5Z29uIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgcG9pbnRzPSIyMDgsMTYwIDE2MCwxNjAgMTYwLDIwMCAxMjAsMjAwIDEyMCwyNDggMTYwLDI0OCAxNjAsMjg4IDIwOCwyODggMjA4LDI0OCAyNDgsMjQ4IDI0OCwyMDAgICAyMDgsMjAwICIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzA2YjBjNyIgY2xhc3M9IiI+PC9wb2x5Z29uPgo8cG9seWdvbiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIHBvaW50cz0iNDU2LDI1NiA0NTYsODAgNDMyLDgwIDQwOCw4MCA0MDgsOTYgNDA4LDI1NiAiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiNiY2JjYmMiIGNsYXNzPSIiPjwvcG9seWdvbj4KPHJlY3QgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4PSI0MDgiIHk9IjI1NiIgc3R5bGU9IiIgd2lkdGg9IjQ4IiBoZWlnaHQ9IjMyIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMDZiMGM3IiBjbGFzcz0iIj48L3JlY3Q+Cjxwb2x5Z29uIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgcG9pbnRzPSI0MDgsNDA4IDQzMiw0NjQgNDU2LDQwOCA0NTYsMjg4IDQwOCwyODggIiBmaWxsPSIjNWE1YTVhIiBkYXRhLW9yaWdpbmFsPSIjYmNiY2JjIiBjbGFzcz0iIj48L3BvbHlnb24+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTI0LDQ4MGgzMjBjNC40MTYsMCw4LTMuNTg0LDgtOFY0MGMwLTQuNDE2LTMuNTg0LTgtOC04aC03MmgtNDguODA4QzIxOS40OCwxMy43NjgsMjAzLjMyLDAsMTg0LDBzLTM1LjQ4LDEzLjc2OC0zOS4xOTIsMzIgIEg5NkgyNGMtNC40MTYsMC04LDMuNTg0LTgsOHY0MzJDMTYsNDc2LjQxNiwxOS41ODQsNDgwLDI0LDQ4MHogTTk2LDg4aDE3NmM0LjQxNiwwLDgtMy41ODQsOC04aDI0djM1Mkg2NFY4MGgyNCAgQzg4LDg0LjQxNiw5MS41ODQsODgsOTYsODh6IE0xNTIsNDhjNC40MTYsMCw4LTMuNTg0LDgtOGMwLTEzLjIzMiwxMC43NjgtMjQsMjQtMjRzMjQsMTAuNzY4LDI0LDI0YzAsNC40MTYsMy41ODQsOCw4LDhoNDh2MjRIMTA0ICBWNDhIMTUyeiBNMzIsNDhoNTZ2MTZINTZjLTQuNDE2LDAtOCwzLjU4NC04LDh2MzY4YzAsNC40MTYsMy41ODQsOCw4LDhoMjU2YzQuNDE2LDAsOC0zLjU4NCw4LThWNzJjMC00LjQxNi0zLjU4NC04LTgtOGgtMzJWNDhoNTYgIHY0MTZIMzJWNDh6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTEyMCwyNTZoMzJ2MzJjMCw0LjQxNiwzLjU4NCw4LDgsOGg0OGM0LjQxNiwwLDgtMy41ODQsOC04di0zMmgzMmM0LjQxNiwwLDgtMy41ODQsOC04di00OGMwLTQuNDE2LTMuNTg0LTgtOC04aC0zMnYtMzIgIGMwLTQuNDE2LTMuNTg0LTgtOC04aC00OGMtNC40MTYsMC04LDMuNTg0LTgsOHYzMmgtMzJjLTQuNDE2LDAtOCwzLjU4NC04LDh2NDhDMTEyLDI1Mi40MTYsMTE1LjU4NCwyNTYsMTIwLDI1NnogTTEyOCwyMDhoMzIgIGM0LjQxNiwwLDgtMy41ODQsOC04di0zMmgzMnYzMmMwLDQuNDE2LDMuNTg0LDgsOCw4aDMydjMyaC0zMmMtNC40MTYsMC04LDMuNTg0LTgsOHYzMmgtMzJ2LTMyYzAtNC40MTYtMy41ODQtOC04LThoLTMyVjIwOHoiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiMwMDAwMDAiIHN0eWxlPSIiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJNMTg0LDMyOGM1Ny4zNDQsMCwxMDQtNDYuNjU2LDEwNC0xMDRzLTQ2LjY1Ni0xMDQtMTA0LTEwNFM4MCwxNjYuNjU2LDgwLDIyNFMxMjYuNjU2LDMyOCwxODQsMzI4eiBNMTg0LDEzNiAgYzQ4LjUyLDAsODgsMzkuNDgsODgsODhzLTM5LjQ4LDg4LTg4LDg4cy04OC0zOS40OC04OC04OFMxMzUuNDgsMTM2LDE4NCwxMzZ6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0iTTM5MiwxMDRoOHYxNTJ2MTUyYzAsMS4wOCwwLjIxNiwyLjE2LDAuNjQ4LDMuMTUyTDQyNCw0NjUuNjRWNDgwaDE2di0xNC4zNmwyMy4zNTItNTQuNDg4ICBDNDYzLjc4NCw0MTAuMTYsNDY0LDQwOS4wOCw0NjQsNDA4VjI1NlY4MGMwLTQuNDE2LTMuNTg0LTgtOC04aC0xNnYtOGgtMTZ2OGgtMTZjLTQuNDE2LDAtOCwzLjU4NC04LDh2OGgtMTZjLTQuNDE2LDAtOCwzLjU4NC04LDggIHYxNjhoMTZWMTA0eiBNNDQ4LDI4MGgtMzJ2LTE2aDMyVjI4MHogTTQzMiw0NDMuNjg4bC0xNi0zNy4zMzZWMjk2aDMydjExMC4zNkw0MzIsNDQzLjY4OHogTTQxNiw4OGgzMnYxNjBoLTMyVjg4eiIgZmlsbD0iIzAwMDAwMCIgZGF0YS1vcmlnaW5hbD0iIzAwMDAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPgo8cmVjdCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9Ijg4IiB5PSIzNjgiIHdpZHRoPSIxOTIiIGhlaWdodD0iMTYiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiMwMDAwMDAiIHN0eWxlPSIiIGNsYXNzPSIiPjwvcmVjdD4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg=="
                    title="Freepik" />
                    Plano de contigência</div>
                    <br>
                    <div class="grid-container-verification">
                        <div class="minor-padding">
                            <b><i>O que é?</b></i><br>É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
                            da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
                            <br><br><b><i>Quem usa?</i></b>
                            <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br>
                        </div>
                        <div class="minor-padding">
                            <img src="https://via.placeholder.com/300">
                        </div>
                    </div>
                <div class="text-title-section main-padding"> 
                <img class="icon"
                src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI5OC42Njc5NjkgNDI2LjY2Nzk2OWMwIDQ3LjEyODkwNi0zOC4yMDcwMzEgODUuMzMyMDMxLTg1LjMzNTkzOCA4NS4zMzIwMzEtNDcuMTI4OTA2IDAtODUuMzMyMDMxLTM4LjIwMzEyNS04NS4zMzIwMzEtODUuMzMyMDMxIDAtNDcuMTI4OTA3IDM4LjIwMzEyNS04NS4zMzU5MzggODUuMzMyMDMxLTg1LjMzNTkzOCA0Ny4xMjg5MDcgMCA4NS4zMzU5MzggMzguMjA3MDMxIDg1LjMzNTkzOCA4NS4zMzU5Mzh6bTAgMCIgZmlsbD0iIzJiMTRmMCIgZGF0YS1vcmlnaW5hbD0iI2ZmYTAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTM2Mi44MzU5MzggMjU0LjMxNjQwNmMtNzIuMzIwMzEzLTEwLjMyODEyNS0xMjguMTY3OTY5LTcyLjUxNTYyNS0xMjguMTY3OTY5LTE0Ny42NDg0MzcgMC0yMS4zMzU5MzggNC41NjI1LTQxLjU3ODEyNSAxMi42NDg0MzctNTkuOTQ5MjE5LTEwLjkyMTg3NS0yLjU1ODU5NC0yMi4yNjk1MzEtNC4wNTA3ODEtMzMuOTg0Mzc1LTQuMDUwNzgxLTgyLjM0Mzc1IDAtMTQ5LjMzMjAzMSA2Ni45ODQzNzUtMTQ5LjMzMjAzMSAxNDkuMzMyMDMxdjU5LjQ3NjU2MmMwIDQyLjIxODc1LTE4LjQ5NjA5NCA4Mi4wNzAzMTMtNTAuOTQ1MzEyIDEwOS41MDM5MDctOC4yOTY4NzYgNy4wODIwMzEtMTMuMDU0Njg4IDE3LjQyOTY4Ny0xMy4wNTQ2ODggMjguMzUxNTYyIDAgMjAuNTg5ODQ0IDE2Ljc0NjA5NCAzNy4zMzU5MzggMzcuMzMyMDMxIDM3LjMzNTkzOGgzNTJjMjAuNTg5ODQ0IDAgMzcuMzM1OTM4LTE2Ljc0NjA5NCAzNy4zMzU5MzgtMzcuMzM1OTM4IDAtMTAuOTIxODc1LTQuNzU3ODEzLTIxLjI2OTUzMS0xMy4yNjk1MzEtMjguNTQyOTY5LTMxLjQ4ODI4Mi0yNi42NDQ1MzEtNDkuNzUtNjUuMzI0MjE4LTUwLjU2MjUtMTA2LjQ3MjY1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjZmZjMTA3IiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtNDkwLjY2Nzk2OSAxMDYuNjY3OTY5YzAgNTguOTEwMTU2LTQ3Ljc1NzgxMyAxMDYuNjY0MDYyLTEwNi42Njc5NjkgMTA2LjY2NDA2MnMtMTA2LjY2Nzk2OS00Ny43NTM5MDYtMTA2LjY2Nzk2OS0xMDYuNjY0MDYyYzAtNTguOTEwMTU3IDQ3Ljc1NzgxMy0xMDYuNjY3OTY5IDEwNi42Njc5NjktMTA2LjY2Nzk2OXMxMDYuNjY3OTY5IDQ3Ljc1NzgxMiAxMDYuNjY3OTY5IDEwNi42Njc5Njl6bTAgMCIgZmlsbD0iI2ZmOTE0NyIgZGF0YS1vcmlnaW5hbD0iI2Y0NDMzNiIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                title= "Freepik" />
                Ferramenta de notificação</div>
                <div class="grid-container-verification">
                    <div class="div1-verification">
                        <div><br>
                        <b><i>O que é?</b></i><br>
                        Ferramenta de comunicação das escolas com as Secretarias de Educação e Saúde sobre a existência de um caso ou suspeita na unidade.
                        <br><br><b><i>Como usa?</b></i>
                        <ol>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual envia o formulário para as escolas de sua rede;
                            <li>No surgimento de um caso ou suspeita, diretores(as) utilizam o formulário para informar para a Secretaria de Educação e Saúde, e seguem o plano de ação indicado.
                        </ol>
                        </div>
                    </div>
                    <div class="div2-verification"><br>
                        <a href="https://docs.google.com/forms/d/e/1FAIpQLScntZ8pwhAONfi3h2bd2JAL584oPWFNUgdu3EtqKmpaHDHHfQ/viewform">
                        <img style="height: 100%; width: 100%;" src="https://i.imgur.com/aNml5YI.png"> 
                        <br>
                        Clique
                        </a>
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
            <div class="div-logo-footer row">
                <div class="col main-padding">
                <a href="https://www.impulsogov.com.br/">
                    <img class="logo-footer"
                    src="https://static1.squarespace.com/static/5d86962ef8b1bc58c1dcaa0b/t/5ddad475ee3ebb607ae3d629/1600289027251/?format=1500w"
                    title="logo Impulso"/>
                </a>
                </div>
                <div class="col main-padding">
                <a href="https://fundacaolemann.org.br/">
                    <img class="logo-footer"
                    src="https://captadores.org.br/wp-content/uploads/2016/02/lemann_logo_pref_vert_pos_rgb.png"
                    tile="logo Lemann">
                </a>            
                <a href="https://www.iadb.org/pt/sobre-o-bid/visao-geral">
                    <img class="logo-footer"
                    src="https://seeklogo.com/images/B/banco-interamericano-de-desenvolvimento-logo-0F13DDE475-seeklogo.com.png"
                    title="logo BID">
                </a>
                </div>
            </div>
            <div class="container text-small main-padding">
                Todo os ícones são do <a href="https://www.freepik.com/">Freepik </a> com permissão de uso mediante créditos.
            </div>
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
    genPlanContainer(data, config, session_state)
    genSimulationContainer(data, config, session_state)
    genPrepareContainer()
    genMonitorContainer()
    genFooterContainer()


if __name__ == "__main__":
    main()
