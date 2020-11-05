# 🏫📚 Escola Segura

**Como preparar a minha rede escolar para um retorno presencial seguro?**

É com essa pergunta que iniciamos o **Escola Segura**, a ferramenta de educação da **Impulso**. Queremos com ela facilitar o processo de decisão do retorno às atividades presenciais em escolas. 

Todos os dados utilizados na ferramenta são abertos e estão disponíveis na nossa [API](http://datasource.coronacidades.org/br). Além disso, com nosso código aberto, incentivamos a transparência e subimissão de melhorias.

A **Escola Segura** está disponível [aqui]().


## Desenvolvimento

Instruções para rodar a aplicação localmente:

### Streamlit

```bash
# roda em localhost:8001
pip install -r requirements.txt
streamlit run src/escolasegura.py
```
### Docker

- Linux/Mac:

```bash
# antes instale o docker
# roda em localhost:8001 com shell aberto
make docker-build-dev
```

- Windows:

[wip rodando com o docker]
