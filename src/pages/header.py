import streamlit as st
import utils

def genHeader():

	""" 
    This is a function that returns the "Footer" session 
    
    """
	escola = utils.load_image("imgs/escolasegura.png")

	st.write(
		f"""
			<div class="base-wrapper row" style="padding-left:60px; padding-top:20px; margin-top:0px; margin-left:0px; margin-bottom:0px;margin-right:0px; background-image: url('https://i.imgur.com/RhIe7on.png');">
				<div>
					<img class="escola-footer" style="margin-bottom:0px;" src="data:image/png;base64,{escola}" title="logo Impulso"/>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Inicio</span><br>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Guia 10 Passos</span><br>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Simulação</span><br>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Quem Somos</span><br>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Fontes e Referências</span><br>
				</div>
				<div style="padding-top:20px; padding-bottom:25px;" >
					<span style="font-size:1.05em; font-color:#A8BFD2;">Dúvidas Frequentes</span><br>
				</div>
			</div>
		""",
		unsafe_allow_html=True,
	)

if __name__ == "__main__":
    main()