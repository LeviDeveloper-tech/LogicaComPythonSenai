dividaInicial = float(input("Digite o valor da divida: R$ "))
taxa = float(input("Digite a taxa: "))
jurosPrimeiroMes = float(dividaInicial * (taxa/100))
pagamentoMensal = float(input(f"Digite o valor da mensalidade. \nO valor da mesalidade não pode ser menor que {jurosPrimeiroMes:.2f} "))

if pagamentoMensal <= jurosPrimeiroMes:
    print("------------------------------------")
    print("Pagamento insuficiente. \nA divida nunca será paga.")
    print("------------------------------------")
else:
    mes = int(0)
    divida = float(dividaInicial)
    totalPago = float(0.0)
    
    while divida > 0:
        juros = float(divida * (taxa/100))
        divida = float(divida + juros)
        mes= int(mes + 1)

        if divida >= pagamentoMensal:
            pagoNesteMes = float(pagamentoMensal)
            divida = float(divida - pagamentoMensal)

        else:
            pagoNesteMes = float(divida)
            divida = 0.0
        
        
        totalPago = float(totalPago + pagoNesteMes)

    totalJuros = float(totalPago - dividaInicial)
    print("------------------------------------")
    print(f"Mês: {mes} \nTotal pago no final da quitação:R$ {totalPago:.2f} \nTotal Juros Totais: R$ {totalJuros:.2f}")
    print("------------------------------------")
    
        