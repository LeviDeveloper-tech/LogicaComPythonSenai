preco = 0

while(preco <= 0):
    cat = int(input("Insira um número: "))
    if cat == 1:
        preco = 10
        print(f"Preço: {preco}")
        break
    elif cat == 2:
        preco = 18
        print(f"Preço:  {preco}")
        break
    elif cat == 3:
        preco = 23
        print(f"Preço:  {preco}")
        break
    elif cat == 4:
        preco = 26
        print(f"Preço:  {preco}")
        break
    elif cat == 5:
        preco = 31
        print(f"Preço:  {preco}")
        break
    else:
        preco = 0
        print(f"Inválida ")
        print("                 ")
        continue
print("Fim do programa!")
print("                 ")
