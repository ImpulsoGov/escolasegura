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
    """ 
    This function generates Escola Segura webpage
    Parameters: 
        session_state (type): section dataset
    """
    if os.getenv("IS_HEROKU") == "TRUE":
        urlpath = os.getenv("urlpath")
    else:
        urlpath = 'https://escolasegura.coronacidades.org/'
        GOOGLE_ANALYTICS_CODE = "UA-161606940-3"
        import pathlib
        from bs4 import BeautifulSoup
        TAG_MANAGER = """
            function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','GTM-5ZZ5F66');
            """
        GA_JS = (
            """
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '%s');
        """
            % GOOGLE_ANALYTICS_CODE
        )
        index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
        soup = BeautifulSoup(index_path.read_text(), features="lxml")
        if not soup.find(id="google-analytics-loader"):
            script_tag_import = soup.new_tag(
                "script",
                src="https://www.googletagmanager.com/gtag/js?id=%s"
                % GOOGLE_ANALYTICS_CODE,
            )
            soup.head.append(script_tag_import)
            script_tag_loader = soup.new_tag("script", id="google-analytics-loader")
            script_tag_loader.string = GA_JS
            soup.head.append(script_tag_loader)
            script_tag_manager = soup.new_tag("script", id="google-tag-manager")
            script_tag_manager.string = TAG_MANAGER
            soup.head.append(script_tag_manager)
            script_tag_manager_body = soup.new_tag(
                "script",
                src="https://www.googletagmanager.com/gtm.js?id=GTM-5ZZ5F66"
            )
            soup.head.append(script_tag_manager_body)
            index_path.write_text(str(soup))    
    utils.localCSS("inicio.css")
    utils.localCSS("localCSS.css")
    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    utils.appdescription(title="A Escola Segura foi criada para apoiar integrantes de secretarias de educação e gestores escolares de todo o Brasil na retomada de atividades presenciais em escolas da rede pública, após o fechamento provocado pela Covid-19. Em 10 passos, mostramos como preparar e gerir o retorno escolar e oferecemos ferramentas para apoiar as etapas desse processo. Queremos contribuir para uma retomada segura das aulas presenciais e reduzir os prejuízos que o fechamento das escolas tem trazido ao aprendizado de milhões de estudantes brasileiros.", subtitle="")

    
    # utils.gen_title(title="Como <b>retomar</b> as atividades presenciais?", subtitle="")
    title="Siga 10 passos para reabrir escolas com segurança!"
    sub="Priorize os passos de acordo com a realidade da sua rede de ensino. É importante seguir todas as recomendações para garantir uma reabertura mais segura. "
    st.write(
        f"""
        <div class="conteudo row" style="margin-top:50px; margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div>
                    <div style="font-size:1.3rem; padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#2b14ff; color:white;">
                    {title}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {sub}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=guia10passos' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Conheça os passos ></button><br>
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
    simulador="Simule o retorno"
    simuladorsub = "Informe os dados da sua rede ou escola e calcule quantas turmas podem voltar em segurança e quais materiais você precisa providenciar."
    title1="Quem Somos"
    sub1="Reunimos organizações atuantes nas áreas de educação, saúde e análise de dados para criar este conteúdo técnico, fundamentado em fontes nacionais e internacionais, para apoiar gestores escolares neste desafio."
    title2="Dúvidas Frequentes"
    sub2="Saiba o que outros gestores e gestoras públicos já perguntaram sobre o desafio da retomada das atividades presenciais em escolas."
    # title3="Quem Somos"
    # sub3="Saiba mais sobre os envolvidos e o desenvolvimento da plataforma."
    st.write(
        f"""
        <div class="conteudo row" style="margin-top: 30px; margin-right:0px; margin-left:0px;">
            <div class="card-plan" style="width:100%;">
                <div>
                    <div style="font-size:1.3rem; padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#2b14ff; color:white;">
                    {simulador}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {simuladorsub}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=simulation' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Simule já ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="conteudo row" style="margin-right:0px; margin-left:0px;">
           <div class="col card-plan" style="width:100%; margin-top:15px; margin-botton:15px;">
                <div>
                    <div style="font-size:1.3rem; padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#7ACCA9; color:white;">
                    {title1}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {sub1}
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=sobre' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Saiba mais ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col card-plan" style="width:100%; margin-top:15px; margin-botton:15px;">
                <div>
                    <div style="font-size:1.3rem; padding:5px; text-align: center; border-top-right-radius: 0.8rem; border-top-left-radius: 0.8rem; background:#7ACCA9; color:white;">
                    {title2}
                    </div>
                    <div style="margin:10px">
                        <div class="card-title">
                        {sub2}
                        <br><br>
                        </div>
                        <div>
                            <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                <a href='{urlpath}?page=duvidasfrequentes' target="_self">
                                <button class="button"; style="border-radius: 0.8rem;">Confira ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>
        """,
        unsafe_allow_html=True,
    )
    
    # tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()
