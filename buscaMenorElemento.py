def find_smallest_element(arr):

# Caso base: se a lista contiver apenas um elemento, retorne-o

se len(arr) == 1:

retornar arr[0]

# Divida a lista em duas metades

meio = len(arr) // 2

primeira_metade = arr[:mid]

segundo_metade = arr[meio:]

# Encontre recursivamente o menor elemento em cada metade

menor_primeiro = encontrar_menor_elemento(primeira_metade)

menor_segundo = encontrar_menor_elemento(segundo_metade)

# Compare os menores elementos de cada metade

se menor_primeiro < menor_segundo:

retornar menor_primeiro

outro:

retornar menor_segundo

# Exemplo para encontrar o menor número na lista
arr = [5, 2, 9, 1, 7]

menor = find_smallest_element(arr)

imprimir(menor) # Saída: 1