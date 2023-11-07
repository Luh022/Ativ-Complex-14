def busca_linear_recursiva(arr, elemento, inicio, fim):

if inicio > fim:

retornar -1

if arr[inicio] == elemento:

retorno inicio

if arr[fim] == elemento:

fim de retorno

return busca_linear_recursiva(arr, elemento, inicio + 1, fim - 1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

elemento = 5

índice = busca_linear_recursiva(arr, elemento, 0, len(arr) - 1)

se índice! = -1:

print(f'O elemento {elemento} foi encontrado no índice {indice}.')

outro:

print(f'O elemento {elemento} não foi encontrado na lista.')