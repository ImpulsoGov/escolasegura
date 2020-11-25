import streamlit as st
import utils

def main(session_state):
    utils.localCSS("style.css")
    utils.genHeroSection(
        title1="Escola", title2="Segura", header=True,
    )
    st.write(
        f"""
        <div class="container main-padding">
        <div class="text-title-section bold"> Quem somos? </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()