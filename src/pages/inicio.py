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
        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em; color:#ff9147; font-weight:bold;">
                        {title}
                        </div>
                        <div><br>
                            {sub}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
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



    utils.gen_title(title="Como podemos te <b>ajudar</b>?", subtitle="")
    simulador="Simulador: como organizar a rebertura?"
    simuladorsub = "Descobra como organizar professores, salas e alunos e quais os materiais necessários para cumprir os protocolors sanitários. "
    title1="Dúvidas Frequentes"
    sub1="Veja respostas para as principais dúvidas."
    title2="Conte com a Gente"
    sub2="Entre em contato com a gente para se atualizar e tirar suas dúvidas."
    title3="Quem Somos"
    sub3="Saiba mais sobre os envolvidos e o desenvolvimento da plataforma."
    st.write(
        f"""
        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em; color:#ff9147; font-weight:bold;">
                        {simulador}
                        </div>
                        <div><br>
                            {simuladorsub}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
            <div class="col card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em; color:#ff9147; font-weight:bold;">
                        {title1}
                        </div>
                        <div><br>
                            {sub1}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em; color:#ff9147; font-weight:bold;">
                        {title2}
                        </div>
                        <div><br>
                            {sub2}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div style="word-break: break-word; font-size:1.5em; color:#ff9147; font-weight:bold;">
                        {title3}
                        </div>
                        <div><br>
                            {sub3}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href="" target=_blank>
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
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


#     spc.genSpecialistContainer()
    tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()
