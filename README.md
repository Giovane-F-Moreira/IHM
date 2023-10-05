# IHM

<table><tr><th colspan="1" rowspan="4" valign="top"></th><th colspan="1">DISCIPLINA</th><th colspan="1"><b>INTERFACE HOMEM-MÁQUINA</b></th></tr>
<tr><td colspan="1" valign="top">Nota máxima</td><td colspan="1" valign="top"><b>10 Pontos</b></td></tr>
<tr><td colspan="1" valign="top">Professor</td><td colspan="1" valign="top"><b>Luis Paulo da Silva Carvalho</b></td></tr>
<tr><td colspan="1">Data de entrega</td><td colspan="1"><b>01/11/2023</b></td></tr>
</table>

1. I**ntrodução** 

Este trabalho destina-se a avaliar os alunos da disciplina de  **INTERFACE HOMEM MÁQUINA** em relação ao conteúdo e práticas compreendidos em sala de aula. Especificamente, deve ser criado um SISTEMA SENSÍVEL A CONTEXTO (SSC), contemplando duas  etapas:  (1)  desenvolvimento  de  uma  simulação  baseada  em  um  mini-mundo;  e  (2)  criação  de  features  de  orientação  a comportamento (BDD) considerando a simulação feita na etapa 1.

2. **Escopo do trabalho**

O  trabalho  deve  ser  realizado INDIVIDUALMENTE.  Ele  consiste  na  concretização  de  um  SSC,  escrito  em  linguagem  de programação PYTHON, devendo estar restrito aos conteúdos teóricos e práticos vistos durante as aulas.

3. **Instruções**

As seguintes instruções devem ser atentamente observadas e cumpridas:

1. **ETAPA 1**

\1.  O aluno deve escolher o tema do seu trabalho e enviar para o meu e-mail (luispscarvalho@gmail\.com) sua decisão o 

quanto  antes  e  até  o  dia  11/10/2023.  A  partir  daí  deverei  acompanhar  o  andamento  dos  trabalhos.  O acompanhamento visa identificar e resolver possíveis problemas e dificuldades de desenvolvimento;

\2.  Ainda aceitarei a escolha de um tema após o dia 11/10/2023, todavia, já no dia 12/10/2023 (um dia após o prazo final 

para definição do tema) será descontado 1.0 (um ponto) da nota total e, para cada dia após 12/10/2023, serão descontados 0.5 pontos da nota final; 

\3.  De  forma  alguma  o  mini-mundo  desenvolvido  por  mim  em  sala  de  aula,  SOCORRO  INTELIGENTE,  poderá  ser 

reutilizado para realizar o seu trabalho;

\4.  Não será permitida a repetição de um tema\. Ou seja, a avaliação consistirá da escolha de um tema por cada trabalho 

a ser apresentado. À medida que os temas forem enviados para mim eu realizarei o controle para garantir a não repetição e exigirei um tema novo, caso o escolhido já tenha sido selecionado anteriormente por algum outro aluno. Desta forma, quanto mais cedo um tema for definido e comunicado para mim através do meu e-mail menor deve ser a probabilidade de redefinição ou escolha de outro tema;

\5.  O SSC deve ser construído utilizando os recursos apresentados e exemplificados durante as aulas: linguagem de 

programação PYTHON e bibliotecas de suporte a reconhecimento facial (face\_recognition e  opencv) e simulações (simpy). **Tais bibliotecas e frameworks são obrigatórios**. Todavia, se quiser e achar necessário, o aluno pode adicionar outras bibliotecas e frameworks para que possam automatizar melhor sua solução;

\6.  Depois de criar a simulação, o aluno deverá realizar uma captura de vídeo para explicar o tema e o funcionamento da 

simulação. O vídeo deverá ser entregue para mim. O vídeo pode ser enviado para o youtube ou para o google drive. O link para o vídeo deve ser testado para verificar se é possível alguém realizar acesso externo a ele;

\7.  Para  cada  tema  deve  ser  definido  um  arquivo  de  configuração,  na  forma  de  um  dicionário  externo  JSON, 

possibilitando a configuração e execução da simulação;

\8.  A simulação deverá ser composta de, pelo  menos, quatro  processos independentes (criados como geradores de 

evento), sendo que um desses processos deve ser baseado em reconhecimento de face;

\9.  **ATENÇÃO: Devem servir como base os scripts PYTHON exemplificados em sala de aula e não os dos vídeos**\. Trata-

se de uma medida para evitar que a biblioteca de reconhecimento de faces seja utilizada para reconhecer uma face por vez. O aceitável é ela ser usada para reconhecer mais de uma face por cada imagem.



<table><tr><th colspan="1" rowspan="4"></th><th colspan="1">DISCIPLINA</th><th colspan="1"><b>INTERFACE HOMEM-MÁQUINA</b></th></tr>
<tr><td colspan="1" valign="top">Nota máxima</td><td colspan="1" valign="top"><b>10 Pontos</b></td></tr>
<tr><td colspan="1" valign="top">Professor</td><td colspan="1" valign="top"><b>Luis Paulo da Silva Carvalho</b></td></tr>
<tr><td colspan="1">Data de entrega</td><td colspan="1"><b>01/11/2023</b></td></tr>
</table>

2. **ETAPA 2**

\1.  Uma  segunda  versão  do  SSC  deve  ser  criada  aproveitando  o  código-fonte  da  primeira  versão  (ETAPA  1)  para 

mostrar a aplicação de Desenvolvimento Orientado a Comportamento (BDD);

\2.  Nesta segunda etapa, é esperado que cada uma das funcionalidades principais do SSC tenha um arquivo de feature 

associado e passos, steps, criados para executar as features; 

\3.  Deve  ser  utilizado  o  framework  PYTHON,  Behave,  para  definir  e  automatizar  a  aplicação  da  Orientação  a 

Comportamento; 

\4.  Depois de recriar o SSC utilizando os recursos de BDD, o aluno deverá realizar uma captura de vídeo para explicar o 

tema e o funcionamento. O vídeo deverá ser entregue para mim. O vídeo pode ser enviado para o youtube ou para o google drive. O link para o vídeo deve ser testado para verificar se é possível alguém realizar acesso externo a ele;

\5.  Todos os processos definidos e criados durante a ETAPA 1 deverão ser adaptados como features executáveis, o que 

inclui o reconhecimento de face.

3. **INSTRUÇÕES PARA AS ETAPAS 1 E 2**

\1.  Os projetos PYTHON das ETAPAS 1 e 2 devem ser entregues em arquivos (\.zip) separados\. Isso tornará possível 

que eu avalie cada etapa de forma independente. Cada entrega deve conter: os scripts PY, as configurações JSON, o arquivo  REQUIREMENTS.TXT  com  as  dependências  e  quaisquer  outros  arquivos  necessários  para  executar  os scripts;

\2.  Só avaliarei a ETAPA 2 se a ETAPA 1 for entregue;

\3.  A ETAPA 1 deve ser entregue antes da ETAPA 2 e não o contrário;

\4.  Você pode (ou DEVE) iniciar a criação da simulação (ETAPA 1) logo agora\. Não é necessário esperar as aulas sobre 

BDD (ETAPA 2) para iniciar a implementação;

\5.  Somente oferecerei suporte, em forma de atendimentos, até o dia 25/10/2023\. Isso evitará que eu tenha que atender 

a muitas demandas de alunos retardatários, que atrasam demais o desenvolvimento das simulações apesar de todos os avisos dados em sala de aula.

4. **ITENS A SEREM ENTREGUES/REALIZADOS** 
1. O tema que será desenvolvido. O aluno deverá propor o tema, mas eu deverei aprová-lo (envie a proposta para o meu email: luispscarvalho@gmail.com);
1. O código-fonte da simulação do SSC escrito em linguagem PYTHON (ETAPA 1);

O código-fonte da versão Orientada a Comportamento do SSC também escrito em PYTHON (ETAPA 2);

3. Os vídeos das etapas 1 e 2.
4. **Barema**

O cálculo da nota da avaliação obedecerá aos seguintes critérios:



<table><tr><th colspan="1" rowspan="4"></th><th colspan="1">DISCIPLINA</th><th colspan="1"><b>INTERFACE HOMEM-MÁQUINA</b></th></tr>
<tr><td colspan="1" valign="top">Nota máxima</td><td colspan="1" valign="top"><b>10 Pontos</b></td></tr>
<tr><td colspan="1" valign="top">Professor</td><td colspan="1" valign="top"><b>Luis Paulo da Silva Carvalho</b></td></tr>
<tr><td colspan="1">Data de entrega</td><td colspan="1"><b>01/11/2023</b></td></tr>
</table>



|NOTA DA AVALIAÇÃO||
| - | :- |
|ETAPA 1|VALOR|
|(a) Código-fonte **funcionando**|8|
|(b) Vídeo de apresentação|2|
|ETAPA 2|VALOR|
|(a) Código-fonte **funcionando**|8|
|(b) Vídeo de apresentação|2|
|TOTAL (ETAPA 1 + ETAPA2 / 2)|10|

**ATENÇÃO**: A ocorrência de plágio (cópia de outros trabalhos) será punida, com o aluno obtendo uma nota ZERO. A ocorrência também será notificada à coordenação do curso.
