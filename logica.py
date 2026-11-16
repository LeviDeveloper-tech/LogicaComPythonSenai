custo_dia = 60
custo_km = 0.15

dias = int(input("Dias alugados:"))
kms = float(input("Km rodados:"))


total = (dias * custo_dia) + (kms * custo_km)

print(f"Total a pagar: R$ {total:.2f}")