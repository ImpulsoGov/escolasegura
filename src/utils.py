import streamlit as st
import time
import os
import yaml
import requests
from pathlib import Path
import base64
import session 
from ua_parser import user_agent_parser

def get_server_session():
    return session._get_session_raw()

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


def load_image(path):
    return base64.b64encode(Path(str(os.getcwd()) + "/" + path).read_bytes()).decode()

def load_markdown_content(relative_path):
    # Paths are relative to /content directory
    full_path = f"{os.getcwd()}/content/{relative_path}"

    # Read File
    with open(full_path, 'r') as file:
        text = file.read()

    return text

def parse_headers(request):
    """ Takes a raw streamlit request header and converts it to a nicer dictionary """
    data = dict(request.headers.items())
    ip = request.remote_ip
    if "Cookie" in data.keys():
        data["Cookie"] = dict([i.split("=", 1) for i in data["Cookie"].split("; ")])
        data["cookies_initialized"] = True
    else:
        data["Cookie"] = dict()
        data["cookies_initialized"] = False
    if "user_public_data" in data["Cookie"].keys():
        data["Cookie"]["user_public_data"] = dict(
            [i.split("|:", 1) for i in data["Cookie"]["user_public_data"].split("|%")]
        )
    data["Remote_ip"] = ip
    data.update(parse_user_agent(data["User-Agent"]))
    return data

def parse_user_agent(ua_string):
    in_data = user_agent_parser.Parse(ua_string)
    out_data = dict()
    data_reference = [
        ["os_name", ["os", "family"]],
        ["os_version", ["os", "major"]],
        ["device_manufacturer", ["device", "brand"]],
        ["device_model", ["device", "model"]],
        ["platform", ["user_agent", "family"]],
        ["app_version", ["user_agent", "major"]],
    ]
    for key_in, keys_out in data_reference:
        try:
            out_data["ua_" + key_in] = in_data[keys_out[0]][keys_out[1]]
        except:
            out_data["ua_" + key_in] = None
    return out_data

def genHeroSection(title1: str, title2: str, header: bool):

    if header:
        header = """<a href="https://coronacidades.org/" target="blank" class="logo-link"><span class="logo-header" style="font-weight:bold;">corona</span><span class="logo-header" style="font-weight:lighter;">cidades</span> <br></a>"""
    else:
        header = """<br>"""

    icon = load_image("imgs/escolasegura_favicon.png")

    st.write(
        f"""
        <div class="container">
            {header}
        <div class="grid-container-header">
            <div class="div1-head">
                <img class="img-logo-header" src="data:image/png;base64,{icon}">
            </div>
            <div class="div2-head">
                <a href="" class="logo-link">
                <span class="hero-container-product main-blue-span">{title1}</span>
                <div class="br-hero"></div>
                <span class="hero-container-product main-blue-span">{title2}</span>
                </a>
            </div>
        </div>
        </div><br>
        <div class="hero-container-subtitle">
            Salas <b>abertas</b> para estudantes<br>Portas <b>fechadas</b> para a Covid-19
        </div>
        """,
        unsafe_allow_html=True,
    )