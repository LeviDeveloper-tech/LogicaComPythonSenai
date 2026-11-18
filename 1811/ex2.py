precoMercadoria = float(input("Digite o valor total da mercadoria: "))

while True:
    percentualDesconto = int(input("Digite o percentual de desconto: "))
    
    if percentualDesconto > 50 or percentualDesconto < 1:
        print("=========================")
        print("Digite um valor de 1 a 50")
        print("=========================")
        continue
    else:
        break

descontoTotal = precoMercadoria * (percentualDesconto/100)
precoFinal = precoMercadoria - descontoTotal


print(f"===Percetuntal do desconto: {percentualDesconto}% ===" )
print(f"===Valor total do desconto: R$ {descontoTotal:.2f} ===" )
print(f"===Valor final da mercadoria: R$ {precoFinal:.2f} ===" )