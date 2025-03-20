def verificador_ano_bissexto():
    while True:
    # Solicita ao usuário que informe o ano
        ano = int(input("Informe o ano: "))

    # Verifica se o ano é bissexto
        if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
            print("SIM")
        if ano == 0:
            print("Encerrando...")
            break    
        else:
            print("NÃO")
# Chama a função
verificador_ano_bissexto()