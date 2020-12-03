import streamlit as st
import utils


def genPrepareContainer():
    """ 
    This is a function that returns the "Prepare" session
              
    """

    verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
    verify_image = utils.load_image("imgs/prepare_verify_forms.png")

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section">
                <img class="square" src="https://i.imgur.com/gGIFS5N.png">
                Como <b>gerir</b> as unidades escolares abertas? 
            </div>
            <p class="minor-padding"><b>A fase de preparação é onde os protocolos de segurança das escolas são discutidos e pactuados. 
            Durante a reabertura</b>, é importante que seja estabelecida uma rotina de verificação das unidades escolares 
            para <b>acompanhar o cumprimento dos protocolos</b> estabelecidos.</p>
            <div class="left-margin">
                <div class="row">
                    <div class="col">
                        <div class="card-plan">
                        <div style="margin:10px">
                        <div class="text-title-section minor-padding main-orange-span"> 
                            <img class="icon" src="data:image/png;base64,{verify_icon}" alt="Fonte: Flaticon">
                            Ferramenta de verificação
                        </div><br>
                        <div>
                            <b><i>O que é?</b></i><br>
                            Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
                            <br><br>
                            <b><i>Quem usa?</b></i>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).</li>
                            <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.</li>
                        </div>
                        <div class="minor-padding button-position">
                            <a href="https://drive.google.com/file/d/1JJiVJorSxc-7gK-7uFgdqHLguBXKUzxb/view" target="_blank">
                                <button class="button-verificacaoimprime"; style="border-radius: .25rem;">imprima aqui ></button>
                            </a>
                        </div>
                        <br>
                        </div>
                        </div>
                    </div>
                    <div class="col">
                            <div class="minor-padding">
                                <img class="img-forms" src='data:image/png;base64,{verify_image}'>
                            </div>
                            <div class="text-card-section minor-padding main-orange-span">
                                Disponibilizamos também o modelo <b>digital</b> e <b>editável</b> para você usar na sua secretaria 
                            </div>
                            <div class="minor-padding button-position">
                                <a href="https://docs.google.com/forms/d/1JjXIs0M-A-RLhISYlltX4fjXL5pu8C_iKUkI_a8GhyI/copy" target="_blank">
                                    <button class="button-verificacaocopie"; style="border-radius: .25rem;"> copie o modelo ></button>
                                </a>
                            </div>
                            <br>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
