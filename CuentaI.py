from typing import AbstractSet
from abc import ABC, abstractmethod

class CuentaI(ABC):
    @abstractmethod
    def getCliente(self):
         pass

    @abstractmethod
    def getCantidad(self):
        pass

    @abstractmethod
    def movimiento(self,importe):
        pass
    
