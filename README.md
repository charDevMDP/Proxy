# PATRONES DE DISEÑO


### EJERCICIO PROXY

```
Nuestro sistema bancario tiene una interface basica Cuenta. 

Esta permite tener el nombre y la cantidad de dinero de un cliente, asi como efectuar un 
nuevo movimiento.

La implementacion basica es CuentaNormal.

Ahora queremos crear un nuevo tipo de cuenta que NO permita quedar en negativo. NO hay que 
modificar CuentaNormal. Hay que crear una nueva que ofrezca la misma API (interface Cuenta) y
delege las llamadas que recibe a  una CuentaNormal excepto, y aqui esta el trabajo, en caso 
que el movimiento requerido fuese a dejar la cuenta en negativo. En este caso, simplemente no 
debe realizar la operacion (un caso mas realista probablemente lanzaria una excepcion, pero aqui
no lo haremos).

Es importante que la clase que crees nueva use una CuentaNormal para delegar las llamadas. Ahora 
la clase es muy sencilla, pero se supone que algunos metodos se pueden complicar en un futuro y
no queremos codigo duplicado.

Una vez tengas la clase, modifica el test test_cuenta_nueva de TestCuentas para que en 
lugar de usar una clase CuentaNormal use nuestra nueva clase.
```

> CharDev :computer: