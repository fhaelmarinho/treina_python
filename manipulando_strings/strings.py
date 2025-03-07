def linha():
    print('*'*30)

# Lista de seções
secoes = ["Manipulando string", "Python", "Rafael", "Daniela", "Webdev", "Data Science"]


#Programa Principal

for secao in secoes:
    if secao == "Manipulando string":
        linha()
        print(secao[::-1])    
        linha()
    elif secao == "Python":
        print(secao[::-2])    
        linha()
    else:    
        
        print(secao)
        linha()




