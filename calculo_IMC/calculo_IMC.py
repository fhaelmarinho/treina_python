
# Função para calcular o IMC
def calculo_IMC(peso, altura):
    return peso/(altura**2)

# Função para classificar o IMC segundo a OMS
def classificacao_IMC(IMC):
    if IMC <= 18.5:
        return 'Baixo Peso'
    elif IMC <= 24.9:
        return 'Peso Normal'
    elif IMC <= 29.9:
        return 'Sobrepeso'
    elif IMC <= 34.9:
        return 'Obesidade Grau I'
    elif IMC <= 39.9:
        return 'Obesidade Grau II'
    else:
        return 'Obesidade Grau III'

# Solicitar dados do usuário
peso = float(input('Digite o Peso em kg:'))
altura = float (input('Digite sua Altura em m: '))

# Calcular o IMC
IMC = calculo_IMC(peso, altura)

# Verificar  Classificação do IMC segundo a OMS
classificacao = classificacao_IMC(IMC)

# Mostrar o resultado e clificação do IMC
print('O valor do IMC é:', round(IMC,2), 'Segundo a OMS sua classificação é:', classificacao)























