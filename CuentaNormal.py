from CuentaI import CuentaI

class CuentaNormal(CuentaI):

    cliente = ''
    cantidad = 0

    def __init__(self, name):
        self.cliente = name
        

    def getCliente(self):
        return self.cliente

    def getCantidad(self):
        return self.cantidad

    def movimiento(self,importe):
        self.cantidad += importe
        if importe < 0:
            return print(f"SE EXTRAJO : {importe *-1}")
        else:
            return print(f"SE DEPOSITO: {importe}")