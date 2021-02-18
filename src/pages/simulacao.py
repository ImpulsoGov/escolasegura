import streamlit as st
import session
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout
import utils
import amplitude
from model.get_school_return_data import entrypoint
from utils import load_markdown_content
import pages.snippet as tm
import pages.header as he
import pages.footer as foo

@st.cache(suppress_st_warning=True)
def get_data(session_state):
    """ 
    This function return a dataframe with all data

    Parameters: 
        config (type): doc config.yaml

    Returns:
        df (type): 2019 school census dataframe
    """
    url = "http://datasource.coronacidades.org/br/cities/safeschools/main?state_id="+session_state.state_id
    df = pd.read_csv(url)
    return df


def genSelectBox(df, session_state):
    """ 
    This function generates select boxes for choosing the school network

    Parameters: 
        df (type): 2019 school census dataframe
        session_state (type): section dataset
        user_analytics (type): user data by amplitude
    """

    st.write(
        f"""
        <div class="main-padding" id="top">
            <div class="subtitle-section"> Selecione sua rede </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3, col4 = st.beta_columns([0.3, 0.5, 0.5, 1])

    with col1:
        session_state.state_id = st.selectbox("Estado", utils.filter_place(df, "state"))
        session_state.state_name = utils.set_state_name(df,session_state.state_id)
    with col2:
        options_city_name = utils.filter_place(
            df, "city", state_id=session_state.state_id
        )
        options_city_name = pd.DataFrame(data=options_city_name, columns=["city_name"])
        x = int(
            options_city_name[options_city_name["city_name"] == "Todos"].index.tolist()[
                0
            ]
        )
        session_state.city_name = st.selectbox("Município", options_city_name, index=x)
        import pathlib
        from bs4 import BeautifulSoup
        GA_JS = (
            """
        window.dataLayer = window.dataLayer || [];
        function municipio(){dataLayer.push('municipio_value': '%s');}
        """
            % session_state.city_name
        )
        index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
        soup = BeautifulSoup(index_path.read_text())
        script_tag_loader = soup.new_tag("script")
        script_tag_loader.string = GA_JS
    with col3:
        options_adiminlevel = utils.filter_place(
            df,
            "administrative_level",
            state_id=session_state.state_id,
            city_name=session_state.city_name,
        )
        options_adiminlevel = pd.DataFrame(
            data=options_adiminlevel, columns=["adiminlevel"]
        )
        y = int(
            options_adiminlevel[
                options_adiminlevel["adiminlevel"] == "Todos"
            ].index.tolist()[0]
        )
        session_state.administrative_level = st.selectbox(
            "Nível de Administração", options_adiminlevel, index=y
        )
    with col4:
        st.write(
            f"""
        <div class="container main-padding">
            <br><br>
        </div>
        """,
            unsafe_allow_html=True,
        )



def genSimulationResult(params, config):
    """ 
    This is a function that returns the simulation result

    Parameters: 
        params (type): parameters for simulation
        config (type): doc config.yaml
              
    """

    result = entrypoint(params, config)

    teacher_icon = utils.load_image("imgs/simulation_teacher_icon.png")
    student_icon = utils.load_image("imgs/student_icons.png")
    mask_icon = utils.load_image("imgs/simulation_mask_icon.png")
    sanitizer_icon = utils.load_image("imgs/simulation_sanitizer_icon.png")
    thermometer_icon = utils.load_image("imgs/simulation_thermometer_icon.png")

    st.write(
        f"""
        <div class="container main-padding light-green-simulator-bg">
            <div class="text-title-section minor-padding main-orange-span"><b>RESULTADO DA SIMULAÇÃO</b></div>
            <div class="row">
                <div class="col minor-padding">
                    <p>Você pode no modelo {params["education_model"]}:</p>
                    <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                        <div class="div2 card-number" style="color:#FF934A; width: 30%; margin-right: 20px;"> {result["num_returning_students"]} </div>
                        <div class="div2" style="width: 50%; padding-left: 10px;"><b>estudantes,</b> <br>{params["hours_per_day"]} horas por dia</div>
                    </div>
                    <div class="grid-container-simulation-material minor-padding" style="padding: 10px; display: flex; flex-flow: row wrap;">
                        <div class="div2 card-number" style="color:#2B14FF; width: 30%; margin-right: 20px;"> {result["num_returning_teachers"]} </div>
                        <div class="div2" style="width: 50%; padding-left: 10px;"><b>professores,</b> <br>{params["hours_per_day"]} horas por dia</div>
                    </div>
                    <div class="card-simulator-bottom light-green-simulator-bg">
                        <img class="icon-cards" style="width: 70%; align-content: center; height: auto;" src="data:image/png;base64,{student_icon}" alt="Fonte: Flaticon">
                        <div class="grid-container-simulation-type" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2" style="width: 20%;"> <img class="icon-cards" src="data:image/png;base64,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" alt="Fonte: Flaticon"> </div>
                            <div class="div2" style="width: 50%;">Cada turma possui somente 1 professor(a)</div>
                        </div>
                    </div>
                </div>
                <div class="col minor-padding">
                    <div class="card-simulator-bottom light-green-simulator-bg minor-padding">
                        <p>Considerando <b>protocolos sanitários</b> para o retorno, serão necessários semanalmente:</p>
                        <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 35%; margin-right: 20px;"> {result["total_thermometers"]} </div>
                            <div class="div2" style="width: 50%; padding-left: 10px;"><b>termômetros</b> (1/100 estudantes)</div>
                        </div>
                        <div class="grid-container-simulation-material minor-padding" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 35%; margin-right: 20px;"> {result["total_masks"]} </div>
                            <div class="div2" style="width: 50%; padding-left: 10px;"><b>máscaras  por semana</b> (1/pessoa cada 3 horas)</div>
                        </div>
                        <div class="grid-container-simulation-material" style="padding: 10px; display: flex; flex-flow: row wrap;">
                            <div class="div2 card-number" style="width: 35%; margin-right: 20px;"> {result["total_sanitizer"]} </div>
                            <div class="div2" style="width: 50%; padding-left: 10px;"><b>litros de álcool em gel</b> (12ml/pessoa por dia)</div>
                        </div>
                        <div class="container">
                            <div class="button-position" style="padding-bottom: 10px;">
                                <a href="https://docs.google.com/spreadsheets/d/15ib2NCdwPbLllofuqf9epKCAQK_hvY1Q8rdp6hHko_U/edit?ts=5f889510#gid=0" target="blank_">
                                <button class="button-protocolos"; style="border-radius: .25rem; font-size:16px;">veja a lista completa ></button><br>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
            <div class="row main-padding">
                <div class="col minor-padding">
                    <div class="minor-padding" style="font-size: 18px; color:#FF934A; font-weight: bold;">VOCÊ CHEGOU AO FINAL DA SIMULACÃO, AGORA CLIQUE ABAIXO E VEJA OUTRAS FERRAMENTAS DISPONIVEÍS.</div>
                    <div class="button-position minor-padding" style="padding-bottom: 10px;">
                        <a href="#top">
                        <button class="button-protocolos"; style="border-radius: .25rem; font-size:16px;">explorar ferramentas ></button><br>
                        </a>
                    </div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )


def main():
    utils.localCSS("localCSS.css")
    session_state = session.SessionState.get(
        key=session.get_user_id(),
        update=False,
        state_name="Acre",
        state_id="AC",
        city_name="Todos",
        administrative_level="Todos",
        refresh=False,
        reset=False,
        already_generated_user_id=None,
        pages_open=None,
        amplitude_events=None,
        button_styles=dict(),
        continuation_selection=None,
        button_simule=0,
        section1_organize=False,
        section2_manage=False,
    )
    he.genHeader("simulation")
    config = yaml.load(open("config/config.yaml", "r"), Loader=yaml.FullLoader)
    df = get_data(session_state)
    data = df[(df["city_name"] == session_state.city_name)& (df["administrative_level"] == session_state.administrative_level)]
    subtitle = """O retorno às atividades presenciais deve ser pensado em etapas para definir não só quem pode retornar, mas também como. Trazemos abaixo um passo a passo para construir a simulação da sua rede - experimente!"""
    utils.main_title(title="<b>Simulador</b>: como organizar a rebertura?", subtitle="")
    utils.gen_title(title="<b>1</b>. Escolha quem pode retornar", subtitle="")
    # params = dict()
    # params["number_students"] = st.number_input(
    #     "Quantos estudantes retornam às aulas presenciais?",
    #     format="%d",
    #     value=data["number_students"].values[0],
    #     step=1,
    # )
    # params["number_teachers"] = st.number_input(
    #     "Quantos professores(as) retornam?",
    #     format="%d",
    #     value=data["number_teachers"].values[0],
    #     step=1,
    # )
    utils.gen_title(title="<b>2</b>. Informe sobre suas salas", subtitle="")
    utils.gen_title(title="<b>3</b>. Organize suas turmas", subtitle="")
    tm.genGuia()
    foo.genFooter()
    # genSelectBox(df, session_state)

    # params = dict()
    # main_icon = utils.load_image("imgs/simulation_main_icon.png")
    # st.write(
    #         f"""
    #         <div class="text-title-section minor-padding">
    #              Quantos <span class="bold main-orange-span">estudantes e professores(as)</span> retornam às salas de aula em diferentes modelos?
    #         </div>
    #         <div class="container main-padding" style="padding-left:0px;">
    #             <div class="container minor-padding main-orange-span" style="font-size: 20px; color:#FF934A; font-weight: bold;"> 
    #                 <img class="minor-icon" src="data:image/png;base64,{main_icon}" alt="Fonte: Flaticon">
    #                 Simule o retorno
    #             </div>
    #             <div class="minor-padding">
    #                 O retorno às atividades presenciais deve ser pensado em etapas para definir não só <b>quem pode retornar</b>, mas também <b>como</b>. Trazemos abaixo um passo a passo para construir a simulação da sua rede - experimente!
    #             </div>
    #              <div class="minor-padding" style="font-size: 20px; color:#FF934A; font-weight: bold;">
    #                 <br>Para qual etapa de ensino você está planejando?
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # # TODO: colocar por estado somente também
    # # if city_name:
    # data = df[
    #     (df["city_name"] == session_state.city_name)
    #     & (df["administrative_level"] == session_state.administrative_level)
    # ]
    # col1, col2 = st.beta_columns([0.9, 0.2])
    # with col1:
    #     education_phase = st.selectbox(
    #         "", data["education_phase"].sort_values().unique()
    #     )
    #     data = data[data["education_phase"] == education_phase]
    # with col2:
    #     st.write(
    #         f"""<div class="container">
    #             <br>
    #             </div>
    #             <br>
    #         """,
    #         unsafe_allow_html=True,
    #     )

    # st.write(
    #     f"""<br>
    #         <div class="container" style="padding-left:0px;">
    #             <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>1. Escolha o modelo de retorno às atividades</b></div>
    #             <div class="minor-padding">
    #                 Existem diversos modelos possíveis de retorno avaliadas de acordo com as etapas de aprendizado. Separamos abaixo 5 opções possíveis indicadas pela UNESCO.
    #             </div>
    #         </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # UNESCO_models = {
    #     'Totalmente Presencial': {
    #         "description": """Neste modelo, todos os estudantes <b>retornam às aulas
    #         presenciais padrão</b>, isto é, os mesmos horários em sala de
    #         aula, porém seguindo os novos protocolos de distanciamento e segurança
    #         sanitária.
    #         <br><br><b>Por que este modelo?</b><br>
    #         Modelo tradicional, onde os estudantes e docentes estão habituados."""
    #         ,
    #         "hours_per_day": 5,
    #         "priority": False
    #     }
    #     , 
    #     'Aulas presenciais + Tarefas remota': {
    #         "description": """Neste modelo professores(as) <b>transmitem
    #         conceitos para os estudantes presencialmente</b>, e, em seguida,
    #         <b>estudantes completam exercícios e tarefas em casa</b>.
    #         <br><br><b>Por que este modelo?</b><br>
    #         Alunos e professores mantêm um contato próximo, e estudantes podem tirar dúvidas durante a exposição da matéria."""
    #         ,
    #         "hours_per_day": 3,
    #         "priority": False
    #     }
    #     , 
    #     'Aulas por vídeo + Tarefas presenciais': {
    #         "description": """Neste modelo estudantes <b>aprendem
    #         novos conceitos de forma remota</b> e, em seguida, <b>concluem exercícios e 
    #         tarefas presencialmente</b> com o(a) professor(a).
    #         <br><br><b>Por que este modelo?</b><br>
    #         Alunos e professores mantêm o convívio, e os estudantes podem tirar dúvidas 
    #         urante a realização dos exercícios e se beneficiarem com as dúvidas dos colegas."""
    #         ,
    #         "hours_per_day": 2,
    #         "priority": False
    #     }
    #     , 
    #     'Grupo prioritário presencial': {
    #         "description": """Neste modelo, os professores têm uma <b>aula normal completa com um grupo
    #         de estudantes presencial, enquanto outro grupo acompanha remotamente 
    #         por meio de videoconferência (VC)</b>.
    #         <br><br><b>Por que este modelo?</b>
    #         Turma mantém o convívio, mesmo que virtual, e os professores atentem todos da turma no mesmo momento."""
    #         ,
    #         "hours_per_day": 5,
    #         "priority": True
    #     }
    # }

    # col1_1, col1_2, col1_3, col1_4 = st.beta_columns([0.35, 0.05, 0.85, 0.3])
    # with col1_1:
    #     params["education_model"] = st.selectbox(
    #         "", list(UNESCO_models.keys())
    #     )
    #     params["priority"] = UNESCO_models[params["education_model"]]["priority"]
    # with col1_2:
    #     st.write(
    #         f"""
    #         <div class="container main-padding">
    #             <br>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # with col1_3:
    # # Sobre o modelo
    #     st.write(
    #             f"""
    #             <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
    #                 <div style="font-family: 'Roboto Condensed', sans-serif; padding:10px; margin-bottom:0px; margin-top: 16px;margin-left: 16px; margin-right: 16px;">
    #                     <b>{params["education_model"]}</b>
    #                     <br><br>{UNESCO_models[params["education_model"]]["description"]}
    #                     <br><br><b><a href="https://en.unesco.org/sites/default/files/unesco-covid-19-response-toolkit-hybrid-learning.pdf">FONTE: UNESCO</a></b>
    #                 </div>
    #                 <div class="button-position" style="margin-bottom: 0px;padding: 10px;margin-top: 16px;margin-right: 16px;margin-left: 16px;">
    #                     <a href="#entenda-modelo">
    #                         <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
    #                             leia sobre todos os modelos >
    #                         </button>
    #                     </a>
    #                 </div>
    #                 <div class="button-position" style="margin-bottom: 0px;padding: 10px;margin-top: 16px;margin-right: 16px;margin-left: 16px;">
    #                     <a href="#entenda-etapa">
    #                         <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
    #                             veja considerações por etapa de ensino >
    #                         </button>
    #                     </a>
    #                 </div>
    #             </div>
    #             <div id="entenda-modelo" class="info-modal-window" style="width: 80%; height: 70%;">
    #                 <div>
    #                     <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
    #                     <h1 class="main-orange-span bold" style="padding: 0px 50px 0px 50px;">Modelos</h1>
    #                     <div style="font-size: 16px; padding: 0px 50px 0px 50px;">
    #                         Abaixo há o quadro completo. Caso não consiga ver a imagem, clique na imagem para baixa-la ou <a href="https://drive.google.com/u/1/uc?id=1tqBItM8XkLdY9u2wk0ZcPrVcHccgdp1f&export=download">[AQUI]</a>.
    #                     </div>
    #                     <a href="https://drive.google.com/u/1/uc?id=1tqBItM8XkLdY9u2wk0ZcPrVcHccgdp1f&export=download"><img style="padding: 50px 50px 50px 50px;" class="images" src="https://i.imgur.com/ZByy47a.jpg"></a>
    #                 </div>
    #             </div>
    #             <div id="entenda-etapa" class="info-modal-window" style="width: 80%; height: 70%;">
    #                 <div>
    #                     <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
    #                     <h1 class="main-orange-span bold" style="padding: 0px 50px 0px 50px;">Etapas de Ensino</h1>
    #                     <div style="font-size: 16px; padding: 0px 50px 0px 50px;">
    #                         <br>
    #                         <b>4 - 8 anos</b><br>
    #                         Pontos principais para consideração:<br>
    #                         <li>Crianças desta faixa etária possuem menor risco de apresentar sintomas graves.</li>                            
    #                         <li>Pais e responsáveis necessitam de creches e suporte para manter demais atividades do dia a dia</li>
    #                         <li>Eficácia muito baixa do ensino remoto</li><br>
    #                         <b>8 - 12 anos</b><br>
    #                         Pontos principais para consideração:<br>
    #                         <li>Crianças desta faixa etária possuem menor risco de apresentar sintomas graves, mas há maior dificuldade em adotar medidas sanitárias.</li>
    #                         <li>Já possuem maior autonomia no cotidiano e pode</li><br>
    #                         <b>12 - 17 anos</b><br>
    #                         Pontos principais para consideração:<br>
    #                         <li>Crianças desta faixa etária possuem maior risco intrínseco de contrair e desenvolver sintomas, mas apresentam maior aderência aos protocolos sanitários</li>
    #                         <li>Logística de agendamento presencial pode ser mais complexa, pois os anos possuem matérias e professores diversos.</li><br>
    #                         <b>17 - 18 anos</b><br>
    #                         Pontos principais para consideração:<br>
    #                         <li>Crianças desta faixa etária possuem maior risco intrínseco de contrair e desenvolver sintomas, mas apresentam maior aderência aos protocolos sanitários.</li>
    #                         <li>Alta eficácia e adesão ao método remoto</li>
    #                         <br>Abaixo há o quadro completo. Caso não consiga ver a imagem, clique na imagem para baixa-la ou <a href="https://drive.google.com/u/1/uc?id=1Sj65MXPkRcw6VxojYBLsJ8otIuvpLfq_&export=download">[AQUI]</a>.
    #                     </div>
    #                     <a href="https://drive.google.com/u/1/uc?id=1Sj65MXPkRcw6VxojYBLsJ8otIuvpLfq_&export=download"><img style="padding: 50px 50px 50px 50px;" class="images" src="https://i.imgur.com/FyoIFe9.jpg"></a>
    #                 </div>
    #             </div>
    #             """,
    #             unsafe_allow_html=True,
    #     )
    # with col1_4:
    #     st.write(
    #         f"""<div class="container">
    #             <br>
    #             </div>
    #             <br>
    #         """,
    #         unsafe_allow_html=True,
    #     )


    # st.write(
    #     f"""<br>
    #         <div class="container" style="padding-left:0px;">
    #             <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>2. Escolha quem pode retornar</b></div>
    #         </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # col2a_1, col2a_2, col2a_3, col2a_4 = st.beta_columns([0.35, 0.05, 0.85, 0.3])
    # with col2a_1:
    #     params["number_students"] = st.number_input(
    #         "Quantos estudantes retornam às aulas presenciais?",
    #         format="%d",
    #         value=data["number_students"].values[0],
    #         step=1,
    #     )
    #     if params["priority"]:
    #         params["number_remote_students"] = st.number_input(
    #         "Quantos estudantes acompanham às aulas somente de forma remota?",
    #         format="%d",
    #         value=data["number_students"].values[0],
    #         step=1,
    #     )
    # with col2a_2:
    #     st.write(
    #         f"""
    #         <div class="container main-padding">
    #             <br>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # with col2a_3:
    #     st.write(
    #         f"""
    #         <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
    #             <div class="row" style="font-family: 'Roboto Condensed', sans-serif; margin-bottom:0px; padding:10px;">
    #                 <b>Iniciamos com total de estudantes reportados no Censo Escolar 2019 (INEP).</b>
    #                 <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de estudantes podem ser vulneráveis ou ter prioridade.
    #             </div>
    #             <div class="button-position" style="padding-bottom: 15px;">
    #                 <a href="#entenda-estudantes">
    #                     <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
    #                         grupos que requerem atencão especial >
    #                     </button>
    #                 </a>
    #             </div>
    #         </div>
    #         <div id="entenda-estudantes" class="info-modal-window" style="width: 80%; height: 70%;">
    #             <div>
    #                 <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
    #                 <h1 class="main-orange-span bold" style="padding: 0px 50px 0px 50px;">Estudantes</h1>
    #                 <div style="font-size: 20px; padding: 0px 50px 0px 50px;">
    #                     <b>Grupos que requerem atencão especial</b>
    #                 </div>
    #                 <br>
    #                 <div style="font-size: 16px; padding: 0px 50px 0px 50px;">
    #                     <b>Exemplos de grupos vulneráveis ou/e marginalizados</b>
    #                     <li>Minorias</li>
    #                     <li>Meninas adolescentes</li>
    #                     <li>Crianças com deficiência de aprendizagem</li>
    #                     <li>Crianças que vivem em instituições de abrigo</li>
    #                     <li>Crianças vivendo em condição de pobreza, em residências com alta ocupância ou improvisadas</li>
    #                     <li>Orfãos</li>
    #                     <li>Crianças separadas de seus responsáveis</li>
    #                     <li>Crianças e adolescentes em risco de abandono escolar</li>
    #                 </div>
    #             </div>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # with col2a_4:
    #     st.write(
    #         f"""<div class="container">
    #             <br>
    #             </div>
    #             <br>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # st.write(
    #     f"""
    #     <div class="container main-padding">
    #         <br>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # col2b_1, col2b_2, col2b_3, col2b_4 = st.beta_columns([0.35, 0.05, 0.85, 0.3])
    # with col2b_1:
    #     params["number_teachers"] = st.number_input(
    #         "Quantos professores(as) retornam?",
    #         format="%d",
    #         value=data["number_teachers"].values[0],
    #         step=1,
    #     )
    # col2b_2=col2a_2
    # with col2b_3:
    #     st.write(
    #         f"""
    #         <div class="col light-green-simulator-bg card-simulator" style="border-radius:30px;">
    #             <div class="row" style="font-family: 'Roboto Condensed', sans-serif; margin-bottom:0px; padding:10px;">
    #                 <b>Iniciamos com total de professores reportados no Censo Escolar 2019 (INEP).</b> 
    #                 <br>Você pode alterar esse valor ao lado. Leve em consideração quais grupos de professores podem ser de risco, confortáveis para retorno e outros.
    #             </div>
    #             <div class="button-position" style="padding-bottom: 15px;">
    #                 <a href="#entenda-professores">
    #                     <button class="button-protocolos" style="border-radius: .25rem; font-size:16px; margin-right: 10px;margin-left: 10px;">
    #                         como retornar professores(as) >
    #                     </button>
    #                 </a>
    #             </div>
    #             <div id="entenda-professores" class="info-modal-window" style="width: 80%; height: 70%;">
    #                 <div>
    #                     <a href="#" title="Close" class="info-btn-close" style="color: white;">&times</a>
    #                     <h1 class="main-orange-span bold" style="padding: 0px 50px 0px 50px;">Professores</h1>
    #                     <div style="font-size: 16px; padding: 0px 50px 0px 50px;">
    #                         <b>Fatores a serem considerados:</b> grupos vulneráveis, número de casos suspeitos, desconforto da rede com o retorno presencial, dificuldade logística e a disponibilidade de retorno presencial.
    #                         <br><br>O quadro explicativo traz para cada fator um desafio e uma ação sugerida.
    #                         <br><br>Caso não consiga ver a imagem, clique na imagem para baixa-la ou <a href="https://drive.google.com/u/1/uc?id=1lLtbEMau4nIj8tZ5rQF51ThV2Q8K1DzE&export=download">[AQUI]</a>.
    #                     </div>
    #                     <a href="https://drive.google.com/u/1/uc?id=1lLtbEMau4nIj8tZ5rQF51ThV2Q8K1DzE&export=download"><img style="padding: 50px 50px 50px 50px;" class="images" src="https://i.imgur.com/4ai7xDK.jpg"></a>
    #                 </div>
    #             </div>
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # col2b_4=col2a_4
    # st.write(
    #     f"""
    #     <br>
    #     <div class="container" style="padding-left:0px;">
    #         <div class="minor-padding" style="font-size: 20px; color:#FF934A;"><b>3. Defina as restrições de retorno</b></div><br>
    #             </div>
    #         </div>
    #     </div>
    #     """,
    #     unsafe_allow_html=True,
    # )

    # col3_1, col3_2, col3_3, col3_4, col3_5, col3_6 = st.beta_columns(
    #     [0.35, 0.05, 0.4, 0.05, 0.4, 0.3]
    # )
    # with col3_1:
    #     params["number_classrooms"] = st.number_input(
    #         "Quantas salas de aula disponíveis?",
    #         format="%d",
    #         value=data["number_classroms"].values[0],
    #         step=1,
    #     )
    #     st.write(
    #         f"""
    #         <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
    #             O número de salas restringe o número de turmas que podem voltar de forma simultânea.
    #         </div>
    #     """,
    #         unsafe_allow_html=True,
    #     )
    # col3_2=col2a_2
    # with col3_3:
    #     params["max_students_per_class"] = st.slider(
    #         "Selecione o máximo de estudantes por turma:", 0, 20, 20, 1
    #     )
    #     st.write(
    #         f"""
    #         <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
    #             Limitamos em 20 estudantes por sala para diminiuir o risco de transmissão seguindo critérios sanitários.
    #         </div>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # col3_4 = col2a_2
    # with col3_5:
    #     params["hours_per_day"] = int(st.slider(
    #         "Selecione o número de horas presenciais diárias na escola por turma:", 
    #         min_value=1, 
    #         max_value=5, 
    #         value=UNESCO_models[params["education_model"]]["hours_per_day"], 
    #         step=1,
    #     ))

    #     st.write(
    #         f"""
    #         <div class="row" style="margin:0px; padding:10px; background:#DDFBF0; border-radius: 1rem 1rem 1rem 1rem;">
    #             As restrições sanitárias limitam a quantidade de tempo e estudantes que conseguem retornar à sala de aula.
    #         </div>

    #         <div class="container">
    #         <br>
    #         </div>
    #         <br>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    # col3_6=col2a_4




    # params["total_hour_class"] = st.number_input(
    #     "Horas diárias de aula disponíveis por sala",
    #     format="%d",
    #     value=8,
    #     step=1,
    # )
    # params["turnos"] = st.number_input(
    #     "Número de turnos",
    #     format="%d",
    #     value=3,
    #     step=1,
    # )
    # x = int(params["total_hour_class"]/params["turnos"])
    # params["hour_class"] = int(st.slider(
    #     "Horas diárias de aula por turma", 
    #     min_value=1, 
    #     max_value=x, 
    #     step=1,
    # ))

    # with st.beta_expander("simular retorno"):
    #     user_analytics = amplitude.gen_user(utils.get_server_session())
    #     opening_response = user_analytics.safe_log_event(
    #         "clicked simule retorno", session_state, is_new_page=True
    #     )
    #     print(params)
    #     genSimulationResult(params, config)


if __name__ == "__main__":
    main()
