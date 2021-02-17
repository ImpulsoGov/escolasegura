import streamlit as st
import yaml
import utils
import os
import pandas as pd
from ipywidgets import AppLayout, GridspecLayout
import pages.snippet as tm
import pages.header as he
import pages.footer as foo
import amplitude



def main(session_state):
    utils.localCSS("localCSS.css")
    he.genHeader()

    protocol_icon = utils.load_image("imgs/plan_protocol_icon.png")
    verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
    verify_image = utils.load_image("imgs/prepare_verify_forms.png")
    notify_icon = utils.load_image("imgs/monitor_notify_icon.png")
    notify_image = utils.load_image("imgs/monitor_notify_forms.png")
    plan_icon = utils.load_image("imgs/monitor_plan_icon.png")
    plan_image = utils.load_image("imgs/monitor_plan_forms.png")
    
    subtitle = """Veja os principais passos para uma reabertura no quiz <span style="color:#ff9147;"><b>Passo a passo de reabertura Escola-Segura</b>.</span>
    <br><br>Nós estudamos bastante para essa prova! Revisamos a literatura científica, protocolos e melhores práticas encontradas em manuais de reabertura nacionais e internacionais, e resumimos os principais passos para você planejar um retorno escolar seguro para a sua comunidade!"""
    utils.main_title(title="Sua <b>rede</b> está preparada para retormada as atividades presenciais?", subtitle=subtitle)
    
    st.write(
        f"""
        <div class="conteudo" style="padding-top:50px;">
            <div class="flat-tabs-left flat-tabs-orange tabs-zoom-in">
                <input type="radio" id="tab-1" name="flat-tabs-left" class="section-one">
                <label for="tab-1"><i></i>Passo 1</label>
                <input type="radio" id="tab-2" name="flat-tabs-left" class="section-two">
                <label for="tab-2"><i></i>Passo 2</label>
                <input type="radio" id="tab-3" name="flat-tabs-left" class="section-three">
                <label for="tab-3"><i></i>Passo 3</label>
                <input type="radio" id="tab-4" name="flat-tabs-left" class="section-four">
                <label for="tab-4"><i></i>Passo 4</label>
                <input type="radio" id="tab-5" name="flat-tabs-left" class="section-five">
                <label for="tab-5"><i></i>Passo 5</label>
                <input type="radio" id="tab-6" name="flat-tabs-left" class="section-six">
                <label for="tab-6"><i></i>Passo 6</label>
                <input type="radio" id="tab-7" name="flat-tabs-left" class="section-seven">
                <label for="tab-7"><i></i>Passo 7</label>
                <input type="radio" id="tab-8" name="flat-tabs-left" class="section-eight">
                <label for="tab-8"><i></i>Passo 8</label>
                <input type="radio" id="tab-9" name="flat-tabs-left" class="section-nine">
                <label for="tab-9"><i></i>Passo 9</label>
                <input type="radio" id="tab-10" name="flat-tabs-left" class="section-ten">
                <label for="tab-10"><i></i>Passo 10</label>           
                <ul>
                    <li class="section-one">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">1. Diálogo
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-two">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">2. Determine as condições do retorno
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>                      
                    </li>
                    <li class="section-three">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">3. Protocolos sanitários
                                </div>
                                <div>
                                </div>
                                <div class="upper-padding">
                                    <div class="col card-plan container">
                                        <div class="left-margin">
                                            <div class="text-title-section main-orange-span minor-padding"> 
                                                <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
                                                Protocolos
                                            </div>
                                            <div class="minor-padding main-black-span">
                                                Quais são as principais <b>recomendações sanitárias</b> e protocolos para retomada?<br>
                                                <b>Listas de orientações para planejar a estrutura sanitária nas escolas.</b>
                                                A ferramenta fornece também rotinas a serem seguidas dentro e fora da sala de aula.<br><br>
                                                <b><i>Quem usa?</i></b>
                                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual
                                                <li> Diretores(as) de escolas.
                                            </div><br>
                                            <div class="button-position" style="padding-bottom: 10px;">
                                                <a href="https://drive.google.com/file/d/1NDdWRenKQ9EzVwBX6GbovSd3UICREhVg/view?usp=sharing" target="blank_">
                                                <button class="button-protocolos"; style="border-radius: .25rem;">acesse ></button><br>
                                                </a>
                                            </div>
                                        </div><br>
                                    </div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-four">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">4. Dimensione a rede
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-five">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">5. Decida o modelo de reabertura
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-six">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">6. Prepare o material pedagógico
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-seven">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">7. Dê atenção aos alunos
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-eight">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">8. Plano de contingência
                                </div>
                                <div>
                                </div>
                                <div class="upper-padding">
                                    <div class="col card-plan container">
                                        <div class="left-margin">
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                                <img class="icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
                                                Plano de contingência
                                            </div>
                                            <div>
                                                <br>
                                                <b><i>O que é?</b></i><br>É importante saber o que fazer se houver algum caso confirmado de Covid-19 em escolas 
                                                da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
                                                <br><br><b><i>Quem usa?</i></b>
                                                <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br></li>
                                            </div>
                                            <div class="minor-padding button-position">
                                                <a href="https://drive.google.com/file/d/1L6FXolCFTGQrfz_TT9zzxh1ojR5KfWEB/view" target="_blank">
                                                    <button class="button-contigenciaimprima"; style="border-radius: .25rem;"> imprima aqui > </button>
                                                </a>
                                            </div>
                                        </div><br>
                                    </div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-nine">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">9. Instrua seus colaboradores
                                </div>
                                <div>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-ten">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png">10. Acompanhe sua rede!
                                </div>
                                <div>
                                </div>
                                <div class="upper-padding row">
                                    <div class="col card-plan container">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                            <img class="icon" src="data:image/png;base64,{verify_icon}" alt="Fonte: Flaticon">
                                            Ferramenta de verificação
                                        </div><br>
                                        <div>
                                            <b><i>O que é?</b></i><br>
                                            Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
                                            <br><br>
                                            <b><i>Quem usa?</b></i>
                                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).</li>
                                            <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.</li>
                                        </div>
                                        <div class="minor-padding button-position">
                                            <a href="https://drive.google.com/file/d/1JJiVJorSxc-7gK-7uFgdqHLguBXKUzxb/view" target="_blank">
                                                <button class="button-verificacaoimprime"; style="border-radius: .25rem;">imprima aqui ></button>
                                            </a>
                                        </div>
                                        </div><br>
                                    </div>
                                    <div class="col card-plan container">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                            <img class="icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
                                            Ferramenta de notificação
                                        </div>
                                        <br>
                                        <b><i>O que é?</b></i><br>
                                        Ferramenta de comunicação das escolas com as Secretarias de Educação e Saúde sobre a existência de um caso ou suspeita na unidade.
                                        <br><br><b><i>Como usa?</b></i>
                                        <ol>
                                            <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual envia o formulário para as escolas de sua rede;</li>
                                            <li>No surgimento de um caso ou suspeita, diretores(as) utilizam o formulário para informar para a Secretaria de Educação e Saúde, e seguem o plano de ação indicado.</li>
                                        </ol>
                                        <div class="minor-padding button-position">
                                            <a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view" target="_blank">
                                                <button class="button-notificacaoimprime"; style="border-radius: .25rem;"> imprima aqui ></button>
                                            </a>
                                        </div>
                                        </div><br>
                                    </div>
                                </div>
                            </div>  
                        </div>
                    </li>
                </ul>
            </div>
        </div>""",
        unsafe_allow_html=True,
    )
    
    # utils.gen_title(title="<b>1</b>. Diálogo", subtitle="")
    
    # utils.gen_title(title="<b>2</b>. Determine as condições do retorno", subtitle="")

    # utils.gen_title(title="<b>3</b>. Protocolos sanitários", subtitle="")
    
    # st.write(
    #     f"""
    #     <div class="conteudo upper-padding">
    #         <div class="col card-plan container">
    #             <div class="left-margin">
    #                 <div class="text-title-section main-orange-span minor-padding"> 
    #                     <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
    #                     Protocolos
    #                 </div>
    #                 <div class="minor-padding main-black-span">
    #                     Quais são as principais <b>recomendações sanitárias</b> e protocolos para retomada?<br>
    #                     <b>Listas de orientações para planejar a estrutura sanitária nas escolas.</b>
    #                     A ferramenta fornece também rotinas a serem seguidas dentro e fora da sala de aula.<br><br>
    #                     <b><i>Quem usa?</i></b>
    #                     <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual
    #                     <li> Diretores(as) de escolas.
    #                 </div><br>
    #                 <div class="button-position" style="padding-bottom: 10px;">
    #                     <a href="https://drive.google.com/file/d/1NDdWRenKQ9EzVwBX6GbovSd3UICREhVg/view?usp=sharing" target="blank_">
    #                     <button class="button-protocolos"; style="border-radius: .25rem;">acesse ></button><br>
    #                     </a>
    #                 </div>
    #             </div><br>
    #         </div>
    #     </div>""",
    #     unsafe_allow_html=True,
    # )
    # utils.gen_title(title="4. Dimensione a rede", subtitle="")

    # utils.gen_title(title="5. Decida o modelo de reabertura", subtitle="")

    # utils.gen_title(title="6. Prepare o material pedagógico", subtitle="")

    # utils.gen_title(title="7. Dê atenção aos alunos", subtitle="")

    # utils.gen_title(title="8. Plano de contingência", subtitle="")

    # st.write(
    #     f"""
    #     <div class="conteudo upper-padding">
    #         <div class="col card-plan container">
    #             <div class="left-margin">
    #              <div class="text-title-section minor-padding main-orange-span"> 
    #                     <img class="icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
    #                     Plano de contingência
    #                 </div>
    #                 <div>
    #                     <br>
    #                     <b><i>O que é?</b></i><br>É importante saber o que fazer se houver algum caso confirmado de Covid-19 em escolas 
    #                     da sua rede. Veja uma ferramenta de reporte do caso para sua escola e monitoramento da rede.
    #                     <br><br><b><i>Quem usa?</i></b>
    #                     <li> Gestor(a) da Secretaria de Educação Municipal ou Estadual.<br></li>
    #                 </div>
    #                 <div class="minor-padding button-position">
    #                     <a href="https://drive.google.com/file/d/1L6FXolCFTGQrfz_TT9zzxh1ojR5KfWEB/view" target="_blank">
    #                         <button class="button-contigenciaimprima"; style="border-radius: .25rem;"> imprima aqui > </button>
    #                     </a>
    #                 </div>
    #             </div><br>
    #         </div>
    #     </div>""",
    #     unsafe_allow_html=True,
    # )

    # utils.gen_title(title="9. Instrua seus colaboradores", subtitle="")

    # utils.gen_title(title="10. Acompanhe sua rede!", subtitle="")
    # st.write(
    #     f"""
    #     <div class="conteudo upper-padding row">
    #         <div class="col card-plan container">
    #             <div>
    #              <div class="text-title-section minor-padding main-orange-span"> 
    #                 <img class="icon" src="data:image/png;base64,{verify_icon}" alt="Fonte: Flaticon">
    #                 Ferramenta de verificação
    #             </div><br>
    #             <div>
    #                 <b><i>O que é?</b></i><br>
    #                 Formulário para conferir a adequação das unidades escolares aos protocolos estabelecidos e indicar orientações.
    #                 <br><br>
    #                 <b><i>Quem usa?</b></i>
    #                 <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual: obtém o formulário e envia para diretores(as).</li>
    #                 <li>Diretores(as) escolares: preenchem o formulário para verificação da Secretaria.</li>
    #             </div>
    #             <div class="minor-padding button-position">
    #                 <a href="https://drive.google.com/file/d/1JJiVJorSxc-7gK-7uFgdqHLguBXKUzxb/view" target="_blank">
    #                     <button class="button-verificacaoimprime"; style="border-radius: .25rem;">imprima aqui ></button>
    #                 </a>
    #             </div>
    #             </div><br>
    #         </div>
    #         <div class="col card-plan container">
    #             <div>
    #              <div class="text-title-section minor-padding main-orange-span"> 
    #                 <img class="icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
    #                 Ferramenta de notificação
    #             </div>
    #             <br>
    #             <b><i>O que é?</b></i><br>
    #             Ferramenta de comunicação das escolas com as Secretarias de Educação e Saúde sobre a existência de um caso ou suspeita na unidade.
    #             <br><br><b><i>Como usa?</b></i>
    #             <ol>
    #                 <li>Gestor(a) da Secretaria de Educação Municipal ou Estadual envia o formulário para as escolas de sua rede;</li>
    #                 <li>No surgimento de um caso ou suspeita, diretores(as) utilizam o formulário para informar para a Secretaria de Educação e Saúde, e seguem o plano de ação indicado.</li>
    #             </ol>
    #             <div class="minor-padding button-position">
    #                 <a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view" target="_blank">
    #                     <button class="button-notificacaoimprime"; style="border-radius: .25rem;"> imprima aqui ></button>
    #                 </a>
    #             </div>
    #             </div><br>
    #         </div>
    #     </div>""",
    #     unsafe_allow_html=True,
    # )
    tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()
