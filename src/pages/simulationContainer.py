import streamlit as st
import utils
import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout

from model.get_school_return_data import entrypoint


def genSimulationResult(params, config):

    result = entrypoint(params, config)

    st.write(
        f"""
        <div class="container main-padding">
                <div class="subtitle-section minor-padding"> RESULTADO DA SIMULAÇÃO </div>
                <p>Com os valores selecionados acima, os resultados da sua rede para os 2 modelos de retorno:</p>
                <div class="row">
                    <div class="col main-padding">
                        <div class="card-simulator-up lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span uppercase">EQUITATIVO</div>
                            <div>Todos os alunos retornam ao menos 1 vez por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087166.svg" title="Freepik"> </div>
                                <div class="div2 card-number">{result["equitative"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087177.svg" title="Freepik"> </div>
                                <div class="div2"> <span class="card-number">{result["equitative"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold"> professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 1x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator-bottom light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra </div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937325.svg" title="Freepik"></div>
                                <div class="div2 card-number"> {result["equitative"]["total_masks"]} </div>
                                <div class="div3 bold"> máscaras por semana</div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2622/2622386.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["equitative"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937355.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {int(result["equitative"]["total_sanitizer"])} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana</div>
                            </div>
                        </div> 
                    </div>
                    <div class="col main-padding">
                        <div class="card-simulator-up lighter-blue-green-bg">
                            <div class="card-title-section main-blue-span">PRIORITÁRIO</div>
                            <div>Número limitado de alunos retorna 5 vezes por semana.</div>
                            <div class="grid-container-simulation-type minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087166.svg" title="Freepik"> </div>
                                <div class="div2 card-number">{result["priority"]["num_returning_students"]} </div>
                                <div class="div3 bold"> alunos retornam às aulas </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (2 horas/dia)</div>
                            </div>
                            <div class="grid-container-simulation-type">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/1087/1087177.svg" title="Freepik"> </div>
                                <div class="div2"> <span class="card-number">{result["priority"]["num_returning_teachers"]}</span> </div>
                                <div class="div3 bold">  professores retornam </div>
                                <div class="div4"> </div>
                                <div class="div5 card-number" style="font-size: 1.5rem"> 5x </div>
                                <div class="div6"> por semana (8 horas/dia) </div>
                            </div>
                        </div>
                        <div class="card-simulator-bottom light-blue-green-bg minor-padding">
                            <div class="card-title-section main-blue-span uppercase">Materiais para compra </div>
                            <p>Será necessário providenciar para o retorno...</p>
                            <div class="grid-container-simulation-material minor-padding">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937325.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_masks"]} </div>
                                <div class="div3 bold" > máscaras por semana </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2622/2622386.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {result["priority"]["total_thermometers"]} </div>
                                <div class="div3 bold"> termômetros </div>
                            </div>
                            <div class="grid-container-simulation-material">
                                <div class="div1"> <img class="icon-cards" src="https://www.flaticon.com/svg/static/icons/svg/2937/2937355.svg" title="Freepik"> </div>
                                <div class="div2 card-number"> {int(result["priority"]["total_sanitizer"])} </div>
                                <div class="div3 bold"> litros de álcool em gel por semana </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>               
            <div class="minor-padding">
                <div class="minor-padding lighter-blue-green-bg" style="border-radius:5px;">
                    <div style="padding:10px;">
                       <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="_blank">
                        <img class = "icon-cards"
                         src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnPjxwYXRoIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgZD0ibTI1NiAwYy0xNDEuMTY0MDYyIDAtMjU2IDExNC44MzU5MzgtMjU2IDI1NnMxMTQuODM1OTM4IDI1NiAyNTYgMjU2IDI1Ni0xMTQuODM1OTM4IDI1Ni0yNTYtMTE0LjgzNTkzOC0yNTYtMjU2LTI1NnptMCAwIiBmaWxsPSIjMmIxNGZmIiBkYXRhLW9yaWdpbmFsPSIjMjE5NmYzIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBkPSJtMzY4IDI3Ny4zMzIwMzFoLTkwLjY2Nzk2OXY5MC42Njc5NjljMCAxMS43NzczNDQtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzFzLTIxLjMzMjAzMS05LjU1NDY4Ny0yMS4zMzIwMzEtMjEuMzMyMDMxdi05MC42Njc5NjloLTkwLjY2Nzk2OWMtMTEuNzc3MzQ0IDAtMjEuMzMyMDMxLTkuNTU0Njg3LTIxLjMzMjAzMS0yMS4zMzIwMzFzOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFoOTAuNjY3OTY5di05MC42Njc5NjljMC0xMS43NzczNDQgOS41NTQ2ODctMjEuMzMyMDMxIDIxLjMzMjAzMS0yMS4zMzIwMzFzMjEuMzMyMDMxIDkuNTU0Njg3IDIxLjMzMjAzMSAyMS4zMzIwMzF2OTAuNjY3OTY5aDkwLjY2Nzk2OWMxMS43NzczNDQgMCAyMS4zMzIwMzEgOS41NTQ2ODcgMjEuMzMyMDMxIDIxLjMzMjAzMXMtOS41NTQ2ODcgMjEuMzMyMDMxLTIxLjMzMjAzMSAyMS4zMzIwMzF6bTAgMCIgZmlsbD0iI2ZhZmFmYSIgZGF0YS1vcmlnaW5hbD0iI2ZhZmFmYSIgc3R5bGU9IiI+PC9wYXRoPjwvZz48L3N2Zz4="
                         title="Freepik" /></a> <b>Veja mais materiais necessários para compra 
                        <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="_blank">
                        aqui</a>.</b>
                    </div>
                </div>
            </div>
            <div class="minor-padding" style="margin-left:0.5em;">
                <br><p>ℹ️<i> Para entender como realizamos os cálculos, leia abaixo a metodologia.</p></i>
            </div>
        """,
        unsafe_allow_html=True,
    )

def genSimulationContainer(df, config, session_state):
    st.write(
        f"""
        <div class="title-section">
            <p style="color:#2b14ff; font-size:21px;"><b>4 - Qual é o modelo de retorno híbrido mais adequado para mim e qual a melhor logística e materiais necessários para isso?</b></p>
        </div>
        <div class="container main-padding">
            <div class="text-title-section"> Simule o retorno </div>
                <div >
                    <div class="minor-padding">Analise qual o modelo de retorno mais adequado para sua realidade e calcule os recursos necessários para a retomada.
                    </div>
                    <div class="minor-padding">
                        <div class="text-title-section minor-padding" style="font-size:20px"> Entenda os modelos de retorno </div>
                            <div>
                                Uma parte essencial da reabertura é definir 
                                <b>quem pode retornar e como</b> - trazemos 2 modelos possíveis:
                            </div>
                        <div class="row main-padding" style="grid-gap: 1rem;">
                            <div class="col lighter-blue-green-bg card-simulator" style="border-radius:30px;">
                                <div class="row">
                                    <div class="col card-title-section">EQUITATIVO</div>
                                    <div class="col text-subdescription container">
                                        <b>Todos os alunos têm aula presencial ao menos 1 vez por semana.</b>
                                        <p></p>
                                        Prioriza-se de forma igualitária que alunos voltem para a escola, mesmo  
                                        que somente 1 dia. Atividades podem ser de reforço ou conteúdo.
                                    </div>
                                </div>
                            </div>
                            <div class="col light-blue-green-bg card-simulator" style="border-radius:30px">
                            <div class="row">
                                <div class="col card-title-section">PRIORITÁRIO</div>
                                <div class="col text-subdescription container">
                                    <b>Número limitado de alunos retorna 5 vezes por semana.</b>
                                <p></p>
                                O modelo prioriza o tempo que o aluno passa na escola, mesmo que para uma quantidade menor de alunos. 
                                Atividades podem ser de reforço ou conteúdo.
                            </div>
                        </div>
                        </div>
                    </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        f"""<br>
            <div class="container">
                <div class="text-title-section minor-padding" style="font-size:20px">Defina seu modelo de retorno</div><br>
                <div>
                    <div class="text-padding bold">1) Para qual etapa de ensino você está planejando?</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # TODO: colocar por estado somente também
    # if city_name:
    data = df[
        (df["city_name"] == session_state.city_name)
        & (df["administrative_level"] == session_state.administrative_level)
    ]
    col1_1, col1_2 = st.beta_columns([0.25, 1])

    with col1_1:
        education_phase = st.selectbox(
            "", data["education_phase"].sort_values().unique()
        )

        data = data[data["education_phase"] == education_phase]
    with col1_2:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write(
        f"""
            <br><div class="container text-padding bold">2) Utilize os filtros para os dados do Censo Escolar (2019):</div>
        """,
        unsafe_allow_html=True,
    )
    if "Rural" in data["school_location"].drop_duplicates().values:
        rural = ["Rural" if st.checkbox("Apenas escolas rurais") else "Todos"][0]

        data = data[(data["school_location"] == rural)]

    if "Sim" in data["school_public_water_supply"].drop_duplicates().values:
        water_supply = [
            "Sim" if st.checkbox("Apenas escolas com água encanada") else "Todos"
        ][0]

        data = data[(data["school_public_water_supply"] == water_supply)]
    st.write(
        f"""
        <div class="container main-padding bold">3) Ou informe seus dados abaixo:</div><br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col2_1, col2_2, col2_3, col2_4 = st.beta_columns([0.4, 0.4, 0.4, 0.5])

    params = dict()
    with col2_1:
        params["number_students"] = st.number_input(
            "Qual total de alunos da sua rede?",
            format="%d",
            value=data["number_students"].values[0],
            step=1,
        )

    with col2_2:
        params["number_teachers"] = st.number_input(
            "Qual total de professores da sua rede?",
            format="%d",
            value=data["number_teachers"].values[0],
            step=1,
        )

    with col2_3:
        params["number_classrooms"] = st.number_input(
            "Qual total de sala de aulas na sua rede?",
            format="%d",
            value=data["number_classroms"].values[0],
            step=1,
        )

    with col2_4:
        st.write(
            f"""
        <div class="container main-padding">
            <br>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.write(
        f"""
        <div class="container main-padding bold">4) Escolha as condições de retorno:</div><br>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.beta_columns(
        [0.35, 0.05, 0.4, 0.05, 0.4, 0.3]
    )

    with col3_1:
        perc_students = st.slider(
            "Percentual de alunos realizando atividades presenciais:", 0, 100, 100, 10
        )
        params["number_students"] = int(perc_students * params["number_students"] / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_students)}% dos alunos</i> - {str(params["number_students"])} alunos no total.<br><hr>
            </div>
        """,
            unsafe_allow_html=True,
        )

    with col3_2:
        st.write(
            f"""
            <div class="container main-padding">
                <br>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3_3:
        perc_teachers = st.slider(
            "Percentual de professores realizando atividades presenciais:",
            0,
            100,
            100,
            10,
        )
        params["number_teachers"] = int(perc_teachers * params["number_teachers"] / 100)

        st.write(
            f"""<div class="container">
            <i>Valor selecionado: {str(perc_teachers)}% dos alunos</i> - {str(params["number_teachers"])} professores no total.<br><hr>
            </div>
            """,
            unsafe_allow_html=True,
        )

    col3_4 = col3_2

    with col3_5:
        st.write(
            f"""<div class="minor-padding"> </div>""",
            unsafe_allow_html=True,
        )

        params["max_students_per_class"] = st.slider(
            "Máximo de alunos por sala:", 0, 20, 20, 1
        )

        st.write(
            f"""<div class="container">
                <i>Valor selecionado: {params["max_students_per_class"]} alunos por sala</i><br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )

    with col3_6:
        st.write(
            f"""<div class="container">
                <br>
                </div>
                <br>
            """,
            unsafe_allow_html=True,
        )

    with st.beta_expander("Simular retorno"):
        genSimulationResult(params, config)

    '''if st.button("Simular retorno"):
        if st.button("Esconder"):
            pass
        genSimulationResult()
    utils.stylizeButton(
        name="SIMULAR RETORNO",
        style_string="""
        box-sizing: border-box;
        border-radius: 15px; 
        width: 150px;padding: 0.5em;
        text-transform: uppercase;
        font-family: 'Oswald', sans-serif;
        background-color: #0097A7;
        font-weight: bold;
        text-align: center;
        text-decoration: none;font-size: 18px;
        animation-name: fadein;
        animation-duration: 3s;
        margin-top: 1.5em;""",
        session_state=session_state,
    )'''

    with st.beta_expander("Ler metodologia"):

        methodology_text = """
        ## Metodologia de Simule o Retorno

        ### O que é?

        O simulador é uma ferramenta de cálculo para o gestor planejar o retorno das atividades escolares definindo restrições e seguindo os protocolos sanitários indicados. 
        
        A partir dos valores e restrições inseridos pelo gestor, o simulador calcula o **número de alunos e professores que podem retornar** às atividades escolares e **os materiais necessários para compra**, incluindo máscaras descartáveis, termômetros e
        litros de álcool em gel (mais materiais podem ser acessados na planilha que disponibilizamos).

        ### Como fazer a simulação?

        Ao acessar a ferramenta, o gestor encontrará os seguintes campos para preenchimento:

        - **Total de alunos:** O gestor pode informar aqui o número total de alunos 
        inscritos no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

        - **Total de professores:** O gestor pode informar aqui o número de professores disponíveis 
        para dar aula no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

        - **Total de salas de aula:** O gestor pode informar aqui o total de salas de aula disponíveis 
        para retorno no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

        - **Percentual de alunos realizando atividades presenciais:** O gestor deve informar aqui o percentual de alunos
        dentre o **Total de alunos** indicado que estão previstos para retornar as atividades.

        - **Percentual de professores realizando atividades presenciais:**  O gestor deve informar aqui o percentual de professores 
        dentre o **Total de professores** indicado que estão previstos para retornar as atividades.

        - **Máximo de alunos por sala:** 
        O gestor deve indicar aqui o limite de alunos por sala de aula. 
        Por padrão, este valor é de 20 alunos por sala, que também é o máximo que permitimos ser escolhido a fim tentar limitar a transmissão da doença.

        - **Filtros da simulação**: (se aplicam aos valores padrões do Censo Escolar 2019)
            - *Apenas escolas rurais*: escolhe-se para retorno apenas escolas em regiões rurais com base no Censo 2019. Este filtro limita para somente os alunos, professores e salas em escolas nessas regiões.
            - *Apenas escolas com água encanada*: escolhe-se para retorno apenas escolas com água encanada (escolas com fornecimento de água da rede pública no Censo 2019). Este filtro limita para somente os alunos, professores e salas em escolas nessas regiões.

        ### Como calculamos o resultado?

        O simulador utiliza as informações: 
        - **A**: total de alunos x percentual de alunos que retornam
        - **P**: total de professores x percentual de professores que retornam
        - **S**: número de salas de aula disponíveis
        - **K**: máximo de alunos permitidos por sala 

        Além desses, são fixados valores para cada modelo de retorno:
        
        - **H**: horas disponíveis para aulas semanalmente (H = 40 horas por semana)
        - **D**: duração de cada aula em horas (D = 2 horas)
        - **N**: quantidade mínima de aulas por semana por aluno (equitativo: N = 1; prioritário: N = 5)

        Para determinar quantos alunos a rede escolar é capaz de receber, utilizamos o conceito de **oportunidade**: uma oportunidade corresponde a um aluno assistir uma aula inteira. Como cada aula pode ter até **K** alunos (máximo por turma), a **quantidade de oportunidades de aulas na rede** é dada por $K \\times O$, onde **O** corresponde à oferta total de aulas na rede.

        A oferta de aulas na rede (**O**) depende diretamente da disponibilidade de professores e salas. Dado o total de horas disponíveis na semana (**H**) e a duração definida de uma aula (**D**), o máximo de aulas que podem ser oferecidas por professor/sala é dado por $Q = \left\lfloor \\frac{ H }{ D } \\right\\rfloor$.

        Assim, a oferta total de aulas (**O**) é dada por:

        $$ 
        O = Q \\times \min{ ( S, P ) } 
        $$

        Ao mesmo tempo, cada aluno deve ter uma quantidade **N** de aulas por semana, que é dada pelo modelo de retorno escolhido. Assim, a capacidade efetiva de retorno de alunos(**C**) é dada por:

        $$
        C = \\frac{K \\times O}{N}
        $$

        O número de alunos que de fato retornam (**R**) depende da capacidade da rede de fornecer horários de aula dadas as restrições de professores, salas e turmas. Logo, **R** é o mínimo entre a quantidade de alunos que têm permissão para retornar **A** e a capacidade de retorno da rede **C**:

        $$
        R = \min{ ( A,C ) }
        $$

        E, finalmente, o número de professores que retornam é dado por **P**.

        ℹ️ *Note que **a capacidade total da rede pode ser maior que o número de alunos que se deseja retornar**. Isso ocorre pois, uma vez selecionada a etapa de ensino, alocamos todos as 40 horas de professores/salas das escolas que possuem essa etapa.*

        *Além disso, no modelo equitativo, no qual a rede oferece apenas uma aula por semana para cada aluno, esta pode atender muito mais alunos do que uma rede operando de maneira convencional.*
        """
        
        st.write(methodology_text)


if __name__ == "__main__":
    main()
