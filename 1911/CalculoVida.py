cigarrosPorDias = int(input("Digite quantos cigarros você fuma por dia: "))
anosDeFumante = int(input("Digite há quantos anos você fuma: "))

percaPorDia = int(cigarrosPorDias * 10) 
percaPorAno = int(percaPorDia * 365) # O quanto ele perdeu em 1 ano
percaTotal = int(percaPorAno * anosDeFumante) #Perca total de todos os anos

diasPerdidos = int(percaTotal//1440)

print(f"Dias perdidos: {diasPerdidos}")


