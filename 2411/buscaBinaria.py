# def buscaBinaria(vetor, meio):
#     vetor = list(range(58, 234, 7))
#     l = int(0)
#     r = int(len(vetor)-1)
#     meio = (l + r)//2
    
#     while(l <= r):
#         if(meio < r):
#             r = int(meio - 1)
#         elif(meio > l):
#             l = int(meio + 1)
#         else:
#             valor = int(vetor[meio])
#             print("Valor {valor} encontrado no índice: {meio}")

vetor = list(range(58, 234, 7))
 
print(vetor)