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
#     urlpath = "http://localhost:8501/"
    urlpath = 'https://escolasegura-staging.herokuapp.com/'
    # urlpath = 'https://escolasegura.coronacidades.org/'
    utils.localCSS("inicio.css")
    utils.localCSS("localCSS.css")
    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    utils.appdescription(title="Escola Segura é uma iniciativa da Impulso Gov que oferece guias, protocolos e simuladores para auxiliar no planejamento de reabertura da rede pública de ensino!", subtitle="")

    
    # utils.gen_title(title="Como <b>retomar</b> as atividades presenciais?", subtitle="")
    title="Conheca os 10 passos para uma reabertura segura!"
    sub="Veja as nossas 10 etapas para retomada presencial das aulas."
    st.write(
        f"""
        <div class="conteudo row" style="margin-top:50px; margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div>
                    <div style="padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#2b14ff; color:white;">
                    {sub}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {title}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=guia10passos' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Acesse ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # utils.gen_title(title="Como podemos te <b>ajudar</b>?", subtitle="")
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
        <div class="conteudo row" style="margin-top: 30px; margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div>
                    <div style="padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#2b14ff; color:white;">
                    {simuladorsub}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {simulador}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=simulation' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Acesse ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
           <div class="col card-plan" style="width:100%;">
                <div>
                    <div style="padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#7ACCA9; color:white;">
                    {sub1}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {title1}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=duvidasfrequentes' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Acesse ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="width:100%;">
                <div>
                    <div style="padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#7ACCA9; color:white;">
                    {sub2}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {title2}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=inicio' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Acesse ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
           <div class="col card-plan" style="width:100%;">
                <div>
                    <div style="padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#7ACCA9; color:white;">
                    {sub3}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {title3}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=sobre' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Acesse ></button><br>
                                </a>
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
