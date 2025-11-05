# DESENVOLVIMENTO DE UM COMPILADOR BÁSICO EM PYTHON: IMPLEMENTAÇÃO DE ANÁLISE LÉXICA, SINTÁTICA E EXECUÇÃO INTERPRETADA

Thales Marques Coelho
Unic Beira Rio

**Palavras-chave:** compilador; análise léxica; Python; interpretação; linguagem simples

---

## 1. Introdução

### 1.1 Apresentação do Tema e Relevância

O desenvolvimento de compiladores representa um dos pilares da Ciência da Computação, pois permite compreender como linguagens de programação são transformadas em instruções executáveis. Criar um compilador, mesmo simples, fornece uma visão prática de como ocorrem as etapas de tradução de código-fonte para execução, envolvendo análise léxica, sintática e semântica.

Este trabalho apresenta o desenvolvimento de um compilador básico em Python, projetado para interpretar uma linguagem simples com operações matemáticas, variáveis e comandos de impressão. O projeto tem caráter educacional, proporcionando aos alunos uma compreensão prática do funcionamento interno de compiladores sem a necessidade de ferramentas complexas.

### 1.2 Definição do Problema de Pesquisa

O problema central deste estudo é: como implementar um compilador simples capaz de analisar e executar instruções escritas em uma linguagem criada pelo desenvolvedor?
Para isso, o compilador deve realizar a análise do código-fonte, interpretar os comandos e produzir resultados de forma automática.

A proposta é criar uma linguagem minimalista que permita operações aritméticas e atribuição de variáveis, sendo executada por um interpretador desenvolvido inteiramente em Python.

---

## 2. Objetivos

**Objetivo Geral**

Desenvolver um compilador básico em Python que realize as etapas fundamentais da compilação: análise léxica, análise sintática e execução interpretada do código.

**Objetivos Específicos**

* Implementar um analisador léxico para separar o código em tokens;
* Criar um analisador sintático simples para interpretar expressões e comandos;
* Desenvolver uma estrutura de execução para avaliar expressões e variáveis;
* Implementar suporte a comandos de impressão (print) e atribuição;
* Validar o compilador com exemplos práticos de código.

---

## 3. Metodologia

O trabalho caracteriza-se como pesquisa experimental aplicada, pois envolve a implementação prática de um sistema de software (compilador) com base em conceitos teóricos de compiladores e linguagens formais.

O compilador foi implementado em Python, linguagem escolhida por sua clareza sintática e ampla disponibilidade de bibliotecas para manipulação de texto. A metodologia seguiu as seguintes etapas:

* **Análise léxica:** Utilização de expressões regulares para identificar palavras-chave, números, identificadores e operadores.
* **Análise sintática:** Interpretação linha a linha do código-fonte, reconhecendo padrões de atribuição e comandos print.
* **Execução:** As expressões são avaliadas usando o interpretador interno do Python (eval), simulando a execução do código compilado.

O código principal foi dividido em funções:

* `lexer(codigo)`: separa o texto em tokens;
* `avaliar_expressao(expr)`: calcula expressões aritméticas;
* `executar(codigo)`: processa e executa o programa linha por linha.

---

## 4. Resultados

O compilador foi testado com o seguinte exemplo de código-fonte:

```python
x = 10
y = 20
z = x + y * 2
print(z)
print(z / 5)