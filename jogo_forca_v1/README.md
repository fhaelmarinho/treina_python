# Treina_Python (Jogo da Forca)
### Lista de Atividades e Desafios para Meus Alunos de Programação - Prof. Rafael Marinho

O jogo da forca é um jogo de adivinhação onde o jogador tenta adivinhar uma palavra, letra por letra, antes de cometer um número máximo de erros.

### Passo 1: Importar bibliotecas necessárias:
```
import random
```

__Explicação__: A biblioteca ```random``` será usada para escolher uma palavra aleatória de uma lista de palavras.

### Passo 2: Definir a lista de palavras
```
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
```
__Explicação__: Aqui definimos uma lista de palavras que serão usadas no jogo. O jogador terá que adivinhar uma dessas palavras.

### Passo 3: Escolher uma palavra aleatória da lista
```
palavra_secreta = random.choice(palavras)
```
__Explicação__: ```random.choice()``` seleciona uma palavra aleatória da lista ```palavras```, depois a variável ```palavra_secreta``` recebe a palavra selecionada.

### Passo 4: Inicializar variáveis
```
letras_corretas = ['_' for letra in palavra_secreta]
tentativas_restantes = 6
letras_erradas = []
```
 __Explicação__: 

```letras_corretas```: Inicializamos uma lista com underscores (```_```) para representar cada letra da palavra secreta. Conforme o jogador acerta as letras, os underscores serão substituídos pelas letras corretas.

```tentativas_restantes```: Definimos o número máximo de tentativas que o jogador pode errar antes de perder o jogo.

```letras_erradas```: Uma lista para armazenar as letras que o jogador já tentou e que não estão na palavra secreta.

### Passo 5: Loop principal do jogo
```
while tentativas_restantes > 0 and '_' in letras_corretas:
      print("\nPalavra: " + " ".join(letras_corretas))
      print("Letras erradas: " + ", ".join(letras_erradas))
      print(f"Tentativas restantes: {tentativas_restantes}")
      tentativa = input("Digite uma letra: ").lower()
```
__Explicação__: 

O loop continua enquanto o jogador ainda tem tentativas restantes e ainda há underscores na lista ```letras_corretas``` (ou seja, a palavra ainda não foi completamente adivinhada).

Mostramos a palavra atual com os underscores e as letras já adivinhadas.
Mostramos as letras que o jogador já tentou e que estão erradas.
Solicitamos ao jogador que digite uma letra.


### Passo 6: Verificar se a letra está na palavra secreta
    if tentativa in palavra_secreta:
        print("Letra correta!")
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                letras_corretas[i] = tentativa
    else:
        print("Letra errada!")
        letras_erradas.append(tentativa)
        tentativas_restantes -= 1

__Explicação__:

Se a letra digitada pelo jogador estiver na palavra secreta, atualizamos a lista ```letras_corretas``` para revelar a posição da letra na palavra.
Se a letra não estiver na palavra secreta, adicionamos a letra à lista ```letras_erradas``` e decrementamos o número de tentativas restantes.      

### Passo 7: Verificar se o jogador ganhou ou perdeu
```
if '_' not in letras_corretas:
    print("\nParabéns! Você ganhou! A palavra era: " + palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era: " + palavra_secreta)
```
__Explicação__:

Se não houver mais underscores na lista ```letras_corretas```, significa que o jogador adivinhou todas as letras e ganhou o jogo.
Caso contrário, o jogador perdeu e mostramos a palavra secreta.



    
