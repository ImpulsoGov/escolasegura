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
        Hoje em <b>{cidade}</b>, segundo o <a href="http://farolcovid.coronacidades.org">FarolCovid</a>, o nível de alerta é: 
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

    protocol_icon = utils.load_image("imgs/plan_protocol_icon.png")
    steps_icon = utils.load_image("imgs/plan_steps_icon.png")
    ruler_icon = utils.load_image("imgs/plan_ruler_icon.png")

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
                            <img class="icon" src="data:image/png;base64,{steps_icon}" alt="Fonte: Flaticon">
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
                            <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
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
                <div class="text-title-section minor-padding"> 
                    <img class="icon" src="data:image/png;base64,{ruler_icon}" alt="Fonte: Flaticon">
                    Régua de protocolo</div>
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
