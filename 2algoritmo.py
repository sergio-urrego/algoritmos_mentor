"""Elabore un algoritmo que permita calcular la siguiente serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34,55,89,144,233,377."""

"""1) inicializar 3 variables "a", "b" y "c" una de ellas debe ser la que active el 
mecanismo para hacer la operacion en este caso "a"""


a=1
b=0
c=0
"""2)la variable "a" es la que va a llevar las cuentas del resultado 
con cada iteracion echa y valida cunatas iteraciones va hacer el flujo """

while a < 377:
    #3)convertimos una de las variables en la suma de la variable que inicio el mecanisco y otra que este en cero
    c=a+b
    #4) la variable "a" que lleva el contador toma el valor de "b" y va a mostar el valor de la variable "b" de aquien en adelante
    a=b
    print(a)
    """5)despues de que la variable "a" tome el valor de "b" esta misma se cambia por 
    el valor de la variable "c" la cual proporciona  el siguiente valor y continua haciendo un flujo 
    de valores asi iterando hasta que la variable "a" nuevamente tome el valor de la variable "b" dentro 
    del flujo asi sobre escribiendo la contador que lleva el conteo y valida el fin de la iteracion """
    b=c


    