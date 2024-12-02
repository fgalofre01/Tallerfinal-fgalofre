from models.Animal_Exotico import Animal_exotico

class Huron(Animal_exotico):
    
   def __init__(self, nombre, peso, edad):
        super().__init__(nombre, peso, edad)
       
   def hacer_sonido(self)->str:
        return f'El {self.nombre} hace ¡Eek Eek!'
   
    
   
    
    