class Carro():
    def __init__(self):
        self.placa = 'FHU2389'
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

class Moto():
    def __init__(self):
        self.placa = 'MKQ6502'
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True

    def sair_da_vaga(self):
        self.estacionado = False

class Vaga():
    def __init__(self, id, tipo, placa):
        self.id = id
        self.tipo = tipo
        self.livre = True
        self.placa = placa
    
    def ocupar(self):
        self.livre = False

    def desocupar(self):
        self.livre = True

class Estacionamento(Vaga,Carro,Moto):
    def __init__(self, total_vagas_livres_carro, total_vagas_livres_moto):
        self.vagas_de_carro = {1:'', 2:'', 3: '', 4: '', 5: ''}
        self.vagas_de_moto = {6: '', 7: '', 8:'', 9: '', 10: ''}
        self.carro_para_vaga = 1
        self.moto_para_vaga = 1
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    def estacionar_carro(self,carro):
        if self.total_vagas_livres_carro > 0:
            self.estacionar(carro)

            for carro in self.vagas_de_carro

    