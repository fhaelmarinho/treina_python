def area(largura, comprimento):
    return largura * comprimento

largura = (float(input("Digite a largura do terreno:")))
comprimento = (float(input("Digite o comprimento do terreno: ")))
area_total = largura * comprimento 
valor_metro_quadrado = 25.0

if area_total < 50:
    print("Terreno pequeno, com área de:", area_total, "m² é isento de IPTU")
else:
    iptu = area_total * valor_metro_quadrado
    print(f"Terreno grande, com área de:", {area_total}, "m² paga IPTU absurdo de", "R$", {iptu})