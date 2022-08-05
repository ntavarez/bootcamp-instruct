class Pessoa: 
    def __init__(self): 
         self._idade = 20
         self._nome = 'Isabela'
      
    def get_idade(self): 
        return self._idade 
    
    def set_idade(self, idade): 
        self._idade = idade 
    
    def get_nome(self): 
        return self._nome
    
    def set_nome(self, nome): 
        self._nome = nome 
  
pessoa = Pessoa()
print(pessoa.get_idade()) 
print(pessoa.get_nome()) 

pessoa.set_idade(25)
pessoa.set_nome('Juliana')
  
print(pessoa._idade)
print(pessoa._nome) 