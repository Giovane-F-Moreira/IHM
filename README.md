# Identify criminal

<!---Esses são exemplos. Veja https://shields.io para outras pessoas ou para personalizar este conjunto de escudos. Você pode querer incluir dependências, status do projeto e informações de licença aqui--->

![GitHub repo size](https://img.shields.io/github/repo-size/Giovane-F-Moreira/IHM)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/Giovane-F-Moreira/IHM)
![Lines of code](https://tokei.rs/b1/github/Giovane-F-Moreira/IHM)
![GitHub language count](https://img.shields.io/github/languages/count/Giovane-F-Moreira/IHM)
![GitHub top language](https://img.shields.io/github/languages/top/Giovane-F-Moreira/IHM)
![GitHub last commit](https://img.shields.io/github/last-commit/Giovane-F-Moreira/IHM)
![GitHub forks](https://img.shields.io/github/forks/Giovane-F-Moreira/IHM)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/Giovane-F-Moreira/IHM)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/Giovane-F-Moreira/IHM)
![GitHub followers](https://img.shields.io/github/followers/Giovane-F-Moreira?label=Follow)

<img src="https://img.freepik.com/premium-vector/face-recognition-low-poly-wireframe-banner-template-futuristic-computer-technology-smart-identification-system-poster-polygonal-design-facial-scan-3d-mesh-art-with-connected-dots_201274-4.jpg" alt="face-recognition">

> Este projeto é uma atividade avaliativa da materia Interface Homem e Maquina.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [X] Desenvolver reconhecimento de face
- [ ] Desenvolver simulação
- [ ] Desenvolver BDD
- [ ] Desenvolver Frontend

## 💻 Pré-requisitos

<details>
  <summary><h3>Requisitos para construção do software</h3></summary>

<details>
      <summary>Introdução</summary>
  Este trabalho destina-se a avaliar os alunos da disciplina de  **INTERFACE HOMEM MÁQUINA** em relação ao conteúdo e práticas compreendidos em sala de aula. Especificamente, deve ser criado um SISTEMA SENSÍVEL A CONTEXTO (SSC), contemplando duas  etapas:  (1)  desenvolvimento  de  uma  simulação  baseada  em  um  mini-mundo;  e  (2)  criação  de  features  de  orientação  a comportamento (BDD) considerando a simulação feita na etapa 1.

</details>

<details>
    <summary> Etapa 1 </summary>
\1.  O aluno deve escolher o tema do seu trabalho

\2.  O SSC deve ser construído utilizando os recursos apresentados e exemplificados durante as aulas: linguagem de

programação PYTHON e bibliotecas de suporte a reconhecimento facial (face\_recognition e  opencv) e simulações (simpy). **Tais bibliotecas e frameworks são obrigatórios**. Todavia, se quiser e achar necessário, o aluno pode adicionar outras bibliotecas e frameworks para que possam automatizar melhor sua solução;

\3.  Depois de criar a simulação, o aluno deverá realizar uma captura de vídeo para explicar o tema e o funcionamento da

simulação. O vídeo deverá ser entregue. O vídeo pode ser enviado para o youtube ou para o google drive. O link para o vídeo deve ser testado para verificar se é possível alguém realizar acesso externo a ele;

\4.  Para  cada  tema  deve  ser  definido  um  arquivo  de  configuração,  na  forma  de  um  dicionário  externo  JSON,

possibilitando a configuração e execução da simulação;

\5.  A simulação deverá ser composta de, pelo  menos, quatro  processos independentes (criados como geradores de

evento), sendo que um desses processos deve ser baseado em reconhecimento de face;

\6.  **ATENÇÃO: Devem servir como base os scripts PYTHON exemplificados em sala de aula e não os dos vídeos**\. Trata-

se de uma medida para evitar que a biblioteca de reconhecimento de faces seja utilizada para reconhecer uma face por vez. O aceitável é ela ser usada para reconhecer mais de uma face por cada imagem.

</details>

<details>
  <summary> ETAPA 2</summary>
\1.  Uma  segunda  versão  do  SSC  deve  ser  criada  aproveitando  o  código-fonte  da  primeira  versão  (ETAPA  1)  para

mostrar a aplicação de Desenvolvimento Orientado a Comportamento (BDD);

\2.  Nesta segunda etapa, é esperado que cada uma das funcionalidades principais do SSC tenha um arquivo de feature

associado e passos, steps, criados para executar as features;

\3.  Deve  ser  utilizado  o  framework  PYTHON,  Behave,  para  definir  e  automatizar  a  aplicação  da  Orientação  a

Comportamento;

\4.  Depois de recriar o SSC utilizando os recursos de BDD, o aluno deverá realizar uma captura de vídeo para explicar o

tema e o funcionamento. O vídeo deverá ser entregue. O vídeo pode ser enviado para o youtube ou para o google drive. O link para o vídeo deve ser testado para verificar se é possível alguém realizar acesso externo a ele;

\5.  Todos os processos definidos e criados durante a ETAPA 1 deverão ser adaptados como features executáveis, o que

inclui o reconhecimento de face.

</details>

<details>
<summary><b>INSTRUÇÕES PARA AS ETAPAS 1 E 2</b></summary>

\1.  Os projetos PYTHON das ETAPAS 1 e 2 devem ser entregues em arquivos (\.zip) separados\. Isso tornará possível

que eu avalie cada etapa de forma independente. Cada entrega deve conter: os scripts PY, as configurações JSON, o arquivo  REQUIREMENTS.TXT  com  as  dependências  e  quaisquer  outros  arquivos  necessários  para  executar  os scripts;

\2.  Só avaliarei a ETAPA 2 se a ETAPA 1 for entregue;

\3.  A ETAPA 1 deve ser entregue antes da ETAPA 2 e não o contrário;

\4.  Você pode (ou DEVE) iniciar a criação da simulação (ETAPA 1) logo agora\. Não é necessário esperar as aulas sobre

BDD (ETAPA 2) para iniciar a implementação;

</details>

</details>

### Requisitos para execução do software

Software construido e **TESTADO** com as seguintes tecnologias:

Ubuntu 20.04    
Python 3.8.10   
face-recognition==1.3.0         
face-recognition-models==0.3.0     
opencv-python==4.8.0.76     
simpy==4.0.2

Instale as dependencias com comando:

```
sudo pip3 install -r requirements.txt
```

<!--Antes de começar, verifique se você atendeu aos seguintes requisitos:
-Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->

<!---* Você instalou a versão mais recente de `<linguagem / dependência / requeridos>`
* Você tem uma máquina `<Windows / Linux / Mac>`. Indique qual sistema operacional é compatível / não compatível.
* Você leu `<guia / link / documentação_relacionada_ao_projeto>`.--->

<!---## ☕ Instalando Geekflix

Para instalar o Geekflix, siga estas etapas:

Linux e macOS:
```
<comando_de_instalação>
```

Windows:
```
<comando_de_instalação>
```
--->

## 🚀 Utilizando o Identify criminal

Para utilizar o Identify criminal, siga estas etapas:

1 - Para utilizar o projeto basta ter o **Visual Studio Code**.  `<br><br>`
  1.1 - Intalando VS Code: https://www.youtube.com/watch?v=49K-Zxc8A7A  \

2 - Exxecute o arquivo principal no terminal

```
python3 autorizador_facial.py
```

## 📫 Contribuindo para Identify criminal

<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->

Para contribuir com Geekflix, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/64364499?v=4" width="100px;" alt="Foto do Giovane Fernandes no GitHub"/><br>
        <sub>
          <b>Giovane Fernandes</b>
        </sub>
        </hr>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <sub>
        <b>Criador do Projeto</b>
      </sub>
    </td>
  </tr>
</table>

## 😄 Seja um dos contribuidores`<br>`

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#nome-do-projeto)`<br>`
