class Carro:  
    def __init__(self, marca):  
        self.marca = marca  
        self.velocidade = 0  # Atributo inicializado  
  
    def acelerar(self):  
        self.velocidade += 10  # Incrementa velocidade  
  
    def mostrar_velocidade(self):  
        print(f"Velocidade atual: {self.velocidade} km/h")  
        
# Solução Problema 3  
class CarroEletrico(Carro):  
    def __init__(self, marca):  
        super().__init__(marca)  # Chama construtor da classe pai  
        self.bateria = 100  # Novo atributo  
  
    def acelerar(self):  
        if self.bateria >= 10:  
            super().acelerar()
            self.bateria -= 5  
        else:  
            print("Bateria fraca! Recarregue.")  
  
    def mostrar_bateria(self):  
        print(f"Bateria restante: {self.bateria}%")  

# Exemplo de uso:  
carro_eletrico = CarroEletrico("Tesla")  
carro_eletrico.acelerar()  
carro_eletrico.mostrar_velocidade()  # Velocidade atual: 10 km/h  
carro_eletrico.mostrar_bateria()      # Bateria restante: 95%  