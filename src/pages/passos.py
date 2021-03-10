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



def main():
    utils.localCSS("localCSS.css")
    he.genHeader("guia10passos")
    # urlpath = "http://localhost:8501/"
    urlpath = 'https://escolasegura-staging.herokuapp.com/'
    # urlpath = 'https://escolasegura.coronacidades.org/'

    protocol_icon = utils.load_image("imgs/plan_protocol_icon.png")
    verify_icon = utils.load_image("imgs/prepare_verify_icon.png")
    verify_image = utils.load_image("imgs/prepare_verify_forms.png")
    notify_icon = utils.load_image("imgs/monitor_notify_icon.png")
    notify_image = utils.load_image("imgs/monitor_notify_forms.png")
    plan_icon = utils.load_image("imgs/monitor_plan_icon.png")
    plan_image = utils.load_image("imgs/monitor_plan_forms.png")

    st.write(
        f"""
        <div class="conteudo title-section" style="padding-bottom:20px;"> 
            <img class="square" src="https://i.imgur.com/gGIFS5N.png">
            Como sua rede pode se preparar para a retomada das atividades presenciais? Temos 10 passos para auxiliar no processo.
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            Revisamos a literatura científica, protocolos e melhores práticas encontradas no Brasil e no mundo para criar 10 passos para você, gestor da educação, preparar e gerir a retomada das atividades presenciais nas escolas, diante dos desafios impostos pela Covid-19. 
            <br><br>
            Aqui, você encontra orientações que começam desde o planejamento da reabertura, com a definição dos protocolos sanitários e regras que devem ser adotados pelas escolas antes de reabrir, até a gestão da rede após a retomada, com recomendações sobre o que fazer diante de algum caso confirmado de Covid-19 dentro da unidade escolar. 
            <br><br>
            Ao longo desse processo de retomada, você pode definir prioridades de acordo com a sua realidade local, mas lembre-se de seguir todas as recomendações presentes nos 10 passos para estruturar uma reabertura mais segura para toda a comunidade escolar.
            <br><br>
            Acesse <a href="https://drive.google.com/file/d/1HqWKjM8uD4HM64fbFcbjS-pPD3SzWcmt/view?usp=sharing" target="blank_" style="text-decoration: none;">aqui</a> os 10 Passos em forma de lista.
        </div>
        <div class="conteudo title-section" style="padding-bottom:20px;"> 
            <img class="square" src="https://i.imgur.com/gGIFS5N.png">
            Passos:
        </div>
        """,
        unsafe_allow_html=True,
    )

    obj1 = "Definir os atores responsáveis por planejar, preparar e monitorar a rede para a retomada de atividades presenciais e estabelecer um canal de comunicação com a comunidade escolar."
    term1 = "Ter clareza sobre os papéis e responsabilidades de cada órgão dentro do processo de retomada, com um comitê estruturado para tomar decisões com agilidade, com discursos e comunicação alinhados. "
    prat1 = """Ação 1. Forme uma Comissão de Reabertura com os atores-chave presentes nos diversos órgãos que devem ser engajados nessa retomada. Além da Secretaria de Educação, a comissão pode envolver membros da Secretaria de Saúde, Secretaria de Assistência/Desenvolvimento Social e também lideranças regionais, caso sua rede conte com essa estrutura. 
<br><br>
Ação 2. Crie um canal para comunicação constante da comissão com a comunidade, em especial com diretores, funcionários de escola, professores, pais e responsáveis. Prepare uma pessoa para ser porta-voz e ponto de referência de todo o processo de retomada para a comunidade escolar e para a imprensa. 
<br><br>
Ação 3. Estabeleça um plano de comunicação, definindo o que, quando, como e com qual frequência a estratégia de reabertura das atividades presenciais será comunicada."""
    obj2 = "Definir os critérios e condições sanitárias que serão considerados para o retorno das atividades presenciais nas escolas, uma vez que o cenário da Covid-19 é variável."
    term2 = "Projetar uma data de retomada das atividades presenciais, de acordo com os critérios definidos."
    prat2 = """Ação 1. Pactue com a Secretaria de Saúde sobre quais condições sanitárias, critérios e dados da Covid-19 devem ser considerados na hora de decidir sobre o retorno seguro de atividades escolares presenciais na sua rede.
<br><br>
Ação 2.  Com base nos critérios pactuados com a Secretaria de Saúde, defina a data de retomada, mesmo que parcial, das atividades presenciais e comece a preparação para o retorno. 
<br><br>
Ação 3. Articule com atores-chave externos, como sindicato de professores, líderes comunitários locais e outros atores relevantes, sobre os critérios pactuados e a data pensada para a  retomada."""
    obj3 = "Estabelecer o protocolo sanitário a ser seguido por todas as escolas da rede que retomarem as atividades presenciais, com orientações sobre adaptação de estrutura física e a necessidade de aquisição de materiais de limpeza e EPIs para prevenir o contágio da Covid-19 dentro das unidades de ensino."
    term3 = "Adequar suas unidades de ensino ao protocolo estabelecido e comunicar as medidas de prevenção adotadas a toda a comunidade escolar. "
    prat3 = """Ação 1. Prepare, com o apoio da Secretaria de Saúde, um protocolo sanitário a ser seguido por todas as escolas que retomarem as atividades presenciais, com a definição da lista de materiais necessários para sua implementação. 
<br><br>
Ação 2. Distribua o protocolo para os diretores escolares.
<br><br>
Ação 3. Organize a compra e distribuição de materiais de limpeza e de proteção individual para as unidades escolares.
<br><br>
Ação 4. Forme um time de inspeção, composto por gestores da Secretaria de Educação e da Vigilância Sanitária, para avaliar a adequação das unidades de ensino ao protocolo e identificar a necessidade de realização de pequenas reformas.  
<br><br>
Ação 5. Agende e realize visitas de inspeção nos prédios das escolas da sua rede. 
<br><br>
Ação 6. Implemente as obras de adequação necessárias.
<br><br>
Ação 7. Faça uma nova rodada de visitas de inspeção e certifique-se que as unidades têm as condições definidas no protocolo sanitário para a retomada. 
<br><br>
Ação 8. Comunique sobre o retorno. Prepare materiais informativos sobre a Covid-19 e os protocolos sanitários adotados, para que a comunidade escolar e a sociedade em geral estejam bem informadas sobre as medidas de prevenção tomadas nessa retomada. 
<br><br>
<b>Quer saber quais são as principais recomendaçõe sanitárias e protocolos para um retomada segura? Clique e confira o material que criamos com as principais recomendações para da Covid-19 dentro e fora da escola:</b>"""
    obj4 = "Identificar, a partir da definição de grupos de risco para Covid-19, quantos estudantes e professores poderão retornar às atividades presenciais em cada unidade escolar."
    term4 = "Projetar a quantidade de estudantes e professores que não retornarão às salas de aula presenciais. Só assim você terá informação qualificada para avaliar o modelo de reabertura mais adequado à realidade da sua comunidade escolar. "
    prat4 = """Ação 1. Peça aos diretores das escolas que dimensionem quantos alunos de cada unidade de ensino, provavelmente, não irão retornar às salas de aula diante de uma retomada das atividades presenciais. Sugerimos que você utilize o canal de comunicação estabelecido pela Comissão de Reabertura, conforme orientado no Passo 1 deste guia, para essa comunicação.  
<br><br>
Ação 2. Dimensione quantos professores estão em grupo de risco e não poderão retornar para atividades presenciais por esse motivo. 
<br><br>
<b>Informe os dados da sua rede e Simule o retorno:</b>"""
    obj5 = "Planejar e definir qual modelo de reabertura das escolas é mais adequado para sua realidade."
    term5 = "Saber quais grupos de estudantes terão prioridade na retomada de atividades presenciais, reorganizando turmas e salas de acordo com o modelo adotado."
    prat5 = """Ação 1. Determine como será usado o tempo presencial e o tempo remoto, se existir. 
<br><br>
Ação 2. Estabeleça qual modelo será adotado no retorno à sala de aula: serão priorizados os anos terminais ou será dada prioridade a alunos com dificuldade de acompanhar o ensino remoto, por exemplo?
<br><br>
Ação 3. Feito o diagnóstico de professores e alunos que podem retornar, conforme definido no passo 4 deste guia, e com base no modelo de retomada escolhido, reorganize a divisão de salas e turmas. Caso necessário, programe a contratação de professores substitutos para suprir a falta de professores que integram o grupo de risco e não poderão retornar.
<br><br>
Ação 4. Comunique à comunidade escolar o modelo adotado e a nova organização de estudantes e professores. 
<br><br>
<b>Entenda que critérios adotar para definir o melhor modelo para sua rede></b>"""
    obj6 = "Preparação do material pedagógico de acordo com o modelo de reabertura definido."
    term6 = "Dispor do material mais adequado para dar sequência ao processo de aprendizado dos estudantes. "
    prat6 = """Ação 1. Revise e prepare o material pedagógico para possibilitar um retorno adequado da rede, considerando o modelo de reabertura adotado. 
<br><br>
Ação 2. Prepare o apoio pedagógico (currículo, formação, avaliação, busca ativa). 
<br>
Recomendamos que o estudante tenha a opção de dar continuidade a sua formação no modo remoto. Caso seja adotado esse modelo, sugerimos que professores que não podem retornar para sala de aula fiquem responsáveis pela produção de material de alunos que continuam remotos."""
    obj7 = "Identificar e atuar sobre alunos que não têm acompanhado as atividades remotas e estão em risco de perder o vínculo com a comunidade escolar. "
    term7 = "Estabelecer uma rotina de busca ativa e suporte aos estudantes da sua comunidade escolar, para superar os desafios impostos pela Covid-19. "
    prat7 = """Ação 1. Estabeleça  junto à Secretaria de Assistência/Desenvolvimento Social uma rotina de identificação e busca ativa de alunos que não retornaram à sala de aula.
<br><br>
Ação 2. Implemente, em parceria com a Secretaria de Saúde do estado ou município, canais de atenção à saúde mental para apoiar profissionais, estudantes e responsáveis nesse processo de retorno."""
    obj8 = "Estruturar um plano de contingência para identificar, isolar e acompanhar casos suspeitos de Covid-19 dentro de unidades escolares.  "
    term8 = "Saber o que fazer e a quem acionar diante do surgimento de um caso suspeito de Covid-19 após a retomada das atividades presenciais. "
    prat8 = """Ação 1. Pactue com a Unidade Básica de Saúde da região de cada escola como será feito o acompanhamento da comunidade escolar.<br>
<br>
Ação 2. Prepare um processo de tomada de decisão sobre fechamento de escolas, definindo papéis e responsabilidades de professores, diretores, secretaria e pais e responsáveis.<br>
<br>
Ação 3. Prepare o porta-voz da Comissão de Reabertura, prevista no passo 1 deste guia, para uma rotina de comunicação acerca da suspensão de atividades de turmas e em escolas à comunidade e à imprensa.<br> 
<br>
Ação 4. Prepare um fluxograma para atribuir responsabilidades diante de um possível caso suspeito e comunique os procedimentos de contingência à comunidade escolar.
<br><br>
<b>Acesse nossa ferramenta para conhecer as indicações de como se preparar, agir e monitorar casos suspeitos ou confirmados de Covid-19:</b>"""
    obj9 = "Instruir e capacitar todos os envolvidos no retorno às atividades presenciais nas escolas."
    term9 = "Ter equipe e comunidade escolar alinhadas e bem informadas sobre os protocolos e procedimentos de prevenção à Covid-19."
    prat9 = """Ação 1. Instrua os gestores escolares, docentes e demais colaboradores das escolas, bem como pais e responsáveis, para que todos estejam alinhados com as novas condutas e responsabilidades, para garantir a observação do protocolo sanitário adotado para reabertura das escolas.
<br><br>
Ação 2. Distribua para as escolas e para a comunidade os materiais de comunicação de procedimentos e novas diretrizes, como cartazes e posters."""
    obj10 = "Manter uma rotina de acompanhamento regular das escolas após a reabertura e da situação da doença na sua cidade."
    term10 = "Saber qual a situação da Covid-19 no seu terrítório e na sua rede escolar para agir com velocidade diante de alguma mudança de cenário. "
    prat10 = """Ação 1. Pactue com a Secretaria de Saúde uma rotina de atualização sobre a situação epidemiológica da doença na sua cidade. 
<br><br>
Ação 2. Acompanhe também a situação epidemiológica da rede e dos casos nas escolas. 
<br><br>
Ação 3. Prepare comunicados internos sobre a situação da rede e determine uma periodicidade de envio.
<br><br>
Ação 4. Planeje e realize uma estratégia de comunicação com a imprensa sobre a situação das escolas.
<br><br>
Ação 5. Acompanhe também a situação epidemiológica da rede e dos casos nas escolas.
<br><br>
<b>Você pode utilizar este formulário como modelo para distribuir para as escolas utilizarem para informar a secretária sobre o caso suspeito ou confirmado:</b>"""
    st.write(
        f"""
        <div class="conteudo" style="padding-top:50px;">
            <div class="flat-tabs-left flat-tabs-orange tabs-zoom-in">
                <input type="radio" id="tab-1" name="flat-tabs-left" class="section-one">
                <label for="tab-1"><i></i>1. Diálogo</label>
                <input type="radio" id="tab-2" name="flat-tabs-left" class="section-two">
                <label for="tab-2"><i></i>2. Critérios</label>
                <input type="radio" id="tab-3" name="flat-tabs-left" class="section-three">
                <label for="tab-3"><i></i>3. Protocolos</label>
                <input type="radio" id="tab-4" name="flat-tabs-left" class="section-four">
                <label for="tab-4"><i></i>4. Dimensionamento</label>
                <input type="radio" id="tab-5" name="flat-tabs-left" class="section-five">
                <label for="tab-5"><i></i>5. Modelo</label>
                <input type="radio" id="tab-6" name="flat-tabs-left" class="section-six">
                <label for="tab-6"><i></i>6. Pedagógico </label>
                <input type="radio" id="tab-7" name="flat-tabs-left" class="section-seven">
                <label for="tab-7"><i></i>7. Pessoas</label>
                <input type="radio" id="tab-8" name="flat-tabs-left" class="section-eight">
                <label for="tab-8"><i></i>8. Contingência</label>
                <input type="radio" id="tab-9" name="flat-tabs-left" class="section-nine">
                <label for="tab-9"><i></i>9. Capacitação</label>
                <input type="radio" id="tab-10" name="flat-tabs-left" class="section-ten">
                <label for="tab-10"><i></i>10. Acompanhamento </label>           
                <ul>
                    <li class="section-one" id="section-one">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>1. Diálogo</b>
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                 <div style="padding-bottom: 10px;">
                                    {obj1}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term1}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat1}
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
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>2. Determine as condições do retorno
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj2}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term2}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat2}
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
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>3. Protocolos sanitários
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj3}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term3}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat3}
                                </div>
                                <div class="upper-padding row">
                                    <div class="col card-plan container">
                                        <div class="left-margin">
                                            <div class="text-title-section main-orange-span minor-padding"> 
                                                <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon">
                                                <b>Protocolos</b>
                                            </div>
                                            <div class="minor-padding main-black-span">
                                                O PDF que você encontrará aqui inclui as <b>recomendações sanitárias e protocolos</b> que podem ser utilizados com a rede para conferir sua adequação dentro das unidades, durante o transporte escolar e até mesmo nas secretarias.
                                            </div><br>
                                            <div class="button-position" style="padding-bottom: 10px;">
                                                <a href="https://drive.google.com/file/d/1T8OsZ5PKFC5vn6QrtSJdkOlONaJjS8lc/view?usp=sharing" target="blank_">
                                                <button class="button"; style="border-radius: .25rem;">acesse ></button><br>
                                                </a>
                                            </div>
                                            <div class="minor-padding main-black-span">
                                                <br>Ou confira o arquivo em forma de <b>lista para verifição</b>.
                                            </div><br>
                                            <div class="button-position" style="padding-bottom: 10px;">
                                                <a href="https://drive.google.com/file/d/1MH6Cpf43Eq31MKqqE39FGMK-aruCD9_c/view?usp=sharing" target="blank_">
                                                <button class="button"; style="border-radius: .25rem;">acesse ></button><br>
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
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>4. Dimensione a rede
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj4}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term4}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat4}
                                </div>
                                <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                    <a href='{urlpath}?page=simulation' target="_blank">
                                    <button class="button"; style="border-radius: 0.8rem;">Simular ></button><br>
                                    </a>
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-five">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>5. Decida o modelo de reabertura
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj5}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term5}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat5}
                                </div>
                                <div>
                                <div align="center" style="padding-top:15px; padding-bottom: 15px;">
                                        <a href='{urlpath}?page=simulation' target="_blank">
                                        <button class="button"; style="border-radius: 0.8rem;">Simular ></button><br>
                                        </a>
                                    </div>
                                </div>
                            </div> 
                        </div>
                    </li>
                    <li class="section-six">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>6. Prepare o material pedagógico
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj6}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term6}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat6}
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-seven">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>7. Dê atenção aos alunos
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj7}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term7}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat7}
                                </div>
                            </div>  
                        </div>
                    </li>
                     <li class="section-eight">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>8. Plano de contingência
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj8}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term8}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat8}
                                </div>
                                <div class="upper-padding row">
                                    <div class="col card-plan container" style="padding:20px;">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                            <img class="icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
                                            <b>Ferramenta de notificação</b>
                                        </div>
                                        <br>
                                        <b><i>O que é?</b></i><br>
                                        Arquivo PDF com perguntas que podem ser utilizadas para criar formulário de notificação de casos suspeitos ou confirmados na escola.<br><br>
                                        <div class="minor-padding button-position">
                                            <a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view" target="_blank">
                                                <button class="button"; style="border-radius: .25rem;"> acesse aqui ></button>
                                            </a>
                                        </div>
                                        </div><br>
                                    </div>
                                    <div class="col card-plan container" style="padding:20px;">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                                <img class="icon" src="data:image/png;base64,{plan_icon}" alt="Fonte: Flaticon">
                                                <b>Plano de contingência</b>
                                            </div>
                                            <div>
                                                <br>
                                                <b><i>O que é?</b></i><br>Plano de Ação e Monitoramento na identificação de casos.
                                                <br><br>
                                            </div>
                                            <div class="minor-padding button-position">
                                                <a href="https://drive.google.com/file/d/1L6FXolCFTGQrfz_TT9zzxh1ojR5KfWEB/view">
                                                    <button class="button"; style="border-radius: .25rem;"> acesse aqui > </button>
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
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>9. Instrua os profissionais
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj9}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                 <div style="padding-bottom: 10px;">
                                   {term9}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;">
                                    {prat9}
                                </div>
                            </div>  
                        </div>
                    </li>
                    <li class="section-ten" id="section-ten">
                        <div class="grid-container">
                            <div class="column-twelve">
                                <div class="title-section">
                                    <img class="square" src="https://i.imgur.com/gGIFS5N.png"><b>10. Acompanhe sua rede!
                                </div>
                                <div class="title-section">OBJETIVO DESTA ETAPA</div>
                                <div style="padding-bottom: 10px;">
                                    {obj10}
                                </div>
                                <div class="title-section">AO TÉRMINO DESTA ETAPA VOCÊ CONSEGUIRÁ</div>
                                <div style="padding-bottom: 10px;">
                                    {term10}
                                </div>
                                <div class="title-section">COLOCANDO EM PRÁTICA</div>
                                <div style="padding-bottom: 10px;"> 
                                    {prat10}
                                </div>
                                <div class="row">
                                    <div class="col card-plan container" style="padding:15px;">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                            <img class="icon" src="data:image/png;base64,{notify_icon}" alt="Fonte: Flaticon">
                                            <b>Ferramenta de notificação</b>
                                        </div>
                                        <br>
                                        <b><i>O que é?</b></i><br>
                                        Arquivo PDF com perguntas que podem ser utilizadas para criar formulário de notificação de casos suspeitos ou confirmados na escola.<br><br>
                                        <div class="minor-padding button-position">
                                            <a href="https://drive.google.com/file/d/1-vmLPk7Cw6CBBC1aNrj9pQFt7aN-uskz/view" target="_blank">
                                                <button class="button"; style="border-radius: .25rem;"> acesse aqui ></button>
                                            </a>
                                        </div>
                                        </div><br>
                                    </div>
                                    <div class="col card-plan container" style="padding:15px;">
                                        <div>
                                         <div class="text-title-section minor-padding main-orange-span"> 
                                            <img class="icon" src="data:image/png;base64,{protocol_icon}" alt="Fonte: Flaticon"><b>Todos os Passos</b>
                                        </div>
                                        <br>
                                        Gostou do conteúdo? Acesse o Guia com os 10 Passos em forma de lista abaixo e aproveite para distribuir ele para sua rede!<br><br>
                                        <div class="minor-padding button-position">
                                            <a https://drive.google.com/file/d/1HqWKjM8uD4HM64fbFcbjS-pPD3SzWcmt/view?usp=sharing" target="_blank">
                                                <button class="button"; style="border-radius: .25rem;"> acesse aqui ></button>
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
    tm.genSimule()
    foo.genFooter()


if __name__ == "__main__":
    main()
