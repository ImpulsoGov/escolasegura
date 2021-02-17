import streamlit as st
import utils

def genFooterContainer():
    """ 
    This is a function that returns the "Footer" session 
    
    """

    bidicon = utils.load_image("imgs/logo-bid.png")
    imaginableicon = utils.load_image("imgs/logo-imaginable.png")
    formaricon = utils.load_image("imgs/logo-formar.png")
    impulso_icon = utils.load_image("imgs/logo-impulso.png")

    st.write(
            f"""
            <div class="conteudo container upper-padding">
                <p style="text-align:left; font-size:.9em;">
                <b>As sugestões e recomendações apresentadas no Escola Segura são indicativas, feitas a partir de dados oficiais públicos 
                e estudos referenciados já publicados, estando sujeitas a variáveis que aqui não podem ser consideradas.</b> 
                Trata-se de contribuição à elaboração de cenários por parte dos governos e não configura qualquer obrigação 
                ou responsabilidade perante as decisões efetivadas.Saiba mais sobre os cálculos por trás em nossa Metodologia, 
                que mantemos atualizada.<br><br>
                <i>Todo código da ferramenta pode ser acessado no 
                <a target="_blank" class="github-link" style="font-family:var(--main-text-font-family)" href="https://github.com/ImpulsoGov/escolasegura">Github do projeto</a> do projeto 
                e os dados estão disponíveis em nossa 
                <a target="_blank" class="github-link" style="font-family:var(--main-text-font-family)" href="https://github.com/ImpulsoGov/coronacidades-datasource/blob/master/README.md">API</a>.</i>
                <br><i> A Escola Segura é uma iniciativa da plataforma <b class="main-orange-span">CoronaCidades</b>. Conheça 
                <a target="_blank" class="github-link" style="font-family:var(--main-text-font-family)" href="https://coronacidades.org/"> aqui</a>. </i>
                </p>
                <div class="text-title-footer main-padding" style="color:#ff9147;"><b>Realizado por</b></div>
                <div class="div-logo-footer main-padding img-center">
                <ul style="list-style-type: none;">
                    <li style="display: inline; margin-right: 2em;">
                    <a class="logo-footer" href="https://www.impulsogov.com.br/" target="_blank">
                        <img class="logo-footer" style="margin-bottom:2em;"
                        src="data:image/png;base64,{impulso_icon}"
                        title="logo Impulso"/>
                    </a></li>
                    <li style="display: inline; margin-right: 2em;">
                        <img class="logo-footer" style="margin-bottom:2em;"
                        src="https://captadores.org.br/wp-content/uploads/2016/02/lemann_logo_pref_vert_pos_rgb.png"
                        tile="logo Lemann">
                    </li>
                    <li style="display: inline;">
                        <img class="logo-footer" style="margin-bottom:2em;"
                        src="data:image/png;base64,{formaricon}"
                        title="logo Formar"/>
                    </li>
                    <li style="display: inline;">
                        <img class="logo-footer" style="margin-bottom:2em;"
                        src="data:image/png;base64,{imaginableicon}"
                        title="logo Imagine"/>
                    </li>
                    <li style="display: inline;">
                        <img class="logo-footer" style="margin-bottom:2em;"
                        src="data:image/png;base64,{bidicon}"
                        title="logo BID"/>
                    </li>
                </ul>          
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

if __name__ == "__main__":
    main()