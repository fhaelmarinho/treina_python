import random

# Lista de palavras para o jogo
palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]

# Escolher uma palavra aleatória
palavra_secreta = random.choice(palavras)

# Inicializar variáveis
letras_corretas = ['_' for letra in palavra_secreta]
tentativas_restantes = 6
letras_erradas = []

# Loop principal do jogo
while tentativas_restantes > 0 and '_' in letras_corretas:
    print("\nPalavra: " + " ".join(letras_corretas))
    print("Letras erradas: " + ", ".join(letras_erradas))
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Solicitar uma tentativa do jogador
    tentativa = input("Digite uma letra: ").lower()
    
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

# Tente agora implementar uma interface para exibir os erros e acertos
