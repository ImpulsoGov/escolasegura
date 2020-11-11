import streamlit as st
from utils import load_image


def genPrepareContainer():

    verify_icon = load_image("imgs/prepare_verify_icon.png")

    st.write(
        f"""
        <div class="container main-padding">
            <div class="title-section"><img class="square" src="https://i.imgur.com/gGIFS5N.png">Como faço a gestão das unidades escolares? 
            </div>
            <p><b>A fase de preparação é onde os protocolos de segurança das escolas são discutidas e pactuadas.</b> 
            Durante a reabertura, é importante que seja estabelecida uma rotina de verificação das unidades escolares 
            para acompanhar o cumprimento dos protocolos estabelecidos.</p>
            <div class="title-section">
            <p style="color:#2b14ff; font-size:21px;"><b>1 - Como verificar e garantir condições para reabertura de escolas por meio de gestores escolares?</b></p>
            </div>
                <div class="left-margin">
                    <div class="row">
                        <div class="col">
                            <div class="text-title-section minor-padding"> 
                                <img class="icon" src="data:image/png;base64,{verify_icon}" alt="Fonte: Flaticon">
                                Ferramenta de verificação
                            </div><br>
                            <b><i>O que é?</b></i><br>
                            Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
                            <br><br>
                            <b><i>Quem usa?</b></i>
                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).</li>
                            <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.</li>
                            <br><b>➡️ Clique na imagem para acessar a ferramenta online ou <a href="https://drive.google.com/file/d/1JJiVJorSxc-7gK-7uFgdqHLguBXKUzxb/view">baixe aqui</a></b><br>
                        </div>
                        <div class="col"><br>
                            <div class="minor-padding">
                                <a href="https://docs.google.com/forms/d/1JjXIs0M-A-RLhISYlltX4fjXL5pu8C_iKUkI_a8GhyI/copy" target="_blank">
                                <img class="img-forms" src="https://i.imgur.com/gA2IIgB.png"> 
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
