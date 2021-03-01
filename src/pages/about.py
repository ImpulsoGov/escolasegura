import streamlit as st
import utils
import pages.snippet as tm
import pages.header as he
import pages.footer as foo

def main():
    """ 
    This is a function that returns the "about" page
      
    Parameters: 
        session_state (type): section dataset
    """
    utils.localCSS("localCSS.css")
    he.genHeader("sobre")
    utils.main_title(title="<b>Quem Somos?</b>", subtitle="")
    utils.gen_title(title="Sobre Nós", subtitle="")
    impulsodescricao = """A Impulso é uma organização não governamental com a missão auxiliar governos na melhora da entrega de 
    serviços públicos de saúde à população através do uso de dados e tecnologia, apoiando o processo de 
    tomada de decisão e visando o aprimoramento contínuo de políticas públicas. Foi fundada em 2019 e é 
    uma das idealizadoras da plataforma <a target="_blank" href="https://coronacidades.org/">CoronaCidades.org</a>."""
    biddescricao = """"O Banco Interamericano de Desenvolvimento tem como missão melhorar vidas. 
    Criado em 1959, o BID é uma das principais fontes de financiamento de longo prazo para o desenvolvimento 
    econômico, social e institucional da América Latina e do Caribe. O BID também realiza projetos de pesquisas 
    de vanguarda e oferece assessoria sobre políticas, assistência técnica e capacitação a clientes públicos e 
    privados em toda a região."""
    lemanndescricao = """"A Fundação Lemann acredita que um Brasil feito por todos e para todos é um Brasil 
    que acredita no seu maior potencial: gente. Isso só acontece com educação de qualidade e com 
    o apoio a pessoas que querem resolver os grandes desafios sociais do país. Nós realizamos 
    projetos ao lado de professores, gestores escolares, secretarias de educação e governos 
    por uma aprendizagem de qualidade. Também apoiamos centenas de talentos, lideranças e organizações 
    que trabalham pela transformação social. Tudo para ajudar a construir um país mais justo, 
    inclusivo e avançado. Saiba mais em: <a target="_blank" href="https://fundacaolemann.org.br/">fundacaolemann.org.br</a>"""
    imaninabledescricao = """"Imaginable Futures é uma empresa de investimento filantrópico global que acredita 
    que a aprendizagem tem o poder de estimular o potencial humano e tem como missão oferecer 
    a cada aluno oportunidades e ferramentas para que eles imaginem e realizem um futuro brilhante. 
    Com compromisso com a parceria e a cocriação, a organização está capacitando alunos, famílias 
    e comunidades para serem os agentes que moldam o futuro. A Imaginable Futures é um empreendimento 
    do The Omidyar Group, fundada e financiada por Pierre e Pam Omidyar."""
    formardescricao = """"O programa Formar foi concebido na Fundação Lemann e atua em parceria com 
    redes públicas de educação em todo o Brasil. Sua gestão é feita por uma equipe 
    multidisciplinar de consultores e especialistas que buscam o aprimoramento da gestão 
    pedagógica e administrativa, a partir do engajamento de dirigentes e equipes gestoras 
    das secretarias e escolas que compõem os sistemas de educação. Buscam também estimular 
    a adoção de políticas públicas perenes que contribuam na melhoria do processo de 
    aprendizagem juntamente com professores e estudantes."""
    st.write(
        f"""
        <div class="conteudo" style="padding-bottom: 10px;">
            <b>Impulso</b><br>{impulsodescricao}<br>
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            <b>Fundação Lemann</b><br>{lemanndescricao}<br>
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            <b>Imaginable Futures</b><br>{imaninabledescricao}<br>
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            <b>Programa Formar</b><br>{formardescricao}<br>
        </div>
        """,
        unsafe_allow_html=True,
    )
    embasamento = """Para a construção do Escola Segura, revisamos a literatura científica, consultamos protocolos encontrados em manuais de retomada do ensino presencial tanto no Brasil como no exterior e pesquisamos as melhores práticas e seus resultados para trazer informações atualizadas e embasadas na ciência. Não menos importante, conversamos com gestores escolares das diversas regiões do país para compreender os desafios enfrentados por eles em seu trabalho com a rede escolar e com a comunidade. Essas conversas levantaram questões e desafios que guiaram nossa busca pelo o que há de mais consolidado na literatura científica e nas diretrizes técnicas de órgãos reguladores sobre uma retomada segura das atividades em ambiente escolar.<br><br>
Após a revisão de documentos técnicos e guias operacionais realizados por agências especializadas como o Center of Disease Control and Prevention (CDC - EUA)[15][20],pela  Escola de Saúde Pública T.H. Chan da Universidade de Harvard[21], pela Organização Mundial da Saúde (OMS)[19], pelo MInistério da Educação[18] e da Saúde[16] do Brasil, pela Fiocruz[17] e pelo Município de Sobral[22] e realizando conversas técnicas com especialistas na área de Educação e gestão escolar, desenvolvemos os 10 Passos, uma ferramenta para guiar a retomada presencial das aulas nas escolas. O objetivo dos 10 Passos é  fornecer ao gestor uma visão objetiva sobre as principais macro ações a serem tomadas durante o processo de retomada das atividades presenciais nas escolas, servindo de guia para reflexões mais aprofundadas sobre cada etapa em um segundo momento.<br><br>
Para esse segundo momento, o Escola Segura traz uma série de ferramentas auxiliares como o Simulador de Retomada, Plano de Ação e Monitoramento, Ferramentas de Verificação e Notificação de Casos Suspeitos e/ou Confirmados, e Protocolos de Atuação.<br><br>
Na estruturação do Simulador foram utilizados como base modelos de retomada do ensino presencial apresentados pela UNESCO[2][4], pela ONU[3], e pela Comissão de Educação do Estado da Carolina do Norte - EUA[5]. Utilizamos também considerações sobre espalhamento da COVID19 dentro dos ambientes de ensino apresentadas em papers e reportagens sobre a experiência de outros países[1][6][7][8][9]. <br><br>
Para as informações sobre protocolos de limpeza e higienização do ambiente escolar, foram utilizados manuais disponibilizados pelo Governo do Amazonas para a retomada das atividades escolares[10] e determinações técnicas de agências de regulação e vigilância sanitária como a ANVISA[12][13] e o CDC (Center for Disease Control) - EUA[14]. Consultamos também as diretrizes sobre cuidado e limpeza em ambientes com risco biológico elaboradas pelo Centro Colaborador para a Qualidade do Cuidado e Segurança do Paciente - Proqualis[11] - entidade vinculada ao ICICT/Fiocruz e que tem como objetivo ser uma fonte de conteúdos técnico-científicos para a área da saúde para adaptar esses cuidados ao ambiente escolar, considerando as melhores práticas que devem ser realizadas quando o risco de contaminação está presente.<br><br>
O Escola Segura traz também uma ferramentas específicas com protocolos sanitários a serem seguidos pelos funcionários das Escolas em relação ao ambiente escolar, ao transporte escolar, à secretaria e atividades administrativas e a comunidade. Para a elaboração desses protocolos, orientações do Center for Disease Control (CDC)-EUA[15] e da ONU[19] foram utilizadas como bases, sendo feitas adaptações que refletem as diversas realidades encontradas no Brasil.<br><br>
O Escola Segura traz um modelo de Plano de Ação e Monitoramento na identificação de casos para auxiliar o gestor a organizar sua rede para lidar com casos suspeitos e/ou confirmados entre alunos e funcionários. Para a criação desse plano de ação, foram utilizadas novamente as considerações do CDC-EUA, além de diretrizes dos Ministérios da Educação[18] e da Saúde[16] do Brasil, e Fiocruz[17]."""
    utils.gen_title(title="Embasamento científico e metodológico", subtitle=embasamento)
    embasamentosimulador =  """Uma das ferramentas disponíveis no Escola Segura é o Simulador de Retomada Presencial das Atividades Escolares. O objetivo dessa ferramenta é auxiliar o gestor escolar no planejamento da capacidade física das escolas de sua rede, considerando o número de docentes, alunos e salas na simulação de possíveis modelos a serem adotados. 
<br><br>Utilizando o Simulador, o gestor poderá testar diferentes configurações de carga horária diária presencial (de 0 até 6 horas) e remota (de 0 até 6 horas) que cada turma terá e como essa configuração escolhida afeta a organização e dimensionamento das necessidades estruturais para a retomada. 
<br><br>Para utilizar o Simulador, o gestor deve primeiramente selecionar qual 1. Estado da federação, 2.  Município e 3. Nível de Administração (Estadual, Municipal, ou Todos) ele deseja. A partir dessa informação, o Simulador traz, segundo os dados do último CENSO ESCOLAR, o 4. “Total de alunos matriculados” e o 5. “Total de professores” da rede. Atenção: Se o nível selecionado for Rede - tanto Municipal como Estadual - os dessas categorias são fixos, mas se o nível selecionado for "Escolar" esses valores são livres para serem alterados. O gestor pode ainda, inserir a 6. quantidade de alunos e de 7. professores que ele já estima que não irão retornar presencialmente (exemplo: professores e alunos que fazem parte de grupos de alto risco para a Covid-19).
<br><br>No segundo passo, o gestor deve informar a 1. “Quantidade de salas disponíveis” e 2. o “número máximo de alunos em cada sala”. Deixamos como referência uma ferramenta de auxílio para esse cálculo que foi desenvolvida pela Faculdade de Educação da UNICAMP. 
<br><br>No terceiro e último passo, o gestor pode selecionar a 1. quantidade de “horas diárias presencial” que deseja atribuir às turmas (variando de 0 à 8 horas diárias), 2. A quantidade de “horas diárias de aula remota por turma” (variando de 0 à 6 horas diárias), 3. “Número de turnos em um dia” (variando de 0 à 12 turnos por dia). O gestor preenche ainda a quantidade de 4. “Horas aula diárias por professor” e 5. “Tempo de hora aula” (em minutos).
<br><br>Com isso, o Simulador devolve ao gestor três grupos de informação: Sobre turmas, sobre sua organização de recursos, e sobre a quantidade necessária de materiais como máscaras, álcool em gel e termômetros.
<br><br>Sobre turmas, o resultado da simulação informa a quantidade de turmas que o gestor consegue retornar e também a quantidade de dias letivos necessários para cumprir as 800 horas anuais determinadas pelo MEC[24].
<br><br>Sobre a organização, o resultado da simulação traz o número de alunos e professores que retornariam e os que não retornariam - baseado na informação passada pelo gestor, o número de salas ocupadas com aulas presenciais e o número de salas ficaram livres. Esse cálculo é realizado com base nos parâmetros definidos pelo próprio gestor nos segundo e terceiro passos.
<br><br>Sobre os materiais, o resultado da simulação traz a quantidade que seriam necessárias semanalmente a serem disponibilizadas para alunos e docentes de: álcool em gel, máscaras e termômetros. Esses cálculos são realizados com base nas informações passadas pelo gestor e em determinações técnicas da Fiocruz / Proqualis [11][17] e dos Ministérios da Saúde[16]  e Educação[18]."""
    st.write(
        f"""
        <div class="conteudo title-section" style="padding-bottom:20px;"> 
            <img id="embasamentosimulador" class="square" src="https://i.imgur.com/gGIFS5N.png">
            Metodologia e Uso do Simulador de Retomada Presencial das Atividades Escolares
        </div>
        <div class="conteudo" style="padding-bottom: 10px;">
            {embasamentosimulador}
        </div>
        """,
        unsafe_allow_html=True,
    )
    utils.gen_title(title="Fontes e referências", subtitle="<br>")    
    st.write(
        f"""
        <div class="conteudo main-padding">
            <div class="table-responsive">
            <table>
                <thead>
                    <tr>
                        <th>Título</th>
                        <th>Fonte</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>[1] COVID-19 Mathematical Modeling for Cornell’s Fall Semester </td>
                        <td> <a href="https://people.orie.cornell.edu/pfrazier/COVID_19_Modeling_Jun15.pdf">
                            Cornell University
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[2] Framework for reopening schools</td>
                        <td> <a href="https://unesdoc.unesco.org/ark:/48223/pf0000373348">
                            United Nations Educational, Scientific and Cultural Organization (UNESCO)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[3] Education during Covid-19 and beyond </td>
                        <td> <a href="https://www.un.org/development/desa/dspd/wp-content/uploads/sites/22/2020/08/sg_policy_brief_covid-19_and_education_august_2020.pdf">
                             United Nations (UN)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[4] COVID-19 response – hybrid learning</td>
                        <td> <a href="https://en.unesco.org/sites/default/files/unesco-covid-19-response-toolkit-hybrid-learning.pdf">
                            United Nations Educational, Scientific and Cultural Organization (UNESCO)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[5] LIGHTING OUR WAY FORWARD: North Carolina’s Guidebook for Reopening Public Schools </td>
                        <td> <a href="https:https://www.dpi.nc.gov/news/covid-19-response-resources/lighting-our-way-forward">
                            DPI
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[6] Restarting and Reinventing School </td>
                        <td> <a href="https://restart-reinvent.learningpolicyinstitute.org/">
                            Learning Policy Institute
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[7]  Determining  the  optimal  strategy  for  reopening  schools,  work  and  society  in  the  UK: balancing  earlier  opening  and  the  impact  of  test  and  trace  strategies  with  the  risk  of occurrence of a secondary COVID-19 pandemic wave </td>
                        <td> <a href="https://www20.anvisa.gov.br/segurancadopaciente/images/documentos/ManualLimpezaeDesinfeccaofinal.pdf">
                           ANVISA
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[8] Mathematical model of Covid-19 spread: How to reopen a college campus </td>
                        <td> <a href="https://www.youtube.com/watch?v=9K_BjXRe-wk">
                           Michigan Technological University
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[9] An Examination of School Reopening Strategies during the SARS-CoV-2 Pandemic</td>
                        <td> <a href="https://doi.org/10.1101/2020.08.05.20169086">
                           DOI
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[10] Manual de Protocolos de Saúde</td>
                        <td> <a href="http://www.educacao.am.gov.br/wp-content/uploads/2020/07/PROTOCOLOS-DE-SAuDE02.pdf">
                           Governo do Estado do Amazonas
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[11] Ferramenta de Planejamento e Cálculo de Custos de Preparações Alcoólicas para a Higiene das Mãos</td>
                        <td> <a href="https://proqualis.net/sites/proqualis.net/files/FerramentadePlanejamentoeClculodeCustosgrfica.pdf">
                            Proqualis
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[12] Segurança do paciente em serviços de saúde: limpeza e desinfecção de superfícies</td>
                        <td> <a href="https://www20.anvisa.gov.br/segurancadopaciente/index.php/publicacoes/item/seguranca-do-paciente-em-servicos-de-saude-limpeza-e-desinfeccao-de-superficies">
                            ANVISA
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[13] NOTA TÉCNICA Nº 47/2020/SEI/GIALI/GGFIS/DIRE4/ANVISA
Uso de luvas e máscaras em estabelecimentos da área de
alimentos no contexto do enfrentamento ao COVID-19.
</td>
                        <td> <a href="https://www.gov.br/anvisa/pt-br/arquivos-noticias-anvisa/310json-file-1">
                            ANVISA
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[14] Appendix A – Risk-assessment for determining environmental cleaning method and frequency</td>
                        <td> <a href="https://www.cdc.gov/hai/prevent/resource-limited/risk-assessment.html">
                            Centers for Disease Control and Prevention (CDC)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[15] Checklist: Planning for In-Person Classes
Instituição: Centers for Disease Control and Prevention (CDC)
</td>
                        <td> <a href="https://www.cdc.gov/coronavirus/2019-ncov/community/pdf/Back-to-School-Planning-for-In-Person-Classes.pdf">
                            CDC
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[16] Orientações para Retomada Segura das Atividades Presenciais nas Escolas de Educação Básica no Contexto da Pandemia da COVID-19</td>
                        <td> <a href="http://antigo.saude.gov.br/images/pdf/2020/September/18/doc-orientador-para-retomada-segura-das-escolas-no-contexto-da-covid-19.pdf">
                            Ministério da Saúde
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[17] Manual sobre Biossegurança para Reabertura de Escolas no Contexto da COVID-19</td>
                        <td> <a href="https://portal.fiocruz.br/sites/portal.fiocruz.br/files/documentos/manualreabertura.pdf">
                            Fiocruz
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[18] Guia de Implementação de Protocolos de Retorno das Atividades Presenciais nas Escolas de Educação Básica</td>
                        <td> <a href="https://www.gov.br/mec/pt-br/assuntos/GuiaderetornodasAtividadesPresenciaisnaEducaoBsica.pdf">
                            Ministério da Educação
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[19] Considerations for school-related public health measures in the context of COVID-19</td>
                        <td> <a href="https://www.who.int/publications/i/item/considerations-for-school-related-public-health-measures-in-the-context-of-covid-19">
                            Organização Mundial da Saúde (OMS)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[20] Operating schools during COVID-19: CDC's Considerations</td>
                        <td> <a href="https://www.cdc.gov/coronavirus/2019-ncov/community/schools-childcare/schools.html?CDC_AA_refVal=https%3A%2F%2Fwww.cdc.gov%2Fcoronavirus%2F2019-ncov%2Fcommunity%2Fschools-childcare%2Fguidance-for-schools.html">
                            Centers for Disease Control and Prevention (CDC)
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[21] SCHOOLS FOR HEALTH: Risk Reduction Strategies for Reopening Schools</td>
                        <td> <a href="https://schools.forhealth.org/risk-reduction-strategies-for-reopening-schools/">
                            Harvard T.H. Chan School of Public Health
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[22] PLANO DE RETOMADA DAS ATIVIDADES DE EDUCAÇÃO PÚBLICA NO MUNICÍPIO DE SOBRAL</td>
                        <td> <a href="https://drive.google.com/file/d/1H2Gzr5C2I0dAA7fyGD5MZHVjwaolND3N/view">
                            Instituição: Município de Sobral - CE
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[23] Cálculo de estudantes por sala</td>
                        <td> <a href="https://www.fe.unicamp.br/salas/">
                            FE/Unicamp
                            </a>
                        </td>
                    </tr>
                    <tr>
                        <td>[24] LEI Nº 9.394
</td>
                        <td> <a href="http://www.planalto.gov.br/ccivil_03/leis/l9394.htm">
                            Presidência da República - Casa Civil
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
            </div>
        </div>
        """,
        unsafe_allow_html = True,
    )

    tm.genSimule()
    foo.genFooter()


if __name__ == "__main__":
    main()
