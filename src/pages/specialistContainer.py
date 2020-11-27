import streamlit as st


def genSpecialistContainer():
    st.write(
        f"""
        <div class="container">
                <div class="left-margin card-plan">
                        <div style="margin:10px">
                            <div class="left-margin">
                                <div class="text-title-section minor-padding"> 
                                Encontro com o <span class="bold main-orange-span">especialista </span></div>
                                <div class="minor-padding main-black-span"><br>
                                Realizamos, semanalmente, um encontro online com <b>Wanderson de Oliveira</b>, 
                                epidemiologista e ex-secretário nacional de vigilância em saúde, para solucionar dúvidas da 
                                gestão pública sobre o processo de retomada de atividades presenciais na rede de ensino. 
                                <div class="main-padding" align="center" style="padding-bottom: 10px;">
                                    <a href="https://forms.gle/DQTfXau4L1eyzHdn7" target=_blank>
                                    <button class="button"; style="border-radius: .25rem;">participe!></button><br>
                                    </a><br>
                                </div>
                            </div>
                        </div>
                </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()

