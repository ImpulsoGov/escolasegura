import streamlit as st
import utils


def genPlanContainer(df, config, session_state):
    data = df[
        (df["state_id"] == session_state.state_id)
        & (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]

    if len(data["overall_alert"]) > 0:

        if session_state.city_name != "Todos":
            cidade = session_state.city_name
        else:
            cidade = session_state.state_id

        # resgata nome do alerta no config do Farol
        farol_covid = utils.get_config(config["br"]["farolcovid"]["config"])["br"][
            "farolcovid"
        ]
        alert = farol_covid["categories"][data["overall_alert"].values[0]]

        elements = config["br"]["farolcovid"]["elements"][alert]

        caption = f"""
        Hoje em <b>{cidade}</b>, segundo o FarolCovid, o nível de alerta é: 
        <t class='{elements["color"]}'><b>{alert.upper()}</b></t>. 
        {elements["description"]}"""

        href = elements["href"]
        url = href + ".png"

    else:
        href = ""
        url = ""
        caption = "Não há nível de alerta na sua cidade. Sugerimos que confira o nível de risco de seu estado."

    situation_classification = farol_covid["rules"]["situation_classification"]["cuts"]
    control_classification = farol_covid["rules"]["control_classification"]["cuts"]
    capacity_classification = farol_covid["rules"]["capacity_classification"]["cuts"]
    trust_classification = farol_covid["rules"]["trust_classification"]["cuts"]

    date_update = farol_covid["date_update"]

    modal = f"""
    <a href="#entenda-mais" class="info-btn">Entenda os níveis do FarolCovid</a>
    <div id="entenda-mais" class="info-modal-window">
        <div>
            <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
            <div style="margin: 10px 15px 15px 15px;">
            <h1 class="main-orange-span bold">Valores de referência</h1>
            <div style="font-size: 14px">
                Para mais detalhes confira nossa página de Metodologia no <a href="http://farolcovid.coronacidades.org">FarolCovid</a>.</b></a>
            </div><br>
            <div style="font-size: 12px">
                <b>Atualizado em</b>: {date_update}<br>
            </div>
            <div class="info-div-table">
            <table class="info-table">
            <tbody>
                <tr>
                    <td class="grey-bg"><strong>Dimensão</strong></td>
                    <td class="grey-bg"><strong>Indicador</strong></td>
                    <td class="grey-bg"><strong><p class="blue-text">Novo Normal</p></strong></td>
                    <td class="grey-bg"><strong>Risco <p class="yellow-text">Moderado</p></strong></td>
                    <td class="grey-bg"><strong>Risco <p class="orange-text">Alto</p></strong></td>
                    <td class="grey-bg"><strong>Risco <p class="red-text">Altíssimo</p></strong></td>
                </tr>
                <tr>
                    <td rowspan="2">
                    <t><span>Situação da doença</span></t><br/>
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
            </div>
        </div>
    </div>"""

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"> <img class="square" src="https://i.imgur.com/gGIFS5N.png">
            Como organizo a reabertura da minha rede escolar? 
            </div>
            <p><b>A fase de planejamento é essencial para uma reabertura segura.</b>
            Devem ser incluídos os diversos atores do dia-a-dia das escolas 
            para diálogo e formulação dos protocolos.</p>
            <div class="left-margin">
                <div class="row">
                    <a class="col card-plan container" 
                    href="https://docs.google.com/forms/d/1Mml-UF44tGqVZ-FQpjuposgb_ZXsi_DoEOdSNiCnAtc/viewform" target="blank_">
                    <div style="margin:10px">
                        <div>
                            <p style="color:#2b14ff; font-size:21px;"> <b>1 - Como checar o preparo da minha secretaria e rede para a reabertura presencial?</b></p>              
                        </div>
                        <div class="left-margin">
                            <div class="text-title-section minor-padding"> 
                            <img class="icon" 
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zOTUuMTMzLDIwMC4zNDhjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZWMTE2Ljg3YzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTYgIHMxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NnY2Ni43ODNDNDExLjgyOCwxOTIuODc1LDQwNC4zNTYsMjAwLjM0OCwzOTUuMTMzLDIwMC4zNDh6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjNWM1ZjY2Ij48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQxMS44MjgsMTgzLjY1MlYxMTYuODdjMC05LjIyMy03LjQ3My0xNi42OTYtMTYuNjk2LTE2LjY5NnYxMDAuMTc0ICBDNDA0LjM1NiwyMDAuMzQ4LDQxMS44MjgsMTkyLjg3NSw0MTEuODI4LDE4My42NTJ6IiBmaWxsPSIjNTM1NjVjIiBkYXRhLW9yaWdpbmFsPSIjNTM1NjVjIiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQ0NS4yMiwxMzMuNTY1SDMyOC4zNWMtOS4yMjMsMC0xNi42OTYtNy40NzMtMTYuNjk2LTE2LjY5NlYxNi42OTYgIEMzMTEuNjU0LDcuNDczLDMxOS4xMjcsMCwzMjguMzUsMGgxMTYuODdjMzYuODIxLDAsNjYuNzc3LDI5Ljk1Niw2Ni43NzcsNjYuNzgzUzQ4Mi4wNCwxMzMuNTY1LDQ0NS4yMiwxMzMuNTY1eiIgZmlsbD0iIzVhNWE1ZiIgZGF0YS1vcmlnaW5hbD0iI2ZmZGUzMyIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00NDUuMjIsMGgtNTAuMDg3djEzMy41NjVoNTAuMDg3YzM2LjgyMSwwLDY2Ljc3Ny0yOS45NTYsNjYuNzc3LTY2Ljc4M1M0ODIuMDQsMCw0NDUuMjIsMHoiIGZpbGw9IiM1YTVhNWEiIGRhdGEtb3JpZ2luYWw9IiNmZmJjMzMiIGNsYXNzPSIiPjwvcGF0aD4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0yOTQuOTU5LDI2Ny4xM0gxODMuNjU0Yy05LjIyMywwLTE2LjY5Ni03LjQ3My0xNi42OTYtMTYuNjk2czcuNDczLTE2LjY5NiwxNi42OTYtMTYuNjk2aDExMS4zMDQgICBjOS4yMjMsMCwxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NlMzMDQuMTgzLDI2Ny4xMywyOTQuOTU5LDI2Ny4xM3oiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiM1YzVmNjYiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0xMDAuMTc2LDIwMC4zNDhjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZWMTE2Ljg3YzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTYgICBzMTYuNjk2LDcuNDczLDE2LjY5NiwxNi42OTZ2NjYuNzgzQzExNi44NzIsMTkyLjg3NSwxMDkuNCwyMDAuMzQ4LDEwMC4xNzYsMjAwLjM0OHoiIGZpbGw9IiMwMDAwMDAiIGRhdGEtb3JpZ2luYWw9IiM1YzVmNjYiPjwvcGF0aD4KPC9nPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xMTYuODcyLDE4My42NTJWMTE2Ljg3YzAtOS4yMjMtNy40NzMtMTYuNjk2LTE2LjY5Ni0xNi42OTZ2MTAwLjE3NCAgQzEwOS40LDIwMC4zNDgsMTE2Ljg3MiwxOTIuODc1LDExNi44NzIsMTgzLjY1MnoiIGZpbGw9IiM1MzU2NWMiIGRhdGEtb3JpZ2luYWw9IiM1MzU2NWMiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTAwLjE3Niw0MzQuMDg3Yy05LjIyMywwLTE2LjY5Ni03LjQ3My0xNi42OTYtMTYuNjk2di02Ni43ODNjMC05LjIyMyw3LjQ3My0xNi42OTYsMTYuNjk2LTE2LjY5NiAgczE2LjY5Niw3LjQ3MywxNi42OTYsMTYuNjk2djY2Ljc4M0MxMTYuODcyLDQyNi42MTQsMTA5LjQsNDM0LjA4NywxMDAuMTc2LDQzNC4wODd6IiBmaWxsPSIjMDAwMDAwIiBkYXRhLW9yaWdpbmFsPSIjNWM1ZjY2Ij48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTExNi44NzIsNDE3LjM5MXYtNjYuNzgzYzAtOS4yMjMtNy40NzMtMTYuNjk2LTE2LjY5Ni0xNi42OTZ2MTAwLjE3NCAgQzEwOS40LDQzNC4wODcsMTE2Ljg3Miw0MjYuNjE0LDExNi44NzIsNDE3LjM5MXoiIGZpbGw9IiM1MzU2NWMiIGRhdGEtb3JpZ2luYWw9IiM1MzU2NWMiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTgzLjY1NCwxMzMuNTY1SDE2LjY5OGMtOS4yMjMsMC0xNi42OTYtNy40NzMtMTYuNjk2LTE2LjY5NlYxNi42OTZDMC4wMDIsNy40NzMsNy40NzUsMCwxNi42OTgsMCAgaDE2Ni45NTdjOS4yMjMsMCwxNi42OTYsNy40NzMsMTYuNjk2LDE2LjY5NlYxMTYuODdDMjAwLjM1LDEyNi4wOTIsMTkyLjg3OCwxMzMuNTY1LDE4My42NTQsMTMzLjU2NXoiIGZpbGw9IiMyYjE0ZjAiIGRhdGEtb3JpZ2luYWw9IiM1MGI5ZmYiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTAwLjE3NiwzNjcuMzA0Yy01NS4yMzQsMC0xMDAuMTc0LTQ0Ljk0LTEwMC4xNzQtMTAwLjE3NHM0NC45NC0xMDAuMTc0LDEwMC4xNzQtMTAwLjE3NCAgUzIwMC4zNSwyMTEuODk3LDIwMC4zNSwyNjcuMTNTMTU1LjQxLDM2Ny4zMDQsMTAwLjE3NiwzNjcuMzA0eiIgZmlsbD0iI2ZmOTE0MCIgZGF0YS1vcmlnaW5hbD0iI2VjNzgzOCIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xODMuNjU0LDUxMkgxNi42OThjLTkuMjIzLDAtMTYuNjk2LTcuNDczLTE2LjY5Ni0xNi42OTZ2LTc3LjkxMyAgYzAtOS4yMjMsNy40NzMtMTYuNjk2LDE2LjY5Ni0xNi42OTZoMTY2Ljk1N2M5LjIyMywwLDE2LjY5Niw3LjQ3MywxNi42OTYsMTYuNjk2djc3LjkxM0MyMDAuMzUsNTA0LjUyNywxOTIuODc4LDUxMiwxODMuNjU0LDUxMnoiIGZpbGw9IiMyYjE0ZjAiIGRhdGEtb3JpZ2luYWw9IiM1MGI5ZmYiIGNsYXNzPSIiPjwvcGF0aD4KPHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBzdHlsZT0iIiBkPSJNMTgzLjY1NCw0MDAuNjk2aC04My40NzhWNTEyaDgzLjQ3OGM5LjIyMywwLDE2LjY5Ni03LjQ3MywxNi42OTYtMTYuNjk2di03Ny45MTMgIEMyMDAuMzUsNDA4LjE2OSwxOTIuODc4LDQwMC42OTYsMTgzLjY1NCw0MDAuNjk2eiIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzQ4YTdlNiIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0yMDAuMzUsMjY3LjEzYzAtNTUuMjM0LTQ0Ljk0LTEwMC4xNzQtMTAwLjE3NC0xMDAuMTc0djIwMC4zNDggIEMxNTUuNDEsMzY3LjMwNCwyMDAuMzUsMzIyLjM2NCwyMDAuMzUsMjY3LjEzeiIgZmlsbD0iI2ZmOTE0NyIgZGF0YS1vcmlnaW5hbD0iI2RiNjMyYyIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0xODMuNjU0LDBoLTgzLjQ3OHYxMzMuNTY1aDgzLjQ3OGM5LjIyMywwLDE2LjY5Ni03LjQ3MywxNi42OTYtMTYuNjk2VjE2LjY5NiAgQzIwMC4zNSw3LjQ3MywxOTIuODc4LDAsMTgzLjY1NCwweiIgZmlsbD0iIzJiMTRmZiIgZGF0YS1vcmlnaW5hbD0iIzQ4YTdlNiIgY2xhc3M9IiI+PC9wYXRoPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik0zOTUuMTMzLDMzMy45MTNjLTMuMjI4LDAtNi40NTctMC45MzUtOS4yNjEtMi44MDVsLTEwMC4xNzQtNjYuNzgzICBjLTQuNjQ3LTMuMDk4LTcuNDM1LTguMzEtNy40MzUtMTMuODkxYzAtNS41ODEsMi43ODgtMTAuNzkzLDcuNDM1LTEzLjg5MWwxMDAuMTc0LTY2Ljc4M2M1LjYwOS0zLjczOSwxMi45MTQtMy43MzksMTguNTIyLDAgIGwxMDAuMTY4LDY2Ljc4M2M0LjY0MSwzLjA5OCw3LjQzNSw4LjMxLDcuNDM1LDEzLjg5MWMwLDUuNTgxLTIuNzk0LDEwLjc5My03LjQzNSwxMy44OTFsLTEwMC4xNjgsNjYuNzgzICBDNDAxLjU4OSwzMzIuOTc4LDM5OC4zNjIsMzMzLjkxMywzOTUuMTMzLDMzMy45MTN6IiBmaWxsPSIjOTlmZmRmIiBkYXRhLW9yaWdpbmFsPSIjN2JjYzI5IiBjbGFzcz0iIj48L3BhdGg+CjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgc3R5bGU9IiIgZD0iTTQwNC4zOTQsMzMxLjEwOGwxMDAuMTY4LTY2Ljc4M2M0LjY0MS0zLjA5OCw3LjQzNS04LjMxLDcuNDM1LTEzLjg5MSAgYzAtNS41ODEtMi43OTQtMTAuNzkzLTcuNDM1LTEzLjg5MWwtMTAwLjE2OC02Ni43ODNjLTIuODA1LTEuODctNi4wMzMtMi44MDUtOS4yNjEtMi44MDV2MTY2Ljk1NiAgQzM5OC4zNjIsMzMzLjkxMyw0MDEuNTg5LDMzMi45NzgsNDA0LjM5NCwzMzEuMTA4eiIgZmlsbD0iIzk5ZmZkNCIgZGF0YS1vcmlnaW5hbD0iIzZlYjgyNSIgY2xhc3M9IiI+PC9wYXRoPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8L2c+PC9zdmc+" 
                            title="Freepik" />
                            Passo a passo</div>
                            <div class="minor-padding main-black-span"><br>
                            <b><i>O que é?</i><br>
                            Guia com 10 passos para uma reabertura segura da sua rede.</b> A ferramenta auxilia na criação de um plano de retomada com a inclusão da Secretaria de Saúde, comunidade escolar e outros atores.<br><br>
                            <b><i>Quem usa?</i></b>
                            <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.
                            </div><br>
                            <div align="center" style="padding-bottom: 10px;">
                                <button class="button"; style="border-radius: .25rem;">Veja Aqui</button><br>
                            </div>
                        </div>
                    </div>
                    </a>
                    <a class="col card-plan container" href="https://docs.google.com/spreadsheets/d/1_fYMo_Cy3ukJCmxdKDa9plTOJDBfbURQSY2z0wGCyTY/view" target="blank_">           
                    <div style="margin:10px">
                        <div class="left-margin">
                            <p style="color:#2b14ff; font-size:21px;"> <b>2 - Quais são as principais recomendações sanitárias e protocolos para retomada?</b></p>
                            <div class="text-title-section minor-padding"> 
                            <img class="icon" 
                            src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDQ2NCA0NjQiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPgo8cGF0aCB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSIiIGQ9Ik00MjAuNDc0LDEyNC44bC00Mi40LTIwLjh2MzUybDU5LjItMjk2QzQ0MC40NzQsMTQ1LjYsNDMzLjI3NCwxMzEuMiw0MjAuNDc0LDEyNC44eiIgZmlsbD0iIzk5ZmZkNCIgZGF0YS1vcmlnaW5hbD0iIzAwZjJhOSIgY2xhc3M9IiI+PC9wYXRoPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPHBhdGggc3R5bGU9IiIgZD0iTTQyMy42NzQsODUuNmwtMzguNC0xOS4yYy0yLjQtMTkuMi0xOS4yLTM0LjQtMzkuMi0zNC40aC0xODQuOGMtNC0xOC40LTIwLTMyLTM5LjItMzJoLTMyICAgYy0xOS4yLDAtMzYsMTQuNC0zOS4yLDMyLjhjLTE4LjQsMy4yLTMyLjgsMjAtMzIuOCwzOS4ydjM1MmMwLDIyLjQsMTcuNiw0MCw0MCw0MGgyODhjMjEuNiwwLDQwLTE2LjgsNDAtMzguNGwwLDBsNTkuMi0yOTYgICBDNDQ4LjQ3NCwxMTIsNDM5LjY3NCw5My42LDQyMy42NzQsODUuNnogTTkwLjA3NCwxNmgzMmMxMC40LDAsMTkuMiw2LjQsMjIuNCwxNmgtNzYuOEM3MC44NzQsMjIuNCw3OS42NzQsMTYsOTAuMDc0LDE2eiAgICBNMzcwLjA3NCw0MjRjMCwxMy42LTEwLjQsMjQtMjQsMjRoLTg4di0yNGMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYyNGgtMTZ2LTU2YzAtNC44LTMuMi04LTgtOHMtOCwzLjItOCw4djU2aC0xNnYtMjQgICBjMC00LjgtMy4yLTgtOC04cy04LDMuMi04LDh2MjRoLTgwdi0yNGMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYyNGgtMjRjLTEzLjYsMC0yNC0xMC40LTI0LTI0VjcyYzAtMTMuNiwxMC40LTI0LDI0LTI0aDg4djE1MiAgIGMwLDEzLjYtMTAuNCwyNC0yNCwyNHMtMjQtMTAuNC0yNC0yNFY3MmMwLTQuOC0zLjItOC04LThzLTgsMy4yLTgsOHYxMjhjMCwyMi40LDE3LjYsNDAsNDAsNDBzNDAtMTcuNiw0MC00MFY0OGgxODQgICBjMTMuNiwwLDI0LDEwLjQsMjQsMjRWNDI0eiBNNDI5LjI3NCwxMjYuNGwtNDMuMiwyMTYuOFY4NC44bDMwLjQsMTUuMkM0MjYuMDc0LDEwNC44LDQzMS42NzQsMTE2LDQyOS4yNzQsMTI2LjR6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCw5NmgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsOTYsMzE0LjA3NCw5NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0zMTQuMDc0LDE2MGgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsMTYwLDMxNC4wNzQsMTYweiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTIxOC4wNzQsMjQwaDMyYzQuOCwwLDgtMy4yLDgtOHMtMy4yLTgtOC04aC0zMmMtNC44LDAtOCwzLjItOCw4ICAgQzIxMC4wNzQsMjM2LjgsMjEzLjI3NCwyNDAsMjE4LjA3NCwyNDB6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwyMjRoLTMyYy00LjgsMC04LDMuMi04LDhjMCw0LjgsMy4yLDgsOCw4aDMyYzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDIyNCwzMTQuMDc0LDIyNHoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0xODYuMDc0LDMyMGgtOTZjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoOTZjNC44LDAsOC0zLjIsOC04UzE5MC44NzQsMzIwLDE4Ni4wNzQsMzIweiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTMxNC4wNzQsMzIwaC05NmMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGg5NmM0LjgsMCw4LTMuMiw4LThTMzE4Ljg3NCwzMjAsMzE0LjA3NCwzMjB6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwxOTJoLTk2Yy00LjgsMC04LDMuMi04LDhzMy4yLDgsOCw4aDk2YzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDE5MiwzMTQuMDc0LDE5MnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0yNTguMDc0LDI5NmMwLTQuOC0zLjItOC04LThoLTE2MGMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGgxNjAgICBDMjU0Ljg3NCwzMDQsMjU4LjA3NCwzMDAuOCwyNTguMDc0LDI5NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KCTxwYXRoIHN0eWxlPSIiIGQ9Ik0zMTQuMDc0LDI4OGgtMzJjLTQuOCwwLTgsMy4yLTgsOHMzLjIsOCw4LDhoMzJjNC44LDAsOC0zLjIsOC04UzMxOC44NzQsMjg4LDMxNC4wNzQsMjg4eiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTIxOC4wNzQsMTQ0aDMyYzQuOCwwLDgtMy4yLDgtOHMtMy4yLTgtOC04aC0zMmMtNC44LDAtOCwzLjItOCw4UzIxMy4yNzQsMTQ0LDIxOC4wNzQsMTQ0eiIgZmlsbD0iIzMyMjE1MyIgZGF0YS1vcmlnaW5hbD0iIzMyMjE1MyIgY2xhc3M9IiI+PC9wYXRoPgoJPHBhdGggc3R5bGU9IiIgZD0iTTMxNC4wNzQsMTI4aC0zMmMtNC44LDAtOCwzLjItOCw4czMuMiw4LDgsOGgzMmM0LjgsMCw4LTMuMiw4LThTMzE4Ljg3NCwxMjgsMzE0LjA3NCwxMjh6IiBmaWxsPSIjMzIyMTUzIiBkYXRhLW9yaWdpbmFsPSIjMzIyMTUzIiBjbGFzcz0iIj48L3BhdGg+Cgk8cGF0aCBzdHlsZT0iIiBkPSJNMzE0LjA3NCwyNTZoLTk2Yy00LjgsMC04LDMuMi04LDhzMy4yLDgsOCw4aDk2YzQuOCwwLDgtMy4yLDgtOFMzMTguODc0LDI1NiwzMTQuMDc0LDI1NnoiIGZpbGw9IiMzMjIxNTMiIGRhdGEtb3JpZ2luYWw9IiMzMjIxNTMiIGNsYXNzPSIiPjwvcGF0aD4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8L2c+PC9zdmc+"
                            title="Freepik" />
                            Protocolos</div>
                            <div class="minor-padding main-black-span"><br>
                                <b><i>O que é?</i><br>
                                Listas de orientações para planejar a estrutura sanitária nas escolas</b>
                                A ferramenta fornece também rotinas a serem seguidas dentro e fora da sala de aula.<br><br>
                                <b><i>Quem usa?</i></b>
                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual
                                <li> Diretores(as) de escolas.
                            </div><br>
                            <div align="center" style="padding-bottom: 10px;">
                                <button class="button"; style="border-radius: .25rem;">Veja Aqui</button><br>
                            </div>
                        </div><br>
                    </div>
                    </a>
                </div><br>
                <div class="title-section">
                 <p style="font-size:21px;"> <b>3 - Quais protocolos seguir de acordo com o nível de alerta da minha região?</b></p>              
                </div>
                <div class="text-title-section"> Régua de protocolo </div>
                <div class="minor-padding">
                    <b><i>O que é?</i><br></b>  Ferramenta de indicação das principais ações a serem tomadas no ambiente escolar para cada nível de alerta.<br><br>
                </div>
                <div class="minor-padding">{caption}</div><br>{modal}
                </div>
                <div class="minor-padding">
                    <a href={href} target="_blank">
                        <img class="images" src={href}> 
                    </a>
                </div>
                </div>
            </div>
        </div><br>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
