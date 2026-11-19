print("Aluguel de Carro")
print("==========================")
valorPorDia = float(60)
valorPorKm = float(0.15)


diasAlugados = int(input("Digite os dias totais que o carro foi alugado: "))
kmPecorridos = float(input("Digite a quantidade de quilometros (km) foram percorridos:  "))

totalAluguel = (diasAlugados * valorPorDia) + (valorPorDia * kmPecorridos)

print("=============================")
print("==========Relatório==========")
print("=============================")
print("                             ")
print(f"Dias alugado-----------{diasAlugados}dias")
print(f"Kms rodados-----------{kmPecorridos:.2f}km")
print("----------------------------")
print("----------------------------")
print(f"Total-----------------R${totalAluguel:.2f}")