import problema6

# Lista para armazenar as contas bancárias
contas = []

# Loop para criar 100 milhões de contas bancárias
for i in range(100_000_000_000):
    conta = problema6.ContaBancaria()
    contas.append(conta)

input("Pressione Enter para continuar...")
