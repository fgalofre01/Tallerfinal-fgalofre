from models.Huron import Huron
from models.Boa_Constrictor import Boa_Constrictor
from models.Perro import Perro
from models.Gato import Gato

class Guarderia():
    
    animals = {
        "huron": Huron("Huron", 10.5, 5),
        "boa constrictor": Boa_Constrictor("Boa Constrictor", 12.8, 7),
        "perro": Perro("Perro", 12.6, 4),
        "gato": Gato("Gato", 6.7, 6)
        }