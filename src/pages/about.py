import streamlit as st
import utils
import pages.snippet as tm
import pages.header as he
import pages.footer as foo

def main(session_state):
    """ 
    This is a function that returns the "about" page
      
    Parameters: 
        session_state (type): section dataset
    """
    he.genHeader()
    utils.main_title(title="<b>Quem Somos?</b>", subtitle="")
    utils.localCSS("localCSS.css")
    # utils.gen_title(title="Quem somos?")
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
    inclusivo e avançado. Saiba mais em: <a target="_blank" href="fundacaolemann.org.br">fundacaolemann.org.br</a>"""
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
    utils.gen_title(title="Impulso", subtitle=impulsodescricao)
    utils.gen_title(title="Banco Interamericano de Desenvolvimento", subtitle=biddescricao)
    utils.gen_title(title="Fundação Lemann", subtitle=lemanndescricao)
    utils.gen_title(title="Imaginable Futures", subtitle=imaninabledescricao)
    utils.gen_title(title="Programa Formar", subtitle=formardescricao)

    tm.genTermo()
    foo.genFooter()


if __name__ == "__main__":
    main()