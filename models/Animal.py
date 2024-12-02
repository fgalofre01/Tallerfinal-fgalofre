
from abc import ABC,abstractmethod

class Animal():
    def __init__(self, nombre: str, peso: float, edad: int):
        self._nombre = nombre
        self._peso = peso
        self._edad = edad 
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre: str) -> None:
        self._nombre = nombre
    
    @property
    def peso(self) -> float:
        return self._peso
    
    @peso.setter
    def peso(self,peso : float) -> None:
        self._peso = peso
        
    @property
    def edad(self) -> int:
        return self._edad
    
    @edad.setter
    def edad(self,edad: int) -> None:
        self._edad = edad
    
    @abstractmethod    
    def hacer_sonido(self) -> str :
        pass
    