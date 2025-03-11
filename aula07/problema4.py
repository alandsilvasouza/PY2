# Problema 1: Soma de números pares em uma lista
def soma_pares(lista):
    """
    Calcula a soma de todos os números pares em uma lista
    Conceitos: loop for, condicional, operador módulo
    """
    total = 0
    for num in lista:
        if num % 2 == 0:  # Verifica se o número é par
            total += num
    return total

# Teste
print(soma_pares([1, 2, 3, 4, 5]))  # Deve retornar 6