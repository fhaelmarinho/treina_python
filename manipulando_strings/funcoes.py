def estudo():
    print("Estudando Python")

def exibir_mensagem(nome="Rafael"):
    print(f"Olá, {nome}!")

estudo()
exibir_mensagem()

def calcular_imposto(valor):
    if valor < 1000:
        imposto = valor * 0.1
    elif valor < 2000:
        imposto = valor * 0.15
    else:
        imposto = valor * 0.25

    return imposto

preco_produto1 = 1000
preco_produto2 = 1500
preco_produto3 = 2000
imposto_produto1 = calcular_imposto(preco_produto1)
imposto_produto2 = calcular_imposto(preco_produto2)
imposto_produto3 = calcular_imposto(preco_produto3)

print(f"O imposto do produto 1 é {imposto_produto1}")
print(f"O imposto do produto 2 é {imposto_produto2}")
print(f"O imposto do produto 3 é {imposto_produto3}")

