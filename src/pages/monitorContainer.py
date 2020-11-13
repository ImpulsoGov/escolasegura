import streamlit as st
import base64
import utils


def genMonitorContainer():

    plan_icon = utils.load_image("imgs/monitor_plan_icon.png")
    plan_image = utils.load_image("imgs/monitor_plan_form.png")
    notify_icon = utils.load_image("imgs/monitor_notify_icon.png")
    notify_image = utils.load_image("imgs/monitor_notify_form.png")

    # Add Container Contents
    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">
                <p style="color:#2b14ff; font-size:21px;"><b>2 - O que fazer quando um caso for confirmado em uma unidade escolar?</b></p>
            </div>
            <div class="left-margin">
                    <div class="row">
                        <div class="col">
                            <div class="text-title-section minor-padding"> 
                            <img class="icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
                            Plano de contingência</div>
                            <br>
                            <b><i>O que é?</b></i><br>É importante saber o que fazer no caso de algum caso confirmado de Covid-19 em escolas 
                            da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
                            <br><br><b><i>Quem usa?</i></b>
                            <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br></li>
                            <br><b>➡️ Clique na imagem para acessar a ferramenta online ou <a href="https://drive.google.com/file/d/1L6FXolCFTGQrfz_TT9zzxh1ojR5KfWEB/view">baixe aqui</a></b><br>
                        </div>
                        <div class="col"><br>
                            <div class="minor-padding">
                                <a href="https://docs.google.com/forms/d/1BunWrThhRcVl564AZDKlut2t1d5ugM9W5YtGnQmwo6Y/copy" target="blank_">
                                    <img class="img-forms" src='data:image/png;base64,{plan_image}'>
                                </a>
                            </div>
                        </div>
                    </div>
                <div class="title-section">
                    <p style="color:#2b14ff; font-size:21px;"><b>3 - Como acompanhar a notificação de casos em unidades escolares e orientar ações?</b></p>
                </div>
                <div class="row">
                    <div class="col">
                        <div class="text-title-section main-padding"> 
                            <img class="icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
                            Ferramenta de notificação
                        </div>
                        <br>
                        <b><i>O que é?</b></i><br>
                        Ferramenta de comunicação das escolas com as Secretarias de Educação e Saúde sobre a existência de um caso ou suspeita na unidade.
                        <br><br><b><i>Como usa?</b></i>
                        <ol>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual envia o formulário para as escolas de sua rede;</li>
                            <li>No surgimento de um caso ou suspeita, diretores(as) utilizam o formulário para informar para a Secretaria de Educação e Saúde, e seguem o plano de ação indicado.</li>
                        </ol>
                        <br><b>➡️ Clique na imagem para acessar a ferramenta online ou </b><a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view">baixe aqui</a></b><br>
                    </div>
                    <div class="col"><br>
                        <div class="main-padding">
                            <a href="https://docs.google.com/forms/d/1xh-_NI925-bWNn81PG5dKKkSa9J14NVwT3SpPIShJzo/copy" target="_blank">
                            <img class="img-forms" src='data:image/png;base64,{notify_image}'> 
                        </div>
                        </a>
                    </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
