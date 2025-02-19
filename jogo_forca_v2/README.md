## Passo a Passo do Jogo da Forca

### 1. **Importar a biblioteca `random`**
   - A biblioteca `random` é usada para escolher uma palavra aleatória da lista de palavras.

   ```python
   import random
   ```

---

### 2. **Definir a lista de palavras e as dicas**
   - Uma lista de palavras é criada para o jogo.
   - Um dicionário de dicas é definido, onde cada palavra está associada a uma dica correspondente.

   ```python
   palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]

   dicas = {
       "python": "Uma linguagem de programação popular.",
       "programacao": "O processo de escrever código para computadores.",
       "desenvolvimento": "Criação de software ou aplicativos.",
       "computador": "Uma máquina que processa informações.",
       "algoritmo": "Uma sequência de passos para resolver um problema."
   }
   ```

---

### 3. **Escolher uma palavra aleatória**
   - A função `random.choice` é usada para selecionar uma palavra aleatória da lista `palavras`.

   ```python
   palavra_secreta = random.choice(palavras)
   ```

---

### 4. **Inicializar variáveis do jogo**
   - `letras_corretas`: Uma lista que armazena as letras corretas adivinhadas pelo jogador. Inicialmente, contém underscores (`_`) para cada letra da palavra secreta.
   - `tentativas_restantes`: O número de tentativas que o jogador tem (inicialmente 6).
   - `letras_erradas`: Uma lista que armazena as letras incorretas já tentadas pelo jogador.

   ```python
   letras_corretas = ['_' for letra in palavra_secreta]
   tentativas_restantes = 6
   letras_erradas = []
   ```

---

### 5. **Definir a função para desenhar a forca**
   - A função `desenhar_forca` exibe o estado atual da forca com base no número de tentativas restantes.
   - Cada estágio da forca é representado por uma string ASCII art.

   ```python
   def desenhar_forca(tentativas_restantes):
       estagios = [
           # Estágios da forca (de 0 a 6 tentativas restantes)
       ]
       print(estagios[6 - tentativas_restantes])
   ```

---

### 6. **Mostrar a dica no início do jogo**
   - A dica correspondente à palavra secreta é exibida para ajudar o jogador.

   ```python
   print("Dica: " + dicas[palavra_secreta])
   ```

---

### 7. **Loop principal do jogo**
   - O jogo continua enquanto o jogador tiver tentativas restantes e ainda houver letras a serem adivinhadas (`_` em `letras_corretas`).

   ```python
   while tentativas_restantes > 0 and '_' in letras_corretas:
   ```

---

### 8. **Exibir o estado atual do jogo**
   - A forca é desenhada usando a função `desenhar_forca`.
   - A palavra atual (com letras adivinhadas e underscores) é exibida.
   - As letras erradas já tentadas são mostradas.
   - O número de tentativas restantes é exibido.

   ```python
   desenhar_forca(tentativas_restantes)
   print("\nPalavra: " + " ".join(letras_corretas))
   print("Letras erradas: " + ", ".join(letras_erradas))
   print(f"Tentativas restantes: {tentativas_restantes}")
   ```

---

### 9. **Solicitar uma tentativa do jogador**
   - O jogador digita uma letra.
   - A entrada é convertida para minúscula e validada:
     - Deve ser uma única letra.
     - Não pode ter sido tentada anteriormente.

   ```python
   tentativa = input("Digite uma letra: ").lower()
   ```

---

### 10. **Verificar se a letra está na palavra secreta**
   - Se a letra estiver na palavra secreta, ela é adicionada à lista `letras_corretas`.
   - Caso contrário, a letra é adicionada à lista `letras_erradas`, e o número de tentativas restantes é reduzido.

   ```python
   if tentativa in palavra_secreta:
       print("Letra correta!")
       for i, letra in enumerate(palavra_secreta):
           if letra == tentativa:
               letras_corretas[i] = tentativa
   else:
       print("Letra errada!")
       letras_erradas.append(tentativa)
       tentativas_restantes -= 1
   ```

---

### 11. **Verificar se o jogador ganhou ou perdeu**
   - Se não houver mais underscores (`_`) em `letras_corretas`, o jogador ganhou.
   - Caso contrário, se as tentativas acabarem, o jogador perdeu.

   ```python
   if '_' not in letras_corretas:
       print("\nParabéns! Você ganhou! A palavra era: " + palavra_secreta)
   else:
       print("\nVocê perdeu! A palavra era: " + palavra_secreta)
   ```

---

### Exemplo de Execução

#### Entrada:
   ```
   Digite uma letra: p
   Digite uma letra: y
   Digite uma letra: z
   ```

#### Saída:
   ```
   Dica: Uma linguagem de programação popular.
   Palavra: p _ _ _ _ _
   Letras erradas: z
   Tentativas restantes: 5
   ```

---

### Resumo do Fluxo do Jogo
1. Escolhe uma palavra aleatória e exibe a dica.
2. Inicializa as variáveis do jogo.
3. Entra em um loop onde o jogador tenta adivinhar letras.
4. Verifica se a letra está na palavra secreta e atualiza o estado do jogo.
5. Exibe o resultado final (vitória ou derrota).

