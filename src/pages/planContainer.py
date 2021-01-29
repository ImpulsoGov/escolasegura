import streamlit as st
import utils


def genPlanContainer(df, config, session_state):
    """ 
    This is a function that returns the "Plan" session

    Parameters: 
        df (type): 2019 school census dataframe
        config (type): doc config.yaml
        session_state (type): section dataset

    """
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
       Hoje, na região que voce selecionou (<b>{cidade}</b>), o nível de alerta é: 
        <t class='{elements["color"]}'><b>{alert.upper()}</b></t>. 
        {elements["description"]}<br>Dados: <a
        href="http://farolcovid.coronacidades.org" style="font-family:
        var(--main-text-font-family)">FarolCovid</a>."""

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
    <a href="#entenda-mais">
        <button class="button-entendaalerta" style="font-size:15px">
            entenda alerta do farolcovid >
        </button>
    </a>
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
            Como <b>estruturar</b> a reabertura da minha rede? 
            </div>
            <p><b>A fase de planejamento é essencial para uma reabertura segura.</b>
            Os diversos atores do dia a dia das escolas devem ser incluídos para diálogo e formulação dos protocolos.</p>
            <div class="left-margin">
                <div class="row">
                    <div class="col card-plan container">
                    <div style="margin:10px">
                        <div class="left-margin">
                            <div class="text-title-section main-orange-span minor-padding"> 
                                <img class="icon" src="data:image/png;base64,{steps_icon}" alt="Fonte: Flaticon">
                                Passo a passo
                            </div>
                            <div class="subtitle-section minor-padding"> 
                                Como checar o <b>preparo</b> da minha secretaria e rede para a reabertura presencial?
                            </div>
                            <div class="minor-padding main-black-span">
                                <b>Guia com 10 passos para uma reabertura segura da sua rede.</b><br>
                                <b><i>Quem usa?</i></b>
                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.
                            </div><br>
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://drive.google.com/file/d/14XzVchfOmub2zBdCJwl7C8s-bc2QZgCS/view" target="blank_">
                                <button class="button-passoapasso"; style="border-radius: .25rem;">acesse ></button><br>
                                </a>
                            </div>              
                            <div class="minor-padding main-black-span">
                                Ferramenta que <b>auxilia na criação de um plano de retomada</b> com a inclusão da Secretaria de Saúde, comunidade escolar e outros atores.<br>
                                <b><i>Quem usa?</i></b>
                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.
                            </div><br>
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://docs.google.com/forms/d/1Mml-UF44tGqVZ-FQpjuposgb_ZXsi_DoEOdSNiCnAtc/viewform" target="blank_">
                                <button class="button-passoapasso"; style="border-radius: .25rem;">acesse ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                    </div>
                    <div class="col card-plan container">
                    <div style="margin:10px">
                        <div class="left-margin">
                            <div class="text-title-section main-orange-span minor-padding"> 
                                <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
                                Protocolos
                            </div>
                            <div class="subtitle-section minor-padding"> 
                                Quais são as principais <b>recomendações sanitárias</b> e protocolos para retomada?
                            </div> 
                            <div class="minor-padding main-black-span">
                                <b>Listas de orientações para planejar a estrutura sanitária nas escolas.</b>
                                A ferramenta fornece também rotinas a serem seguidas dentro e fora da sala de aula.<br><br>
                                <b><i>Quem usa?</i></b>
                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual
                                <li> Diretores(as) de escolas.
                            </div><br>
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://drive.google.com/file/d/1NDdWRenKQ9EzVwBX6GbovSd3UICREhVg/view?usp=sharing" target="blank_">
                                <button class="button-protocolos"; style="border-radius: .25rem;">acesse ></button><br>
                                </a>
                            </div>
                        </div><br>
                    </div>
                    </div>
                </div><br>
                <div class="text-title-section main-orange-span minor-padding"> 
                    <img class="icon" src="data:image/png;base64,{ruler_icon}" alt="Fonte: Flaticon">
                    Régua de protocolo
                </div>
                <div class="subtitle-section minor-padding"> 
                    Quais protocolos seguir de acordo com o nível de alerta da minha região?
                </div> 
                <div class="minor-padding">
                    Ferramenta de indicação das <b>principais ações</b> a serem tomadas no ambiente escolar <b>para cada nível de alerta.<b>
                </div>
                <div class="main-padding">{caption}</div><br>{modal}
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
