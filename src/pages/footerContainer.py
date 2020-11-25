import streamlit as st
import utils

def genFooterContainer():
    bidicon = utils.load_image("imgs/logo-bid.png")
    imaginableicon = utils.load_image("imgs/logo-imaginable.png")
    formaricon = utils.load_image("imgs/logo-formar.png")
    impulso_icon = utils.load_image("imgs/logo-impulso.png")

    st.write(
            f"""
            <div class="container main-padding">
                <div class="text-title-footer main-padding"> Realizado por </div>
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
                <div class="container text-small main-padding">
                    Todo os ícones são do <a href="https://www.freepik.com/" target="_blank">Freepik </a> com permissão de uso mediante créditos.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


#  <a href="https://www.iadb.org/pt/sobre-o-bid/visao-geral" target="_blank">
#                     <img class="logo-footer"
#                     src="https://seeklogo.com/images/B/banco-interamericano-de-desenvolvimento-logo-0F13DDE475-seeklogo.com.png"
#                     title="logo BID">
#                 </a>


if __name__ == "__main__":
    main()