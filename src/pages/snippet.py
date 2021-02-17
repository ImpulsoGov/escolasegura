import streamlit as st
import utils

def genTermo():
	verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
	st.write(
		f"""
		<div style="text-align:center; padding-top:10px; padding-bottom:25px; background: #ff9147; margin-top:50px; margin-bottom:0px;">
			<img class="square" src="data:image/png;base64,{verify_icon}"> 
			<span style="color:#ffffff;"><b>Conheça nosso termo de responsabilidade</b></span>
		</div>
		""",
		unsafe_allow_html=True,
	)