# coding=utf-8
import streamlit as st
import yaml
import time
from pages import inicio, inicio2
import pages.about as sobre
import pages.passos as guiapassos
import pages.simulacao as simulacao
import pages.referencesContainer as referencias
import pages.duvidas as duvidas
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

# Remove menu da visualizacao
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>

    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# # SESSION STATE
# time.sleep(
#     0.05
# )  # minimal wait time so we give time for the user session to appear in steamlit
# session_state = session.SessionState.get(
#     key=session.get_user_id(),
#     update=False,
#     state_name="Acre",
#     state_id="AC",
#     city_name="Todos",
#     administrative_level="Todos",
#     refresh=False,
#     reset=False,
#     already_generated_user_id=None,
#     pages_open=None,
#     amplitude_events=None,
#     button_styles=dict(),
#     continuation_selection=None,
#     button_simule=0,
#     section1_organize=False,
#     section2_manage=False
# )
# utils.applyButtonStyles(session_state)
# PAGES[page].main(session_state)
# # query_params = st.experimental_get_query_params()
# # page_param = query_params.get("page", [0])
# # if query_params:
# #     PAGES[page_param[0]].main(session_state)
# # else:
# #     PAGES[page].main(session_state)


def main():
    """ 
    This function generates Escola Segura
    """

    # SESSION STATE
    time.sleep(
        0.05
    )  # minimal wait time so we give time for the user session to appear in steamlit

    PAGES = {   
        "inicio" : inicio,
        "inicio2" : inicio2,
        "guia10passos" : guiapassos,
        "simulation" : simulacao,
        "sobre" : sobre,
        "referencias": referencias,
        "duvidasfrequentes" : duvidas
    }
    # page = st.sidebar.radio(
    #     "Menu", list(PAGES.keys()),
    # )
    query_params = st.experimental_get_query_params()
    page_param = query_params.get("page", [0])
    if query_params:
        PAGES[page_param[0]].main()
    else:
        inicio.main()

    # if query_params:
    #     PAGES[page_param[0]].main()
    # else:
    #     PAGES[page].main()
    

if __name__ == "__main__":
    main()

# app = Flask(__name__)

# @app.route('/')
# def main():
# #     # inicio.main()
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=8501)
#     # app.run(host="localhost", debug=True, port=8501)


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def main():
#     return inicio.main()

# @app.route('/<path:entry>')
# def hello(entry):
#     if entry=='guia10passos':
#         return 'Guia Passos!'
#     elif entry=='simulador':
#         return 'Simulador!'
#     else:
#         return "Hello World!"

# if __name__ == '__main__':
#     app.run()

# x = st.slider('Pick a number')
# st.write('You picked:', x)

# if not hasattr(st, 'already_started_server'):
#     # Hack the fact that Python modules (like st) only load once to
#     # keep track of whether this file already ran.
#     st.already_started_server = True

#     st.write('''
#         The first time this script executes it will run forever because it's
#         running a Flask server.

#         Just close this browser tab and open a new one to see your Streamlit
#         app.
#     ''')

#     from flask import Flask

#     app = Flask(__name__)

#     @app.route('/foo')
#     def serve_foo():
#         x = st.slider('Pick a number')
#         st.write('You picked:', x)
#         return 'This page is served via Flask!'

#     app.run(port=8888)


# # We'll never reach this part of the code the first time this file executes!

# # Your normal Streamlit app goes here:
# x = st.slider('Pick a number')
# st.write('You picked:', x)
