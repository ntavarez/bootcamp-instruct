class Carro():
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True
        print('Estacionado.')

    def sair_da_vaga(self):
        self.estacionado = False

class Moto():
    def __init__(self, placa):
        self.placa = placa
        self.estacionado = False
    
    def estacionar(self):
        self.estacionado = True
        print('Estacionado.')

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
    def __init__(self):
        self.vagas_de_carro = ["","","","",""]
        self.vagas_de_moto = ["","","","",""]
        self.carro_para_vaga = 1
        self.moto_para_vaga = 1
        self.total_vagas_livres_carro = 5
        self.total_vagas_livres_moto = 5

    def estacionar_carro(self, carro):
        if self.total_vagas_livres_carro > 0:
            posicao = self.vagas_de_carro.index("")
            self.vagas_de_carro.pop(posicao)
            self.vagas_de_carro.insert(posicao, carro.placa)
            self.total_vagas_livres_carro = self.total_vagas_livres_carro - 1
            carro.estacionado = True
    
    def estacionar_moto(self, moto):
        if self.total_vagas_livres_moto > 0:
            posicao = self.vagas_de_moto.index("")
            self.vagas_de_moto.pop(posicao)
            self.vagas_de_moto.insert(posicao, moto.placa)
            self.total_vagas_livres_moto = self.total_vagas_livres_moto - 1
            moto.estacionado = True
        elif self.total_vagas_livres_carro < 5:
            posicao = self.vagas_de_carro.index("")
            self.vagas_de_carro.pop(posicao)
            self.vagas_de_carro.insert(posicao, moto.placa)
            self.total_vagas_livres_carro = self.total_vagas_livres_carro - 1
            moto.estacionado = True
            
    def remover_carro(self, carro): 
        vaga = self.vagas_de_carro.index(carro.placa)
        self.vagas_de_carro.pop(vaga)
        self.vagas_de_carro.insert(vaga,"")
        self.total_vagas_livres_carro= self.total_vagas_livres_carro + 1
        carro.estacionado = False

    def remover_moto(self, moto): 
        vaga = self.vagas_de_moto.index(moto.placa)
        self.vagas_de_moto.pop(vaga)
        self.vagas_de_moto.insert(vaga,"")
        self.total_vagas_livres_moto = self.total_vagas_livres_moto + 1
        moto.estacionar = False

    def estado_do_estacionamento(self):
        print(f'Vagas para carros: ', self.total_vagas_livres_carro)
        for i in range(len(self.vagas_de_carro)):
            print('Vaga ' + str(i+1) + ': ' + self.vagas_de_carro[i])
        print(f'Vagas para motos: ', self.total_vagas_livres_moto)
        for i in range(len(self.vagas_de_moto)):
            print('Vaga ' + str(i+1) + ': ' + self.vagas_de_moto[i])


carro1 = Carro('BFD6744')
carro2 = Carro('DGH2217')
moto1 = Moto('CPY0789')
moto2 = Moto('FTQ3623')
moto3 = Moto('DRG2367')
moto4 = Moto('CXX9004')
moto5 = Moto('QTY3321')
moto6 = Moto('LOJ6648')

estacionamento = Estacionamento()

estacionamento.estacionar_carro(carro1)
estacionamento.estacionar_carro(carro2)

estacionamento.estado_do_estacionamento()

estacionamento.estacionar_moto(moto1)
estacionamento.estacionar_moto(moto2)
estacionamento.estacionar_moto(moto3)
estacionamento.estacionar_moto(moto4)
estacionamento.estacionar_moto(moto5)
estacionamento.estacionar_moto(moto6)

estacionamento.estado_do_estacionamento()

estacionamento.remover_carro(carro2)
estacionamento.remover_moto(moto3)
estacionamento.remover_moto(moto4)

estacionamento.estado_do_estacionamento()





    