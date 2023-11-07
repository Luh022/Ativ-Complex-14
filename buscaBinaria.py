def busca_binaria(arr, alvo, inicio, fim):

if inicio > fim:

retornar -1

meio = (inicio + fim) // 2

if arr[meio] == alvo:

retornar meio

elif arr[meio] < alvo:

return busca_binaria(arr, alvo, meio + 1, fim)

outro:

return busca_binaria(arr, alvo, inicio, meio - 1)

