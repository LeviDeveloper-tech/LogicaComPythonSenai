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