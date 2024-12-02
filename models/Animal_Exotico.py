from models.Animal import Animal

class Animal_exotico(Animal):
    def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
        
    def hacer_sonido(self) -> str :
        return "Estos animales hacen un sonido caracteristico"
        
  
    
    
    
