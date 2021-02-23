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
    he.genHeader("duvidasfrequentes")
    subtitle = """A Escola Segura, ferramenta online focada em orientar uma reabertura planejada da rede de ensino pública diante da Covid-19, promoveu encontros online com Wanderson Oliveira, epidemiologista e ex-Secretário Nacional de Vigilância em Saúde, para solucionar dúvidas de gestoras e gestores públicos sobre o assunto. 
Quatro encontros foram realizados, sempre às terças-feiras (24/11, 01/12, 08/12 e 15/12), e trataram sobre o uso de EPI nas escolas, a importância da definição conjunta de fluxos e sistemas de notificação entre secretarias de saúde e de educação, bem como ressaltaram as boas práticas pelo país.
<br><br>
Atua na gestão pública e precisa de apoio para pensar os desafios da saúde municipal e da reabertura de escolas? <a href="https://coronacidades.org/fale-conosco/" target="_self" style="text-decoration: none;">Fale conosco.</a>"""
    utils.main_title(title="<b>Dúvidas Frequentes</b>", subtitle=subtitle)
    utils.localCSS("localCSS.css")
    # utils.gen_title(title="Quem somos?")
    pergunta1 = """Wanderson Oliveira considera que o acesso a testes é um fator que pode ser diferenciador para aquelas escolas localizadas em cidades maiores em comparação com as instaladas em localidades menores. Mas mesmo sem a possibilidade de confirmar a covid-19 por teste, a escola tem total possibilidade de fazer a vigilância da doença, usando como critério a identificação de sintomas. “A realidade logística é diferente, mas se eu identifico sinais da síndrome respiratória e já afasto o caso suspeito, o teste é um acessório, o mais importante é identificar o suspeito e agir”, explica."""
    pergunta2 = """O epidemiologista elencou algumas boas práticas adotadas por redes de ensino no país para controlar a Covid-19 entre estudantes. Uma delas é fornecer grupos de máscaras divididas por cor para orientar a troca ao longo do período escolar. “O aluno utiliza três máscaras em um período, no primeiro horário são as máscaras azuis, no segundo as máscaras brancas e no terceiro, máscaras amarelas. Com essa divisão, a equipe escolar consegue identificar se os estudantes estão fazendo a renovação das máscaras corretamente”, exemplificou. Outra boa prática é a adoção, sempre que possível, de atividades ao ar livre, em que a chance de transmissão do coronavírus é muito menor. """
    pergunta3 = """No modelo de reabertura fundamentado em bolhas, os estudantes só interagem com um grupo fixo de pessoas na escola. Caso haja alguma contaminação, é possível, em um primeiro momento, isolar apenas aquela bolha, que esteve em contato com o suspeito. Wanderson Oliveira explica que esse modelo precisa ser adaptado à realidade de cada escola. “Não posso fazer uma reabertura escolar pensando na escola que existia antes da pandemia. É uma outra escola, que gira em torno de 40% a 60% da capacidade anterior instalada”, explica. “Eu posso dividir grupos de estudantes em uma mesma sala, bem ventilada, e organizar de tal maneira que crie camadas de proteção. Se todos os estudantes, professores, funcionários estiverem usando máscara, higienização das mãos e respeitando a distância de 1,5m, o risco de contaminação é baixo”, reforça. """
    pergunta4 = """Segundo Wanderson Oliveira, esses critérios vão variar de acordo com a realidade da escola e o modelo pedagógico adotado nessa retomada. “Se a escolha foi pelo sistema de bolhas, em que existem grupos de estudantes e não há contato entre alunos fora dessas bolhas, pode ser o caso de fazer o isolamento só daquele grupo, ou de uma sala de aula, mas não será necessário fechar a escola toda”, esclareceu. Caso o modelo adotado contemple a mesclagem de turmas, será necessário avaliar caso a caso. A adesão ao uso de EPIs, a ventilação dos espaços e a distância entre carteiras devem ser considerados nessa avaliação. 
<br>
Segundo o especialista, fechar a escola diante de uma necessidade de conter a Covid-19 não deve ser considerado um retrocesso, mas o processo sempre em aprimoramento. “Se eu tive um caso e precisei fechar a escola, interrompo as atividades por 14 dias, monitoro a evolução daquele caso, se a testagem deu positivo ou negativo, e depois retomo as atividades presenciais, com as medidas e cuidados necessários”, complementou. """
    pergunta5 = """A orientação de Wanderson Oliveira é para que as escolas promovam a vigilância de síndrome gripal. Segundo o especialista, em um primeiro momento, só com sintomas, não é possível cravar que um quadro é ou não de Covid-19. Diante da suspeita, os protocolos já devem ser acionados e as medidas serão mais ou menos restritivas dependendo da confirmação após a realização de testes. “Na definição de síndrome gripal eu tenho um quadro de sintomas, como tosse, febre e dor no corpo, por exemplo. Todos que apresentarem esse quadro serão considerados suspeitos pela escola”, explicou. “A escola passa a fazer parte de um rede de vigilância em saúde”, reforçou. """
    pergunta6 = """De acordo com o especialista, o diálogo com a comunidade deve ser uma constante no processo de retomada de atividades presenciais em escolas. “Precisamos dialogar com pais, responsáveis, lideranças comunitárias onde a escola está inserida para esclarecer que a pandemia não acabou. As medidas preventivas objetivam evitar ao máximo que casos dentro da escola aconteçam, mas eles podem acontecer”, reforçou. 
<br>
Para esse diálogo, a orientação é para que as escolas criem ambientes para ouvir e sanar dúvidas dos pais sobre os protocolos e medidas adotados. Wanderson Oliveira sugere o uso de ferramentas digitais gratuitas, como as disponíveis no Google, para promover reuniões online com pais e responsáveis e a criação de canais específicos no WhatsApp para essa comunicação. 
<br>
Além das escolas, as secretarias municipais de educação também podem contribuir com uma comunicação constante e esclarecedora com esse público. “Às vezes, a escola não tem dinheiro para manter uma linha de telefone exclusiva para essa comunicação com pais e responsáveis. A prefeitura poderia suprir essa situação, estabelecer um canal para receber demandas de pais e responsáveis, criar boletins informativos para que os pais se mantenham informados sobre o que está acontecendo no ambiente da escola em relação à Covid”, complementou."""
    pergunta7 = """O epidemiologista Wanderson Oliveira reforça a importância do uso de EPIs e adoção de medidas preventivas em uma eventual reabertura de escolas. Segundo o especialista, é fundamental o uso de máscaras para crianças acima de oito anos e todos os profissionais da equipe escolar, a manutenção de espaços ventilados e da distância de 1,5 metro entre os estudantes, bem como a higienização constante das mãos com água, sabão e álcool em gel.  
<br>
“O que deve ser evitado é o contato próximo, sem máscara, por mais de 15 minutos, a menos de um metro e meio de distância. Passar no corredor de máscara, por exemplo, não é contato próximo”, explicou."""
    utils.gen_title(title="Quais diferenças de estratégia podemos pensar para escolas urbanas e rurais?", subtitle=pergunta1)
    utils.gen_title(title="Quais boas estratégias têm sido adotadas no dia a dia de escolas que já reabriram e podem servir de exemplo?", subtitle=pergunta2)
    utils.gen_title(title="Como a dinâmica de bolhas pode ser implementada no ensino público?", subtitle=pergunta3)
    utils.gen_title(title="Que critérios adotar para decidir fechar uma turma ou uma escola inteira?", subtitle=pergunta4)
    utils.gen_title(title="Como identificar casos suspeitos e monitorar a presença da Covid-19 nas escolas?", subtitle=pergunta5)
    utils.gen_title(title="Como conscientizar e manter a comunicação com pais e responsáveis sobre regras e eventuais medidas de restrição?", subtitle=pergunta6)
    utils.gen_title(title="Quais os principais protocolos e equipamentos de proteção individual que devem ser adotados dentro da escola em uma eventual reabertura?", subtitle=pergunta7)

    tm.genSimule()
    foo.genFooter()


if __name__ == "__main__":
    main()
