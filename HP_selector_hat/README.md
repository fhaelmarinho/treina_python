
# **Sorting Hat Quiz - Hogwarts House Selector**

## **Descrição do Programa**

Este programa é uma simulação simples do Chapéu Seletor de Hogwarts, famoso no universo de Harry Potter. O objetivo é ajudar os usuários a descobrir qual seria sua casa em Hogwarts (Grifinória, Corvinal, Lufa-Lufa ou Sonserina) com base nas respostas fornecidas a um conjunto de perguntas. 

O programa utiliza uma lógica de pontuação para calcular qual casa melhor se alinha às escolhas do usuário. Ao final, ele exibe os resultados e informa a casa correspondente ao perfil do usuário.

---

## **Objetivos Educacionais**

1. **Introdução à Programação**:
   - Este programa serve como um excelente exemplo prático para quem está aprendendo Python. Ele demonstra conceitos fundamentais, como entrada de dados (`input()`), estruturas condicionais (`if`, `elif`, `else`) e manipulação de variáveis.

2. **Desenvolvimento de Lógica de Programação**:
   - A implementação do sistema de pontuação ensina como usar condições e operadores lógicos para criar fluxos de decisão em programas.

3. **Prática de Interface de Usuário Simples**:
   - O programa apresenta uma interface textual interativa, onde o usuário responde perguntas sequenciais. Isso ajuda a entender como projetar interfaces básicas para interação com o usuário.

4. **Tratamento de Entradas Inválidas**:
   - O programa inclui tratamento básico para entradas inválidas, mostrando como lidar com erros de entrada sem interromper o fluxo do programa.

5. **Engajamento com Temas Populares**:
   - Utilizando o universo de Harry Potter, o programa torna o aprendizado mais envolvente e divertido, especialmente para iniciantes em programação.

---

## **Como Funciona o Programa**

1. **Inicialização**:
   - O programa começa inicializando as variáveis de pontuação para cada casa: Grifinória (`gryffindor`), Corvinal (`ravenclaw`), Lufa-Lufa (`hufflepuff`) e Sonserina (`slytherin`), todas começam com zero pontos.

2. **Perguntas Interativas**:
   - O usuário responde a três perguntas, cada uma com opções numéricas pré-definidas. Cada resposta adiciona pontos a uma ou mais casas, dependendo da escolha do usuário.

3. **Cálculo da Casa Final**:
   - Após responder todas as perguntas, o programa calcula qual casa tem a maior pontuação. Se houver empate, todas as casas empatadas serão exibidas.

4. **Exibição dos Resultados**:
   - O programa exibe a pontuação final de cada casa e informa ao usuário sua "casa selecionada" com base na pontuação.

---

## **Instruções de Uso**

### **Requisitos**
- Python 3.x instalado no seu computador.

### **Execução**
1. Clone ou baixe este repositório.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `.py` está localizado.
3. Execute o programa usando o seguinte comando:
   ```bash
   python nome_do_arquivo.py
   ```
4. Responda às perguntas digitando o número correspondente à sua escolha e pressionando `Enter`.

### **Exemplo de Execução**
```
[Q1] Do you like Dawn or Dusk?
    [1] Dawn
    [2] Dusk
    Enter your answer (1-2): 1

[Q2] When I’m dead, I want people to remember me as:
    [1] The Good
    [2] The Great
    [3] The Wise
    [4] The Bold
    Enter your answer (1-4): 4

[Q3] Which kind of instrument most pleases your ear?
    [1] The violin
    [2] The trumpet
    [3] The piano
    [4] The drum
    Enter your answer (1-4): 4

Final Scores:
🦁 Gryffindor: 7
🦅 Ravenclaw: 1
🦡 Hufflepuff: 1
🐍 Slytherin: 1

Your house is:
🦁 Gryffindor
```

---

## **Estrutura do Código**

O código está organizado da seguinte forma:

1. **Inicialização de Variáveis**:
   - As variáveis `gryffindor`, `ravenclaw`, `hufflepuff` e `slytherin` armazenam as pontuações das casas.

2. **Perguntas e Respostas**:
   - Cada pergunta usa `input()` para capturar a resposta do usuário e atualiza as pontuações com base nas escolhas.

3. **Cálculo e Exibição dos Resultados**:
   - O programa calcula a pontuação máxima e exibe a(s) casa(s) correspondente(s).

---

## **Contribuições**

Se você deseja contribuir para este projeto, fique à vontade para abrir uma issue ou enviar um pull request. Sugestões de melhorias incluem:

- Adicionar mais perguntas para tornar o quiz mais detalhado.
- Implementar uma interface gráfica (GUI) usando bibliotecas como Tkinter ou Pygame.
- Traduzir o programa para outros idiomas.

---

## **Licença**

Este projeto está licenciado sob a **MIT License**, o que significa que você pode usá-lo, modificá-lo e distribuí-lo livremente.

