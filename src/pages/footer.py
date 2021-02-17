import streamlit as st
import utils

def genFooter():

	""" 
    This is a function that returns the "Footer" session 
    
    """
	escola = utils.load_image("imgs/escolasegura.png")
	bidicon = utils.load_image("imgs/logo-bid.png")
	imaginableicon = utils.load_image("imgs/logo-imaginable.png")
	formaricon = utils.load_image("imgs/logo-formar.png")
	impulso_icon = utils.load_image("imgs/logo-impulso.png")

	st.write(
		f"""
			<div class="base-wrapper row" style="padding-left:60px; padding-top:20px; margin-top:0px; margin-left:0px; margin-bottom:0px;margin-right:0px; background:#f8f8f8">
				<div>
					<img class="escola-footer" style="margin-bottom:2em;" src="data:image/png;base64,{escola}" title="logo Impulso"/>
				</div>
				<div>
					<span style="font-size:0.7em; font-color:#A8BFD2;">Realizado por:</span><br>
					<img class="logo-footer" style="margin-bottom:2em;" src="data:image/png;base64,{impulso_icon}" title="logo Impulso"/>
				</div>
				<div>
					<span style="font-size:0.7em; font-color:#A8BFD2;">Viabilizado por:</span><br>
					<img class="logo-footer" style="margin-bottom:2em;" src="data:image/png;base64,{imaginableicon}" title="logo Imagine"/>
					<img class="logo-footer" style="margin-bottom:2em;" src="data:image/png;base64,{bidicon}" title="logo BID"/>
					<img class="logo-footer" style="margin-bottom:2em;" src="https://captadores.org.br/wp-content/uploads/2016/02/lemann_logo_pref_vert_pos_rgb.png" tile="logo Lemann">
				</div>
				<div>
					<span style="font-size:0.7em; font-color:#A8BFD2;">Implementação:</span><br>
					<img class="logo-footer" style="margin-bottom:2em;" src="data:image/png;base64,{formaricon}" title="logo Formar"/>
				</div>
			</div>
		""",
		unsafe_allow_html=True,
	)

if __name__ == "__main__":
    main()