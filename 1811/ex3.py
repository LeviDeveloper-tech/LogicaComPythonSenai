print("=====Calculadora de viagem=====")
print("===============================")
distancia = float(input("Qual a distância da viagem em km: "))
velocidadeMedia = float(input("Qual a velocidade média em km: "))

tempo = float(distancia/velocidadeMedia)
horas = int(tempo)
minutos = round((tempo - horas)*60)

dias = int(tempo//24)
restoDias = int(tempo % 24)

print("================")
print(f"Dias de viagem: {dias} dias e {restoDias} horas")
print(f"Hora total de viagem: {horas}h:{minutos}m")
