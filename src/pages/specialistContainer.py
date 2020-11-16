import streamlit as st

def genSpecialistContainer():
    st.write(
        f"""
        <div class="container">
                <div class="left-margin card-plan">
                    <a href="https://forms.gle/MrkuQ9H4WwEYjbw98" target=_blank>
                        <div style="margin:10px">
                            <div class="left-margin">
                                <div class="text-title-section minor-padding"> 
                                Fale com o especialista</div>
                                <div class="minor-padding main-black-span"><br>
                                <b>Wanderson</b> é ... e estará disponível para..
                                <div align="center" style="padding-bottom: 10px;">
                                    <button class="button"; style="border-radius: .25rem;">Veja Aqui</button><br>
                                </div>
                            </div>
                        </div>
                    </a>
                </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    
if __name__ == "__main__":
    main()