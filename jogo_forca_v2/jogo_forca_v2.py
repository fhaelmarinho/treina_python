import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]

# Dicas para cada palavra
dicas = {
    "python": "Uma linguagem de programação popular.",
    "programacao": "O processo de escrever código para computadores.",
    "desenvolvimento": "Criação de software ou aplicativos.",
    "computador": "Uma máquina que processa informações.",
    "algoritmo": "Uma sequência de passos para resolver um problema."
}

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Inicializar variáveis
letras_corretas = ['_' for letra in palavra_secreta]
tentativas_restantes = 6
letras_erradas = []

# Função para desenhar a forca
def desenhar_forca(tentativas_restantes):
    estagios = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    print(estagios[6 - tentativas_restantes])

# Mostrar a dica no início do jogo
print("Dica: " + dicas[palavra_secreta])

# Loop principal do jogo
while tentativas_restantes > 0 and '_' in letras_corretas:
    desenhar_forca(tentativas_restantes)
    print("\nPalavra: " + " ".join(letras_corretas))
    print("Letras erradas: " + ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Solicitar uma tentativa do jogador
    tentativa = input("Digite uma letra: ").lower()
    
    # Validar a entrada
    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Por favor, insira apenas uma letra válida.")
        continue
    if tentativa in letras_corretas or tentativa in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue
    
    # Verificar se a letra está na palavra secreta
    if tentativa in palavra_secreta:
        print("Letra correta!")
        for i, letra in enumerate(palavra_secreta):
            if letra == tentativa:
                letras_corretas[i] = tentativa
    else:
        print("Letra errada!")
        letras_erradas.append(tentativa)
        tentativas_restantes -= 1

# Verificar se o jogador ganhou ou perdeu
if '_' not in letras_corretas:
    print("\nParabéns! Você ganhou! A palavra era: " + palavra_secreta)
else:
    print("\nVocê perdeu! A palavra era: " + palavra_secreta)