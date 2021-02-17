import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout

import pages.planContainer as pc
import pages.simulationContainer as sc
import pages.prepareContainer as prc
import pages.monitorContainer as mc
import pages.referencesContainer as rc
import pages.footerContainer as fc
import pages.footer as foo
import pages.snippet as tm
import pages.specialistContainer as spc
import amplitude
import session
import escolasegura
import time


def main():
    # import pathlib
    # from bs4 import BeautifulSoup
    # index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    # soup = BeautifulSoup(index_path.read_text(), features="lxml")
    # script_tag_import = soup.new_tag("script", src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css")
    # soup.head.append(script_tag_import)
    # script_tag_import2 = soup.new_tag("script", src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css")
    # soup.head.append(script_tag_import2)
    # script_tag_import3 = soup.new_tag("script", src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js")
    # soup.head.append(script_tag_import3)
    # script_tag_import4 = soup.new_tag("script", src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js")
    # soup.head.append(script_tag_import4)
    # import pathlib
    # from bs4 import BeautifulSoup
    # index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    # soup = BeautifulSoup(index_path.read_text(), features="lxml")
    # script_tag_import = soup.new_tag("script", src="https://kit.fontawesome.com/bdd89edb33.js")
    # soup.head.append(script_tag_import)

    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    utils.localCSS("localCSS.css")
    subtitle = """Veja guias e protocolos para facilitar uma reabertura planejada da 
    rede pública de ensino, respeitando boas práticas de distanciamento e segurança 
    sanitária para controle da Covid-19. Encontre as ferramentas corretas de acordo 
    com o status atual de sua abertura:"""
    utils.main_title(title="Seja <b>Bem Vindo</b> ao Escola Segura!", subtitle=subtitle)

    
    utils.gen_title(title="Como <b>retomar</b> as atividades presenciais?", subtitle="")
    title="CONHEÇA OS 10 PASSOS PARA REABERTURA!"
    sub="Veja nossa guia os 10 passos para retomada presencial das aulas."
    st.write(
        f"""
        <div class="conteudo row">
            <div class="col flip" style="padding-top:10px; margin-right:0px; margin-left:0px;">
                <div class="front" style="background-image: url(https://images.pexels.com/photos/540518/pexels-photo-540518.jpeg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb)">
                </div>
                <div class="back">
                   <h2>{title}</h2>
                   <p>{sub}</p>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        f"""
        <div class="conteudo"> 
            <hr style="height:5px;color:#ff9147;background-color:#ff9147">
        </div>
        """,
        unsafe_allow_html=True,
    )



    utils.gen_title(title="Como podemos te <b>ajudar</b>?", subtitle="")
    title1="Quero saber por onde começar"
    sub1="Ainda estou começando planejar a abertura."
    title2="Quero me planejar"
    sub2="Quero descobrir como organizar professores e alunos em diferentes turmas, e quais os recursos necessários."
    title3="Quero gerir a rede"
    sub3="Já tenho unidades abertas e quero acompanhar."
    st.write(
        f"""
        <div class="conteudo" style="padding-top:10px;">
            <div class="flip">
                <div class="front" style="background-image: url(https://images.pexels.com/photos/540518/pexels-photo-540518.jpeg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb)">
                </div>
                <div class="back">
                   <h2>{title1}</h2>
                   <p>{sub1}</p>
                </div>
            </div>
            <div class="flip">
                <div class="front" style="background-image: url(https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb)">
                </div>
                <div class="back">
                   <h2>{title2}</h2>
                   <p>{sub2}</p>
                </div>
            </div>
            <div class="flip">
                <div class="front" style="background-image: url(https://images.pexels.com/photos/36717/amazing-animal-beautiful-beautifull.jpg?w=1260&h=750&dpr=2&auto=compress&cs=tinysrgb)">
                </div>
                <div class="back">
                   <h2>{title3}</h2>
                   <p>{sub3}</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write(
        f"""
        <div class="conteudo"> 
            <hr style="height:5px;color:#ff9147;background-color:#ff9147">
        </div>
        """,
        unsafe_allow_html=True,
    )



    utils.gen_title(title="<b>Simulador</b>: como organizar a rebertura?", subtitle="")
    st.write(
        f"""
        <div class="conteudo" style="padding-bottom: 10px;">
            Descobra como organizar professores, salas e alunos e quais os materiais necessários para cumprir os protocolors sanitários.           
        </div>
        <div class="conteudo" align="center">
            <a href="" target=_blank>
            <button class="button"; style="border-radius: .25rem;">veja aqui ></button><br>
            </a><br>
            <hr style="height:5px;color:#ff9147;background-color:#ff9147">
        </div>
        """,
        unsafe_allow_html=True,
    )


    spc.genSpecialistContainer()
    tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()