import streamlit as st
import utils
import pages.snippet as tm
import pages.header as he
import pages.footer as foo
import os

if os.getenv("IS_HEROKU") == "TRUE":
    urlpath = os.getenv("urlpath")
else:
    urlpath = 'https://escolasegura.coronacidades.org/'

def main():
    """ 
    This is a function that returns the "about" page
      
    Parameters: 
        session_state (type): section dataset
    """
    he.genHeader("termo")
    st.write(
        f"""
        <div class="conteudo main-title" style="padding-top: 50px;"> 
            <b>Termos de Uso</b>
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            1. Estou ciente que as sugestões e recomendações apresentadas na plataforma Escola Segura são meramente indicativas, feitas a partir de dados oficiais públicos e estudos referenciados já publicados. 
    <br><br>2. Estou   ciente   de   que   a   utilização   dos   referenciais   da   plataforma   não corresponde a uma certificação de melhores práticas para a reabertura de escolas. 
    <br><br>3. Estou   ciente   que   a   plataforma   Escola   Segura  não configura qualquer obrigação ou responsabilidade perante as decisões efetivadas pelos gestores públicos.
    <br><br>4. Estou  ciente  que é  responsabilidade exclusiva da rede pública e degestores públicos a tomada de qualquer decisão a respeito da reaberturade   escolas,   inclusive   quanto   à   pertinência   dos   cenários   produzidos   pela plataforma Escola Segura com a realidade local.
    <br><br>5. Estou  ciente  é que  responsabilidade exclusiva da rede pública e degestores públicos   a   avaliação   e   a   eventual   adoção   de   medidas   deprevenção   necessárias   para   garantir   a   adequação   sanitária   dosestabelecimentos   públicos   de   ensino   para   os   diferentes   cenários   dereabertura de escolas. 
    <br><br>6. Estou   ciente   da   metodologia   utilizada   pela   plataforma   Escola   Segura, disponibilizada e atualizada <a href="{urlpath}?page=sobre">aqui</a>.
        </div>
        """,
        unsafe_allow_html=True,
    )
    utils.localCSS("localCSS.css")
    # utils.gen_title(title="Quem somos?")

    tm.genGuia()
    foo.genFooter()


if __name__ == "__main__":
    main()
