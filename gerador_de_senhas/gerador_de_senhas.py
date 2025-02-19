import random
import string

def gerar_senha(comprimento, usar_maiusculas=True, usar_numeros=True, usar_especiais=True):
    caracteres = string.ascii_lowercase
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiais:
        caracteres += string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(comprimento))

comprimento = int(input("Digite o comprimento da senha: "))
print("Senha gerada:", gerar_senha(comprimento))