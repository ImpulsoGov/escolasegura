import streamlit as st
import time
import os
import yaml
import requests

def get_config(url=os.getenv("CONFIG_URL")):
    return yaml.load(requests.get(url).text, Loader=yaml.FullLoader)

def localCSS(filename):
    with open(filename) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def stylizeButton(name, style_string, session_state, others=dict()):
    """ adds a css option to a button you made """
    session_state.button_styles[name] = [style_string, others]


def applyButtonStyles(session_state):
    """ Use it at the end of the program to apply styles to buttons as defined by the function above """
    time.sleep(0.1)
    html = ""
    for name, style in session_state.button_styles.items():
        parts = (
            style[0]
            .replace("\n", "")
            .replace("    ", "")
            .replace("; ", "&")
            .replace(";", "&")
            .replace(":", "=")
        )
        other_args = "&".join(
            [str(key) + "=" + str(value) for key, value in style[1].items()]
        )
        html += f"""
        <iframe src="resources/redo-button.html?name={name}&{parts}&{other_args}" style="height:0px;width:0px;">
        </iframe>"""
    st.write(html, unsafe_allow_html=True)

def filter_place(df, level, state_id=None, administrative_level=None, city_name=None):
    if level == "state":
        return df["state_id"].sort_values().unique()
    elif level == "city":
        data = df[df["state_id"] == state_id]
        return data["city_name"].sort_values().unique()
    else:
        data = df[df["state_id"] == state_id]
        if city_name != None and city_name != "Todos":
            data = df[df["city_name"] == city_name]
        return data["administrative_level"].sort_values().unique()
