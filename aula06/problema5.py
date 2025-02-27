class ContaBancaria:
    def __init__(self):
        self.__saldo = 0  # Atributo privado saldo, inicializado com 0

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")
        self.__saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def ver_saldo(self):
        return self.__saldo


# Exemplo de uso
conta = ContaBancaria()
conta.depositar(100.00)
print(f"Saldo atual: R${conta.ver_saldo():.2f}")
try:
    conta.sacar(50.00)
except ValueError as e:
    print(e)


# Tentar sacar mais do que o saldo disponível
try:
    conta.sacar(200.00)
except ValueError as e:
    print(e)

# Tentar depositar valor negativo
try:
    conta.depositar(-10.00)
except ValueError as e:
    print(e)