ano = int(input("Digite um ano: "))

#Antes de 1582 não existia o calendário gregoriano

if ano < 1582:
 print("Não dentro do período do calendário gregoriano")
else:
   if ano % 4 != 0:
     print("ano comum")
   elif ano % 100 != 0:
     print("Ano bissexto")
   elif ano % 400 != 0:
     print("ano comum")
   else:
     print("Ano bissexto") 