## Metodologia de Simule o Retorno

### O que é?

O simulador é uma ferramenta de cálculo para o gestor planejar o retorno das atividades escolares definindo restrições e seguindo os protocolos sanitários indicados. 

A partir dos valores e restrições inseridos pelo gestor, o simulador calcula o **número de alunos e professores que podem retornar** às atividades escolares e **os materiais necessários para compra**, incluindo máscaras descartáveis, termômetros e
litros de álcool em gel (mais materiais podem ser acessados na planilha que disponibilizamos).

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

A oferta de aulas na rede ($O$) depende diretamente da disponibilidade de professores e salas. Dado o total de horas disponíveis na semana ($H$) e a duração definida de uma aula ($D$), o máximo de aulas que podem ser oferecidas por professor/sala é dado por $Q = \left\lfloor \frac{ H }{ D } \right\rfloor$.

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