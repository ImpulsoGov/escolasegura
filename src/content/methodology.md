## Metodologia de Simule o Retorno

### O que é?

O simulador é uma ferramenta para auxiliar o gestor nos cálculos de quantos alunos conseguem retornar às atividades escolares dadas as restrições de quantidade de professores e salas de aulas. 


### O que o simulador calcula?

A partir dos valores inseridos pelo usuário, o simulador calcula as seguintes quantidades:
- número de alunos que podem retornar às atividades escolares
- número de professores que podem retornar às atividades escolares
- número de maścaras descartáveis necessárias
- número de termômetros necessários
- número de litros de álcool em gel necessários


### O que o usuário seleciona no simulador?
Ao acessar a ferramenta, o usuário encontrará os seguintes campos para preenchimento:
 - **Quantidade de alunos que se deseja retornar (A):** O usuário fornece o número total de alunos que deseja retornar às atividades presenciais na rede local de ensino. O sistema automaticamente fornece como sugestão a quantidade que consta nas bases do governo. Contudo, o usuário está livre para escolher a quantidade que quiser.
- **Quantidade de professores disponíveis para retorno (P):** O usuário fornece o número de professores disponíveis para dar aula na rede local de ensino. O sistema automaticamente fornece como sugestão a quantidade de professores que consta nas bases do governo. Contudo, o usuário está livre para escolher a quantidade que quiser.
- **Número máximo de alunos por sala (K):** O usuário fornece o limite de alunos por sala determinado pelo gestor a fim de limitar a transmissibilidade da doença.
- **Modelo de retorno:** O usuário pode escolher os seguintes modelos de retorno:
    - **Modelo:** Totalmente presencial
        **Descrição:** Neste modelo, todos os estudantes retornam às aulas presenciais como antes, com os mesmos horários em sala de aula, porém seguindo os novos protocolos de distanciamento e segurança sanitária.
    - **Modelo:** Híbrido com aulas expositivas presenciais + tarefas para casa.
        **Descrição:** Nos modelos híbridos todos os estudantes retornam às aulas presenciais por tempo reduzido na escola e têm parte das aulas remotas. Em especial, neste modelo professores(as) transmitem conceitos para os estudantes presencialmente, e os estudantes completam exercícios e tarefas em casa.
    - **Modelo:** Híbrido: Aulas gravadas em vídeo + tarefas presenciais
    **Descrição:** Nos modelos híbridos todos os estudantes retornam às aulas presenciais por tempo reduzido na escola e têm parte das aulas remotas. Em especial, neste modelo estudantes aprendem novos conceitos de forma remota e concluem exercícios e tarefas presencialmente com o(a) professor(a).
    - **Modelo:** Híbrido: Aulas gravadas previamente e distribuídas em vídeo.
    **Descrição:** Nos modelos híbridos todos os estudantes retornam às aulas presenciais por tempo reduzido na escola e têm parte das aulas remotas. Em especial, neste modelo ambas as aulas expositivas e exercícios são feitos em sala e de forma remota.
    - **Modelo:** Prioritário: Aulas síncronas por vídeo com parte de estudantes em sala e parte em casa (grupo dividido)
    **Descrição:** Neste modelo, os professores têm uma aula normal completa com um grupo de estudantes presencial, enquanto outro grupo acompanha remotamente 
            por meio de videoconferência (VC).
Os modelos indicam a quantidade de horas de aula no dia de cada turma (ex: um modelo total presencial teria 5 horas de aula enquanto um modelo híbrido teria uma carga reduzida, de 3 horas). **Apenas um modelo deve ser escolhido por simulação.**


### Como calculamos as quantidades de alunos e professores retornando?

O simulador recebe todas as informações mencionadas acima e, além dessas quantidades, fixamos o total de horas disponíveis para aulas num dia (H = 10 = 5 horas x 2 turnos) para os cálculos. Assim, a quantidade máxima de aulas por dia (Q) é dada pela razão do total de horas disponíveis e a duração máxima escolhida de permanência na escola num dia:

$$ Q = \left\lfloor \frac{ H }{ D } \right\rfloor $$

Dada a quantidade de aulas, o máximo de turmas para retorno depende da disponibilidade de professores e salas. Cada professor acompanha somente 1 turma, e cada turma precisa de uma sala disponível para aula. Logo, com uma quantidade de salas disponíveis S e uma quantidade de professores que podem retornar **P**, a oferta possível de turmas **O** é dada pela fórmula:

$$ O = \min{ ( S \times Q, P ) } $$

Como cada turma pode ter até **K** alunos, a quantidade máxima de alunos que a rede é capaz de retornar num dia é dada por:

$$ C = K \times O $$
    
Note que a capacidade de atendimento da rede pode exceder o seu número convencional de alunos. Uma rede que oferece apenas uma aula por semana por aluno pode atender muito mais alunos do que uma rede operando de maneira convencional. Portanto, o número de alunos que de fato retornam **R** é o mínimo entre a quantidade de alunos que têm permissão para retornar **A** e a capacidade de retorno da rede C. Expresso como uma fórmula:

$$ R = \min{ ( A,C ) } $$

Assim, as quantidades respectivas de alunos e professores que de fato retornam são **R** e **P**.


### Como calculamos as quantidades de materiais?

O simulador usa valores de referência para determinar as quantidades de materiais de proteção e limpeza necessários. 

Note que as quantidades de materiais de uso individual (como máscaras e álcool em gel) dependem do tempo que cada indivíduo passa em aula. Por isso e outros motivos, o cálculo dos materiais de uso individual é feito de forma diferente para alunos e professores. Considere primeiro o caso dos alunos.

Com base no número de aulas por semana por aluno (N) e a duração de cada aula (D), é possível calcular o tempo semanal em aulas por aluno (TA).

$$ T_A = N \times D $$

Considerando o uso estimado de L litros de álcool em gel por hora por pessoa, a quantidade de álcool em gel necessária para os alunos (GA) é:

$$ G_A = R \times T_A \times L $$

Para determinar a quantidade de máscaras necessárias, o simulador leva em consideração a troca delas a cada E horas. Contudo, vale ressaltar que as aulas nem sempre são sequenciais. É possível que entre aulas o aluno seja obrigado a descartar a sua máscara por conta da validade. É prudente garantir ao aluno pelo menos uma máscara por aula. Assim, a quantidade de máscaras exigidas por alunos MA é dada por:

$$ M_A = R \times \max{ \left( N, \left\lceil{}  \frac{T_A}{E}  \right\rceil{} \right) }  $$

Com relação aos professores, o tempo semanal em aulas por professor TP  é dado por:

$$ T_P = \frac{ R \times T_A }{ K \times P } $$

Portanto, as quantidades sugeridas de álcool em gel para professores GP e de máscaras para professores MP são dadas por:

$$ G_P = P \times T_P \times L $$
$$ M_P =  P \times \left\lceil \frac{ T_P }{ E } \right\rceil  $$

No caso dos professores, não há a ressalva sobre garantir uma máscara por aula. Essa escolha provém da expectativa de que intervalos entre aulas de professores serão mais curtos. Nesse sentido, o aproveitamento das máscaras é maior. Contudo, a troca ainda deve ser observada a cada E horas. Com isso, as quantidade totais respectivas de álcool em gel GT  e de máscaras MT são

$$ G_T = G_A + G_P $$
$$ M_T = M_A + M_P $$

No caso de termômetros infravermelhos, é indicado um termômetro para cada 100 alunos. O simulador automaticamente realiza esse cálculo, arredondando para cima. 


### Como fazer a simulação?

O gestor passa como variáveis para o simulador o total de alunos que se deseja retornar **(A)**, o máximo de alunos em cada sala **(n)**, o número de professores disponíveis **(P)** e salas disponíveis **(S)**.

Calculamos a oferta de aulas pelo mínimo entre o número de professores e o total de salas disponíveis na semana, e o total de tempos de aula **(n)** disponíveis na semana:

$$ O = (n x 2) x min{S, P} $$

Para cada modelo de turno, temos uma quantidade de tempos de aula diferentes por semana:
- **Modelo baseado em horas**: alunos frequentam a escola todos os dias.
- **Modelo baseado em dias alternados**: turmas se alternam entre os dias da semana para frequentar a escola. Exemplo: Turma A frequenta a escola Segundas e Quartas, Turma B frequenta a escola Terças e Quintas.
- **Modelo baseado em dias consecutivos**: a quantidade de horas na escola é a mesma do modelo baseado em dias alternados, alterando apenas a alocação nos dias da semana. Exemplo: Turma A frequenta a escola Segundas e Terças, Turma B frequenta a escola Quartas e Quintas. 
- **Modelo baseado em semanas**: cada turma frequenta a escola por uma semana (todos os dias da semana), alternadamente. Exemplo: Turma A frequenta a escola na primeira semana, Turma B frequenta a escola na segunda semana, e assim sucessivamente.


### Tratamento dos dados do Censo Escolar - 2019
Utilizamos os dados do Censo Escolar 2019 como base para os cálculos padrão, mas o gestor pode alterar todas as variáveis de entrada no simulador para adequar à sua realidade. 
 
**Alunos:** O número de alunos é dado pela soma de quantidade de matrículas de cada turma única no Censo Escolar - 2019. Neste caso, a soma dos alunos de todas as turmas da rede ou município é igual ao total de alunos da rede ou município.
 
**Professores:** O número de professores é dado pela soma de professores únicos por etapa de ensino, rede e município. Ou seja:
    - A soma dos professores de todas as etapas da rede **não necessariamente** é igual ao total de professores da rede (um professor pode dar aula para mais de uma etapa)
    - A soma dos professores de todas as rede do município **não necessariamente** é igual ao total do município (um professor pode dar aula para mais de uma rede)

**Salas:** O número de salas é dado pela soma de salas existentes por escola por etapa de ensino, rede ou município. Ou seja:
    - A soma de salas de uma mesma rede para todas as etapas **não necessariamente** é igual ao total de salas da rede (uma escola pode oferecer mais de uma etapa)
    - A soma de salas de um mesmo município para todas as etapas **não necessariamente** é igual ao total de salas do município (uma escola pode oferecer mais de uma etapa)

**Filtros:** O filtro de escolas com água encanada restringe somente o número de salas pois assumimos ser possível realocar alunos para outras escolas próximas. 

Por outro lado, o filtro de localização (rural ou urbana) restringe tanto número de salas quanto professores e alunos por ser uma condição que não se limita à infraestrutura, mas também à região na qual alunos e professores se inserem ou são próximos.

**Considerações:** Não consideramos alunos EJA, professores de atividades complementares (somente tipo Docente) e turmas exclusivas especiais com base nos filtros do Censo para as Sinopses Estatísticas da Educação Básica.


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

### Como calculamos os números de alunos e professores retornando?

O simulador utiliza as informações: 

- $\bold{A}$: total de alunos x percentual de alunos que retornam
- $\bold{P}$: total de professores x percentual de professores que retornam
- $\bold{S}$: número de salas de aula disponíveis
- $\bold{K}$: máximo de alunos permitidos por sala 

Além dessas, são fixados valores para cada modelo de retorno:

- $\bold{H}$: horas disponíveis para aulas semanalmente ($H$ = 40 horas por semana)
- $\bold{D}$: duração de cada aula em horas ($D$ = 2 horas)
- $\bold{N}$: quantidade mínima de aulas por semana por aluno (equitativo: $N$ = 1; prioritário: $N$ = 5)

Para determinar quantos alunos a rede escolar é capaz de receber, utilizamos o conceito de **oportunidade**: uma oportunidade corresponde a um aluno assistir uma aula inteira. Como cada aula pode ter até $K$ alunos (máximo por turma), a **quantidade de oportunidades de aulas na rede** é dada por $K \times O$, onde $O$ corresponde à oferta total de aulas na rede.

A oferta de aulas na rede ($O$) depende diretamente da disponibilidade de professores e salas. Dado o total de horas disponíveis na semana ($H$) e a duração definida de uma aula ($D$), o máximo de aulas que podem ser oferecidas por professor/sala é dado por 

$$ Q = \left\lfloor \frac{ H }{ D } \right\rfloor $$

Assim, a oferta total de aulas é dada por:

$$ 
O = Q \times \min{ ( S, P ) } 
$$

Ao mesmo tempo, cada aluno deve ter uma quantidade $N$ de aulas por semana, que é dada pelo modelo de retorno escolhido. Assim, a capacidade efetiva de retorno de alunos($C$) é dada por:

$$
C = \frac{K \times O}{N}
$$

O número de alunos que de fato retornam $R$ depende da capacidade da rede de fornecer horários de aula dadas as restrições de professores, salas e turmas. Logo, $R$ é o mínimo entre a quantidade de alunos que têm permissão para retornar $A$ e a capacidade de retorno da rede $C$:

$$
R = \min{ ( A,C ) }
$$

E, finalmente, o número de professores que retornam é dado por $P$.

ℹ️ *Note que **a capacidade total da rede pode ser maior que o número de alunos que se deseja retornar**. Isso ocorre pois, uma vez selecionada a etapa de ensino, alocamos todos as 40 horas de professores/salas das escolas que possuem essa etapa.*

*Além disso, no modelo equitativo, no qual a rede oferece apenas uma aula por semana para cada aluno, esta pode atender muito mais alunos do que uma rede operando de maneira convencional.*

### Como calculamos as quantidades de materiais?

O simulador trabalha com as seguintes informações:

* $\bold{T_A}$: total de horas que cada aluno passa em aula na semana
* $\bold{T_P}$: total de horas que cada professor passa em aula na semana
* $\bold{G}$: litros de álcool em gel necessários
* $\bold{M}$: total de máscaras necessárias, considerando alunos e professores
* $\bold{M_A}$: total de mascáras necessárias, considerando apenas alunos
* $\bold{M_P}$: total de máscaras necessárias, considerando apenas professores
* $\bold{I}$: número de termômetros infravermelhos necessários

Além dessas informações, o simulador usa alguns valores de referência:

* $\bold{L}$: uso estimado de álcool em gel por pessoa por hora em litros ($L$ = 0.002 litros) 
* $\bold{U}$: limite de tempo para troca de máscara em horas ($U$ = 3 horas)
* $\bold{W}$: quantidade de pessoas que um termômetro é capaz de atender ($W$ = 100 pessoas)

As quantidades de materiais de uso individual (como máscaras e álcool em gel) dependem do tempo que cada indivíduo passa em aula. Portanto, o simulador contabiliza a quantidade de horas que alunos e professores passam na unidade escolar por semana. Tais valores podem ser encontrados através das seguintes fórmulas:

$$ 
T_A = N \times D
$$

$$
T_P = \frac{ R \times T_A }{ K \times P }
$$

A quantidade de álcool necessário, então, é dada por:

$$

G = L \times (R \times T_A + P \times T_P)

$$

Para determinar a quantidade de máscaras necessárias, o simulador leva em consideração a troca delas a cada $U$ horas. Contudo, vale ressaltar que as aulas nem sempre são sequenciais. É possível que entre aulas o aluno seja obrigado a descartar a sua máscara por conta da validade. É prudente garantir ao aluno pelo menos uma máscara por aula. Assim, a quantidade de máscaras exigidas por alunos $M_A$ é dada por:

$$
M_A = R \times \max{ \left( N, \left\lceil{}  \frac{T_A}{U}  \right\rceil{} \right) }
$$

No caso dos professores, não há a ressalva sobre garantir uma máscara por aula. Essa escolha provém da expectativa de que intervalos entre aulas de professores serão mais curtos. Contudo, a troca ainda deve ser observada a cada $U$ horas. Com isso, as quantidade de máscaras exigidas por professores $M_P$ é dada por:

$$
M_P =  P \times \left\lceil \frac{ T_P }{ U } \right\rceil
$$

Portanto, o total de máscaras necessárias pode ser obtido através da seguinte fórmula:

$$
M_T = M_A + M_P
$$

No caso de termômetros infravermelhos, é indicado um termômetro para cada $W$ alunos. Sendo assim, o simulador realiza o seguinte cálculo:

$$
I = \left\lceil \frac{R}{W} \right\rceil
$$
