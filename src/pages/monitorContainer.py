import streamlit as st
import base64
import utils


def genMonitorContainer():

    plan_icon = utils.load_image("imgs/monitor_plan_icon.png")
    plan_image = utils.load_image("imgs/monitor_plan_forms.png")
    notify_icon = utils.load_image("imgs/monitor_notify_icon.png")
    notify_image = utils.load_image("imgs/monitor_notify_forms.png")

    # Add Container Contents
    st.write(
        f"""
        <div class="container main-padding">
            <div class="left-margin">
                    <div class="row">
                        <div class="col">
                            <div class="card-plan">
                            <div style="margin:10px">
                            <div class="text-title-section minor-padding main-orange-span"> 
                                <img class="icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
                                Plano de contingência
                            </div>
                            <div>
                                <br>
                                <b><i>O que é?</b></i><br>É importante saber o que fazer se houver algum caso confirmado de Covid-19 em escolas 
                                da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
                                <br><br><b><i>Quem usa?</i></b>
                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br></li>
                            </div>
                            <div class="minor-padding button-position">
                                <a href="https://drive.google.com/file/d/1L6FXolCFTGQrfz_TT9zzxh1ojR5KfWEB/view" target="_blank">
                                    <button class="button-contigenciaimprima"; style="border-radius: .25rem;"> imprima aqui > </button>
                                </a>
                            </div>
                            <br>
                            </div></div>
                        </div>
                        <div class="col">
                            <div class="minor-padding">
                                <img class="img-forms" src='data:image/png;base64,{plan_image}'>
                            </div>
                            <div class="text-card-section minor-padding main-orange-span">
                                Disponibilizamos também o modelo <b>digital</b> e <b>editável</b> para você usar na sua secretaria 
                            </div>
                            <div class="minor-padding button-position">
                                <a href="https://docs.google.com/forms/d/1BunWrThhRcVl564AZDKlut2t1d5ugM9W5YtGnQmwo6Y/copy" target="_blank">
                                    <button class="button-contigenciacopie"; style="border-radius: .25rem;"> copie o modelo ></button>
                                </a>
                            </div>
                            <br>
                        </div>
                    </div>
                <div class="row">
                    <div class="col">
                        <div class="card-plan">
                        <div style="margin:10px">
                            <div class="text-title-section minor-padding main-orange-span"> 
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
                            <div class="minor-padding button-position">
                                <a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view" target="_blank">
                                    <button class="button-notificacaoimprime"; style="border-radius: .25rem;"> imprima aqui ></button>
                                </a>
                            </div>
                            <br>
                        </div></div>
                    </div>
                    <div class="col">
                        <div class="main-padding">
                            <img class="img-forms" src='data:image/png;base64,{notify_image}'>
                            <div class="text-card-section minor-padding main-orange-span">
                                Disponibilizamos também o modelo <b>digital</b> e <b>editável</b> para você usar na sua secretaria 
                            </div>
                            <div class="minor-padding button-position">
                                <a href="https://docs.google.com/forms/d/1xh-_NI925-bWNn81PG5dKKkSa9J14NVwT3SpPIShJzo/copy" target="_blank">
                                    <button class="button-notificacaocopie"; style="border-radius: .25rem;"> copie o modelo ></button>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
