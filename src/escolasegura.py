# coding=utf-8
import streamlit as st
import yaml
import session
import time
import pages.about as sobre
import pages.simulationContainer as simulation
import pages.passos as passos
import pages.inicio as inicio
import pages.referencesContainer as referencias
import socket
import utils
import pages.simulationContainer as sc
from PIL import Image
import pathlib
from flask import Flask, request
from flask.wrappers import Request


st.set_page_config(
    page_title="Escola Segura", 
    page_icon=Image.open("imgs/escolasegura_favicon.png"),
    layout='wide',
    initial_sidebar_state='collapsed')

def main():
    """ 
    This function generates Escola Segura
    """

    # Remove menu da visualizacao
    hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

    # SESSION STATE
    time.sleep(
        0.05
    )  # minimal wait time so we give time for the user session to appear in steamlit
    session_state = session.SessionState.get(
        key=session.get_user_id(),
        update=False,
        state_name="Acre",
        state_id="AC",
        city_name="Todos",
        administrative_level="Todos",
        refresh=False,
        reset=False,
        already_generated_user_id=None,
        pages_open=None,
        amplitude_events=None,
        button_styles=dict(),
        continuation_selection=None,
        button_simule=0,
        section1_organize=False,
        section2_manage=False,
    )

    PAGES = {   
        "Inicio" : inicio,
        "Guia 10 passos" : passos,
        "Simulacão" : simulation,
        "Quem somos?" : sobre,
        "Fontes e Referências": referencias
    }

    page = st.sidebar.radio(
        "Menu", list(PAGES.keys()),
    )

    if __name__ == "__main__":
        PAGES[page].main()
        utils.applyButtonStyles(session_state)

if __name__ == "__main__":
    main()
