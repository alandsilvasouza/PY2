from datetime import datetime  # Para registrar data e hora das transações

class ContaBancaria:
    def __init__(self):
        # Atributo privado saldo, inicializado com 0
        self.__saldo = 0
        # Lista para armazenar o histórico de transações
        self.__historico = []

    def depositar(self, valor, obs=""):
        # Adiciona o valor ao saldo e registra a transação no histórico
        if valor > 0:
            self.__saldo += valor
            self.__registrar_transacao("Depósito", valor, obs)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor, obs=""):
        # Verifica se há saldo suficiente para o saque e registra a transação no histórico
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
                self.__registrar_transacao("Saque", valor, obs)
                print(f"Saque de R${valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def ver_saldo(self):
        # Retorna o saldo atual
        return self.__saldo

    def extrato(self):
        # Exibe o histórico de transações com data, hora e observação
        print("\n--- Extrato da Conta ---")
        for transacao in self.__historico:
            print(f"{transacao['data_hora']} | {transacao['tipo']} | R${transacao['valor']:.2f} | Obs: {transacao['obs']}")
        print(f"Saldo atual: R${self.__saldo:.2f}\n")

    def __registrar_transacao(self, tipo, valor, obs):
        # Método privado para registrar uma transação no histórico
        transacao = {
            "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),  # Data e hora formatadas
            "tipo": tipo,  # Tipo de transação (Depósito ou Saque)
            "valor": valor,  # Valor da transação
            "obs": obs  # Observação (opcional)
        }
        self.__historico.append(transacao)


# Exemplo de uso da classe
conta = ContaBancaria()
conta.depositar(100.50, "Salário")
conta.sacar(50.25, "Pagamento de conta")
conta.depositar(200.00, "Presente")
conta.sacar(30.00, "Lanche")
conta.extrato()


lista1 = [] #criando uma lista
lista1.append("item1") #adicionando um item na lista
dict1 = { "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        , "obs": "observacao" 
        , "outro_chave": "outro_valor" } #criando um conjunto

#laço
for item in lista1:
    print(item["data_hora"], item["obs"]) 
