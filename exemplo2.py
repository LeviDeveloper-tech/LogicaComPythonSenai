velocidade = float(input("Velocidade (km/h): "))

if velocidade > 80:
    multa = (velocidade - 80)*5
    print("Você foi multado!")
    print(f"Multa: R$ {multa:.2f}")
else:
    print("Sem multa")