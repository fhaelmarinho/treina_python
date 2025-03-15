menu = '''
Selecione a opção desejada:

[d] Depositar (1)
[s] Sacar (2)
[e] Extrato (3)
[q] Sair (0)
'''

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_TRANSACAO = 10

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        print("Depositar")
        valor = float(input("Informe o valor do depósito: "))
        if valor <=0:
            print("Operação não permitida! Informe um valor válido")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    elif opcao == "s" or opcao == "S":
        print("Sacar")
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente!")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite diário de saques atingido!")
        elif valor > limite:
            print("Limite de saque excedido!")    
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    
    elif opcao == "e" or opcao == "E":
        print("========== Extrato =========")
        print(extrato)
        print(f"saldo: R$ {saldo:.2f}")
        print("========== Extrato =========")
        
    elif opcao == "q" or opcao == "Q":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")