def buscaBinaria(vetor, alvo):
    l = int(0)
    r = int(len(vetor)-1)
    meio = (l + r)//2
    
    while l <= r:
        if meio < alvo:
            l = int (meio + 1)
        elif meio > alvo:
            r = int(meio - 1)
        else:
            return f"Valor {vetor[meio]} encontrado no índice {meio}"  
    return f"Valor {alvo} não encontrado."


vetor = [58, 65, 72, 79, 86, 93, 100, 107, 114, 121, 128, 135, 142, 149, 156, 163, 170, 177, 184, 191, 198, 205, 212, 219, 226, 233]

print(buscaBinaria(vetor, 59))