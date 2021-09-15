from CuentaNormal import CuentaNormal
from CuentaI import CuentaI


class CuentaProxy(CuentaI):

    def __init__(self,name):
        self.cuenta_normal = CuentaNormal(name)

    def getCliente(self):
        return self.cuenta_normal.getCliente()
    
    def getCantidad(self):
        return self.cuenta_normal.getCantidad()

    def movimiento(self,importe):
        disponible = self.cuenta_normal.cantidad

        if importe < 0:
            if disponible == 0:
                return print('La cuenta esta en cero no podes realizar extracciones')
            else:
                monto = disponible - (importe*-1)
                if monto < 0:
                    return print(f'No podes retirar {importe*-1} porque solo dispones de {disponible}')
                else:
                    return self.cuenta_normal.movimiento(importe)
        else:
            return self.cuenta_normal.movimiento(importe)
