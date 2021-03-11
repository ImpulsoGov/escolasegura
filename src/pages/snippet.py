import streamlit as st
import utils
import os

if os.getenv("IS_HEROKU") == "TRUE":
    urlpath = os.getenv("urlpath")
else:
    urlpath = 'https://escolasegura.coronacidades.org/'

def genTermo():
	verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
	st.write(
		f"""
		<div style="text-align:center; padding-top:10px; padding-bottom:25px; background: #ff9147; margin-top:50px; margin-bottom:0px;">
			<a href="{urlpath}?page=termo" target="_self" style="text-decoration: none;"><img class="square" src="data:image/png;base64,{verify_icon}"> 
			<span style="color:#ffffff;"><b>Conheça nosso termo de responsabilidade</b></span></a>
		</div>
		""",
		unsafe_allow_html=True,
	)

def genSimule():
	simulation_icon = utils.load_image("imgs/simulation_main_icon.png")
	st.write(
		f"""
		<div style="text-align:center; padding-top:10px; padding-bottom:25px; background: #ff9147; margin-top:50px; margin-bottom:0px;">
			<a href='{urlpath}?page=simulation' target="_self" style="text-decoration: none;"><img class="square" src="data:image/png;base64,{simulation_icon}"> 
			<span style="color:#ffffff;"><b>Simule o retorno aqui e calcule o que é necessário para a retomada</b></span>
			</a>
		</div>
		""",
		unsafe_allow_html=True,
	)

def genGuia():
	plan_icon = utils.load_image("imgs/monitor_plan_icon.png")	
	st.write(
		f"""
		<div style="text-align:center; padding-top:10px; padding-bottom:25px; background: #ff9147; margin-top:50px; margin-bottom:0px;">
			<a href='{urlpath}?page=guia10passos' target="_self" style="text-decoration: none;"><img class="square" src="data:image/png;base64,{plan_icon}"> 
			<span style="color:#ffffff;"><b>Conheça nosso Guia de 10 Passos.</b></span>
			</a>
		</div>
		""",
		unsafe_allow_html=True,
	)
