# Jogo de Adivinhação de Número

## Descrição do Programa

Este é um jogo de adivinhação onde o jogador tenta adivinhar um número aleatório gerado pelo computador. O número está entre 0 e 500, e o jogador recebe dicas se o palpite está muito alto ou muito baixo até acertar o número correto.

---

## Objetivos Educacionais

1. **Introdução à Programação**:
   - Este programa é um excelente exemplo para iniciantes em programação. Ele demonstra conceitos fundamentais como loops (`while`), condicionais (`if`, `elif`, `else`), e manipulação de variáveis.

2. **Desenvolvimento de Lógica de Programação**:
   - A implementação do jogo ensina como usar loops e condições para criar um fluxo de jogo interativo.

3. **Interação com o Usuário**:
   - O programa utiliza a função `input()` para capturar a entrada do usuário e fornece feedback em tempo real, ajudando a entender como criar interfaces de usuário simples.

4. **Uso de Bibliotecas**:
   - O programa utiliza a biblioteca `random` para gerar números aleatórios, introduzindo o conceito de bibliotecas e como elas podem ser usadas para adicionar funcionalidades ao código.

---

## Como Funciona o Programa

1. **Inicialização**:
   - O programa começa importando a biblioteca `random` e gerando um número aleatório entre 0 e 500.

2. **Loop de Adivinhação**:
   - O jogador é solicitado a adivinhar o número. O programa fornece feedback se o palpite está muito alto ou muito baixo.
   - O loop continua até que o jogador adivinhe o número correto.

3. **Contagem de Tentativas**:
   - O programa mantém um contador de tentativas e exibe o número de tentativas quando o jogador acerta o número.

---

## Instruções de Uso

### Requisitos
- Python 3.x instalado no seu computador.

### Execução
1. Clone ou baixe este repositório.
2. Abra o terminal ou prompt de comando e navegue até o diretório onde o arquivo `.py` está localizado.
3. Execute o programa usando o seguinte comando:
   ```bash
   python advinha_o_numero.py