# 🏫📚 Escola Segura

**Salas abertas para estudantes**

**Portas fechadas para a Covid-19**

Em um primeiro momento, a pandemia de Coronavírus exigiu a interrupção das aulas presenciais e o fechamento de escolas das redes municipais e estaduais por todo o Brasil. As medidas foram necessárias como parte dos esforços para interromper a propagação da doença. Hoje, após muitos meses de atuação na resposta ao coronavírus e os aprendizados acumulados ao redor do mundo, já é possível compreender melhor o comportamento da doença e adotar medidas de prevenção que possibilitem a retomada das atividades escolares presenciais de forma segura para estudantes, professores e equipe escolar. 

O retorno às atividades presenciais em escolas deve levar em consideração diversas variáveis, priorizando sempre a saúde dos atores envolvidos. Para apoiar secretários de educação e demais integrantes da gestão pública nesse processo, desenvolvemos a **Escola Segura**, uma ferramenta online da plataforma **CoronaCidades** que oferece protocolos, simuladores e checklist para orientar todas as etapas do retorno às aulas, desde o planejamento até o monitoramento das escolas reabertas. 


É com essa pergunta que iniciamos o **Escola Segura**, a ferramenta de educação da **Impulso**. Queremos com ela facilitar o processo de decisão do retorno às atividades presenciais em escolas. 

Todos os dados utilizados na ferramenta são abertos e estão disponíveis na nossa [API](http://datasource.coronacidades.org/br). Além disso, com nosso código aberto, incentivamos a transparência e submissão de melhorias.

A **Escola Segura** está disponível [aqui](https://escolasegura.coronacidades.org/).


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
