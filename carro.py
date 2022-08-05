class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = 'Preto'
        self.modelo = 'Kicks'
        self.velocidade = 80
        self.velocidade_min = 0
        self.velocidade_max = 300

    def ligar(self):
        self.ligado = True
        
    def desligar(self):
        self.ligado = False

    def aumentar_velocidade(self):
        if not self.ligado:
            return
        if self.velocidade < self.velocidade_min:
            self.velocidade += 1
        
    def reduzir_velocidade(self):
        if not self.ligado:
            return
        if self.velocidade > self.velocidade_max:
            self.velocidade -= 1
    
    def __str__(self) -> str:
        return f'Carro - ligado {self.ligado} - velocidade { self.velocidade}'

carro = Carro()

for x in range(80):
 carro.reduzir_velocidade()

# aumentar velocidade
carro.ligar()
carro.aumentar_velocidade()
print(f'Carro está ligado? ', carro.ligado)
print(f'Carro está em qual velocidade? ', carro.velocidade)
 
# reduzir velocidade

carro.reduzir_velocidade()
carro.desligar()
print(f'Carro está desligado? ', carro.desligado)