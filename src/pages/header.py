import streamlit as st
import utils

def genHeader(active):

	""" 
    This is a function that returns the "Footer" session 
    
    """
	escola = utils.load_image("imgs/escolasegura.png")
	header = utils.load_image("imgs/grey_header.png")
	# urlpath = 'http://localhost:8501/'
	urlpath = 'https://escolasegura-staging.herokuapp.com/'
	# urlpath = 'https://escolasegura.coronacidades.org/'
	# import pdb; pdb.set_trace()
	if active=="guia10passos":
		st.write(
			f"""
				<div class="conteudo" id="navbar">
				  <a href="{urlpath}?page=inicio" style="padding-top:0px; padding-bottom:0px;"><img class="escola-navbar" src="data:image/png;base64,{escola}" title="logo Impulso"/></a>
				  <a href="{urlpath}?page=inicio">Início</a>
				  <a class="active" href="{urlpath}?page=guia10passos">Guia 10 Passos</a>
				  <a href="{urlpath}?page=simulation">Simule o retorno</a>
				  <a href="{urlpath}?page=sobre">Quem Somos</a>
				  <a href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>
				</div>
			""",
			unsafe_allow_html=True,
		)
	elif active=="sobre":
		st.write(
			f"""
				<div class="conteudo" id="navbar">
				  <a href="{urlpath}?page=inicio" style="padding-top:0px; padding-bottom:0px;"><img class="escola-navbar" src="data:image/png;base64,{escola}" title="logo Impulso"/></a>
				  <a href="{urlpath}?page=inicio">Início</a>
				  <a href="{urlpath}?page=guia10passos">Guia 10 Passos</a>
				  <a href="{urlpath}?page=simulation">Simule o retorno</a>
				  <a class="active" href="{urlpath}?page=sobre">Quem Somos</a>
				  <a href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>
				</div>
			""",
			unsafe_allow_html=True,
		)
	elif active=="simulation":
		st.write(
			f"""
				<div class="conteudo" id="navbar">
				  <a href="{urlpath}?page=inicio" style="padding-top:0px; padding-bottom:0px;"><img class="escola-navbar" src="data:image/png;base64,{escola}" title="logo Impulso"/></a>
				  <a href="{urlpath}?page=inicio">Início</a>
				  <a href="{urlpath}?page=guia10passos">Guia 10 Passos</a>
				  <a class="active" href="{urlpath}?page=simulation">Simule o retorno</a>
				  <a href="{urlpath}?page=sobre">Quem Somos</a>
				  <a href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>
				</div>
			""",
			unsafe_allow_html=True,
		)
	elif active=="duvidasfrequentes":
		st.write(
			f"""
				<div class="conteudo" id="navbar">
				  <a href="{urlpath}?page=inicio" style="padding-top:0px; padding-bottom:0px;"><img class="escola-navbar" src="data:image/png;base64,{escola}" title="logo Impulso"/></a>
				  <a href="{urlpath}?page=inicio">Início</a>
				  <a href="{urlpath}?page=guia10passos">Guia 10 Passos</a>
				  <a href="{urlpath}?page=simulation">Simule o retorno</a>
				  <a href="{urlpath}?page=sobre">Quem Somos</a>
				  <a class="active" href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>
				</div>
			""",
			unsafe_allow_html=True,
		)

# <a href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>
# <a class="active" href="{urlpath}?page=duvidasfrequentes">Dúvidas Frequentes</a>


	# st.write(
	# 	f"""
	# 	<nav class="navbar navbar-default navbar-fixed-top navbar-shrink">
	#         <div class="container">
	#             <!-- Brand and toggle get grouped for better mobile display -->
	#             <div class="navbar-header page-scroll">
	#                 <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
	#                     <span class="sr-only">Toggle navigation</span>
	#                     <span class="icon-bar"></span>
	#                     <span class="icon-bar"></span>
	#                     <span class="icon-bar"></span>
	#                 </button>
	#                 <a class="navbar-brand page-scroll" href="#page-top">Celine Is Awesome</a>
	#             </div>
	#             <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
	#                 <ul class="nav navbar-nav navbar-right">
	#                     <li class="hidden active">
	#                         <a href="#page-top"></a>
	#                     </li>
	#                     <li class="">
	#                         <a class="page-scroll" href="#services">Services</a>
	#                     </li>
	#                     <li class="">
	#                         <a class="page-scroll" href="#portfolio">Portfolio</a>
	#                     </li>
	#                     <li class="">
	#                         <a class="page-scroll" href="#about">About</a>
	#                     </li>
	#                     <li class="">
	#                         <a class="page-scroll" href="#team">Team</a>
	#                     </li>
	#                     <li class="">
	#                         <a class="page-scroll" href="#contact">Contact</a>
	#                     </li>
	#                 </ul>
	#             </div>
	#         </div>
	#     </nav>""",
	# unsafe_allow_html=True,
	# )


if __name__ == "__main__":
    main()
