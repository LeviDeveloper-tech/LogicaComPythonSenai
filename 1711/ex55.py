salario = float(input("Salário total: R$"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = float(salario + aumento)

print(f"Salário Base: R$ {salario:.2f}")
print(f"-------------------------------")
print(f"Aumento: R$ {aumento:.2f}")
print(f"-------------------------------")
print(f"Novo Salário: R$ {novo_salario:.2f}")
print(f"-------------------------------")