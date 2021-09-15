from CuentaProxy import CuentaProxy
from CuentaNormal import CuentaNormal

def main():

    print('CUENTA NORMAL ==========\n')
    cuenta_normal = CuentaNormal('pepe')
    print(f'Bienvenido: {cuenta_normal.getCliente()}')
    print('usted dispone de $',cuenta_normal.getCantidad())
    print('\n')

    #DEPOSITOS
    cuenta_normal.movimiento(20)
    cuenta_normal.movimiento(25)
    #EXTRACCION
    cuenta_normal.movimiento(-80)
    #SALDO
    print(f'SU SALDO ES: ${cuenta_normal.getCantidad()}')

    print('\n------------------------\n')

    print('CUENTA PROXY ==========\n')
    cuenta_proxy = CuentaProxy('pepeproxy')
    print(f'Bienvenido: {cuenta_proxy.getCliente()}')
    print('usted dispone de $',cuenta_proxy.getCantidad())
    print('\n')

    #DEPOSITOS
    cuenta_proxy.movimiento(20)
    cuenta_proxy.movimiento(25)
    #EXTRACCION
    cuenta_proxy.movimiento(-80)
    #SALDO
    print(f'SU SALDO ES: ${cuenta_proxy.getCantidad()}')
    print('\n')


main()