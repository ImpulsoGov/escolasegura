
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


### Como fazer a simulação?

Ao acessar a ferramenta, o gestor encontrará os seguintes campos para preenchimento:

- **Total de alunos:** O gestor pode informar aqui o número total de alunos 
inscritos no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

- **Total de professores:** O gestor pode informar aqui o número de professores disponíveis 
para dar aula no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

- **Total de salas de aula:** O gestor pode informar aqui o total de salas de aula disponíveis 
para retorno no sistema local de ensino. *Por padrão, fornecemos esse valor com base no Censo Escolar 2019.*

- **Número máximo de alunos por sala:** O usuário fornece o limite de alunos por sala determinado pelo gestor a fim de limitar a transmissibilidade da doença.

- **Número de horas presenciais diárias na escola por turma:**  Os modelos indicam a quantidade de horas de aula no dia de cada turma (ex: um modelo total presencial teria 5 horas de aula enquanto um modelo híbrido teria uma carga reduzida, de 3 horas), porém o usúario também pode altera-lo.

O gestor deve informar aqui o percentual de professores 
dentre o **Total de professores** indicado que estão previstos para retornar as atividades.

- **Máximo de alunos por sala:** 
O gestor deve indicar aqui o limite de alunos por sala de aula. 
Por padrão, este valor é de 20 alunos por sala, que também é o máximo que permitimos ser escolhido a fim tentar limitar a transmissão da doença.

- **Modelo de retorno:** O usuário pode escolher os seguintes modelos de retorno:
  - **Modelo:** Totalmente presencial
    - **Descrição:** Neste modelo, todos os estudantes retornam às aulas presenciais como antes, com os mesmos horários em sala de aula, porém seguindo os novos protocolos de distanciamento e segurança sanitária.
  - **Modelo:** Híbrido: Aulas expositivas presenciais + tarefas para casa
    - **Descrição:** Nos modelos híbridos todos os estudantes retornam às aulas presenciais por tempo reduzido na escola e têm parte das aulas remotas. Em especial, neste modelo professores(as) transmitem conceitos para os estudantes presencialmente, e os estudantes completam exercícios e tarefas em casa.
  - **Modelo:** Híbrido: Aulas gravadas em vídeo + tarefas presenciais
    - **Descrição:** Nos modelos híbridos todos os estudantes retornam às aulas presenciais por tempo reduzido na escola e têm parte das aulas remotas. Em especial, neste modelo estudantes aprendem novos conceitos de forma remota e concluem exercícios e tarefas presencialmente com o(a) professor(a).
  - **Modelo:** Prioritário: Aulas síncronas por vídeo com parte de estudantes em sala e parte em casa (grupo dividido)
    - **Descrição:** Neste modelo, os professores têm uma aula normal completa com um grupo de estudantes presencial, enquanto outro grupo acompanha remotamente por meio de videoconferência (VC).

### Tratamento dos dados do Censo Escolar - 2019
Utilizamos os dados do Censo Escolar 2019 como base para os cálculos padrão, mas o gestor pode alterar todas as variáveis de entrada no simulador para adequar à sua realidade. 
 
**Alunos:** O número de alunos é dado pela soma de quantidade de matrículas de cada turma única no Censo Escolar - 2019. Neste caso, a soma dos alunos de todas as turmas da rede ou município é igual ao total de alunos da rede ou município.
 
**Professores:** O número de professores é dado pela soma de professores únicos por etapa de ensino, rede e município. Ou seja:
    - A soma dos professores de todas as etapas da rede **não necessariamente** é igual ao total de professores da rede (um professor pode dar aula para mais de uma etapa)
    - A soma dos professores de todas as rede do município **não necessariamente** é igual ao total do município (um professor pode dar aula para mais de uma rede)

**Salas:** O número de salas é dado pela soma de salas existentes por escola por etapa de ensino, rede ou município. Ou seja:
    - A soma de salas de uma mesma rede para todas as etapas **não necessariamente** é igual ao total de salas da rede (uma escola pode oferecer mais de uma etapa)
    - A soma de salas de um mesmo município para todas as etapas **não necessariamente** é igual ao total de salas do município (uma escola pode oferecer mais de uma etapa)

**Considerações:** Não consideramos alunos EJA, professores de atividades complementares (somente tipo Docente) e turmas exclusivas especiais com base nos filtros do Censo para as Sinopses Estatísticas da Educação Básica.


### Como calculamos os números de alunos e professores retornando?

O simulador utiliza as informações: 
- $\bold{N_a}$: número de alunos autorizados a retornar à escola.
- $\bold{N_p}$: número de professores autorizados a voltar à escola.
- $\bold{N_s}$: número de salas de aula disponíveis.
- $\bold{horas_de_aula_por_turma}$: duração do tempo em aula por dia (definido por modelo ou usuário).
- $\bold{max_alunos_por_sala}$: máximo de alunos permitidos por sala.


Além dessas, são fixados valores para os modelos:
- $\bold{max_professores_por_turma}$: máximo de professores por turma.
- $\bold{horas_possiveis_sala}$: total de horas disponíveis para aulas em um dia. Padrão: 10 = 5 horas x 2 turnos (manhã / tarde).


Depois calcula o máximo de turmas de acordo com a quantidade de alunos, professores e salas possíveis:

Máximo por alunos.
$$ M_a = \frac{N_a}{max_alunos_por_sala} $$

Máximo por professores.
$$ M_p = N_p \times max_professores_por_turma $$

Máximo por salas.
$$ M_s = \frac{horas_possiveis_sala \times N_s}{horas_de_aula_por_turma} $$


Identifica o máximo de turmas:

$$\bold{R}$$ [maximo_de_turmas] $$= \min{(M_a, M_p, M_s)}$$


Dado o máximo de turmas, retorna o número de professores e alunos que podem voltar:
- $\bold{A}$ [total de alunos que retornam]: máximo de turmas x máximo de alunos por sala ($\bold{K}$)
- $\bold{P}$ [total de professrores que retornam]: máximo de turmas x máximo de professores por turma (fixado em 1)


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
