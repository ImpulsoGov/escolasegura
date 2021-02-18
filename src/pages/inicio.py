import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout
import pages.referencesContainer as rc
import pages.footer as foo
import pages.snippet as tm
import pages.specialistContainer as spc
import amplitude
import session
import time
from pathlib import Path


def main():
    # urlpath = "http://localhost:8501/"
    urlpath = 'https://escolasegura-staging.herokuapp.com/'
    # urlpath = 'https://escolasegura.coronacidades.org/'

    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    utils.localCSS("localCSS.css")
    subtitle = """Veja guias e protocolos para facilitar uma reabertura planejada da 
    rede pública de ensino, respeitando boas práticas de distanciamento e segurança 
    sanitária para controle da Covid-19. Encontre as ferramentas corretas de acordo 
    com o status atual de sua abertura:
    <br>
    Confira o inicio alternativo <a href="https://escolasegura-staging.herokuapp.com/?page=inicio2" >aqui</a>."""
    utils.main_title(title="Seja <b>Bem Vindo</b> ao Escola Segura!", subtitle=subtitle)

    
    utils.gen_title(title="Como <b>retomar</b> as atividades presenciais?", subtitle="")
    title="CONHEÇA OS 10 RETOMAR PARA REABERTURA!"
    sub="Veja nossa RETOMAR os 10 passos para retomada presencial das aulas."
    st.write(
        f"""
        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div style="margin:10px">
                    <div>
                        <div class="card-title" >
                        {title}
                        </div>
                        <div><br>
                            {sub}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href='{urlpath}?page=guia10passos' target="_self">
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
                        <div class="card-title" >
                        {simulador}
                        </div>
                        <div><br>
                            {simuladorsub}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href='{urlpath}?page=simulation' target="_self">
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
            <div class="col card-plan" style="margin-top:20px; width:100%;">
                <div style="margin:10px;">
                    <div>
                        <div class="card-title" >
                        {title1}
                        </div>
                        <div><br>
                            {sub1}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href='{urlpath}?page=duvidasfrequentes' target="_self">
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="margin-top:20px; width:100%;">
                <div style="margin:10px;">
                    <div>
                        <div class="card-title" >
                        {title2}
                        </div>
                        <div><br>
                            {sub2}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href='{urlpath}?page=inicio' target="_self">
                                <button class="button"; style="border-radius: .25rem;">ver ></button><br>
                                </a><br>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="margin-top:20px; width:100%;">
                <div style="margin:10px;">
                    <div>
                        <div class="card-title" >
                        {title3}
                        </div>
                        <div><br>
                            {sub3}
                            <div align="center" style="padding-bottom: 10px;">
                                <a href='{urlpath}?page=sobre' target="_self">
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
    
    tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()
