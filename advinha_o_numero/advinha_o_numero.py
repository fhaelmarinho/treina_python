import random

numero_correto = random.randint(0, 500)
tentativa = 0
numero = 0

while numero != numero_correto:
    numero = int(input("Chute um número: "))
    tentativa += 1
    if numero > numero_correto:    
        print("Número muito alto!")
    elif numero < numero_correto:
        print("Número muito baixo")
    else:
        print(f"Você acertou o número correto, {numero_correto} em {tentativa} tentativas")