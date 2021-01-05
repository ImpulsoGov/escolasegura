# 🏫📚 Escola Segura

**Como preparar a minha rede escolar para um retorno presencial seguro?**

É com essa pergunta que iniciamos o **Escola Segura**, a ferramenta de educação da **Impulso**. Queremos com ela facilitar o processo de decisão do retorno às atividades presenciais em escolas. 

Todos os dados utilizados na ferramenta são abertos e estão disponíveis na nossa [API](http://datasource.coronacidades.org/br). Além disso, com nosso código aberto, incentivamos a transparência e subimissão de melhorias.

A **Escola Segura** está disponível [aqui](https://escolasegura.coronacidades.org/). As informacões compiladas do projeto pode ser acessada [aqui](https://sites.google.com/impulsogov.org/wiki-techdados/produtos/escola-segura?authuser=1&read_current=1).

**Missão**:  Oferecer guias e protocolos para possibilitar uma reabertura planejada da rede pública de ensino, respeitando boas práticas de distanciamento social e segurança sanitária para manter o controle da covid-19. 

**Público**: voltada para integrantes de secretarias de educação de estados e municípios.


## Desenvolvimento

Instruções para rodar a aplicação localmente:

### Streamlit

```bash
# Para criar uma env
pip install virtualenv
virtualenv nome_da_virtualenv
# Para ativar a env (Windows)
cd nome_da_virtualenv\Scripts\activate
# Para ativar a env (Linux)
source nome_da_virtualenv/bin/activate
```
#### Instalação da versão apropriada do Streamlit
Faça o download através desse [link](https://escolasegura.coronacidades.org/).

```bash
# Com seu ambiente virtual ativo,
# rode o shell no diretório que salvou o streamlit e insira o comando
pip install streamlit-0.70.0-py2.py3-none-any.whl
```

```bash
# roda em localhost:8501
pip install -r requirements.txt
cd src
streamlit run escolasegura.py
```
### Docker

- Linux/Mac:

```bash
# antes instale o docker
# roda em localhost:8501 com shell aberto
make docker-build-dev
```

- Windows:

[wip rodando com o docker]
