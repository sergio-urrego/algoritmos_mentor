""" 1. Calcular la distancia que recorre un vehículo en cierto tiempo definiendo una velocidad
      constante (Distancia = Velocidad x Tiempo), así mismo cuanto tiempo tardaría en alcanzar
      los 1000 kilómetros de distancia si se mantiene esa misma velocidad."""


print("----------------------------------------------------------------------------------------------")
print("---------------------------------Bienvenido-------------------------------------------------- ")
print("----------------------------------------------------------------------------------------------")
#1) hay que definir la velocidad crucero en este caso la vamos a pedir al usuario 
velocidad=int(input("escribe la velocidad crucero a la que va el vehiculo \n->"))

#2) hay que definir el tiempo para este ejemplo va hacer en minutos
tiempo=int(input("para saber cuantos recorreras debes poner un tiempo en minutos\n-> "))

#3) debemos hacer una convercion de minutos a hora y/o horas
minutos=int(tiempo%60)
horas=(tiempo-minutos)/60
hora=tiempo*1/60

#4) debemos  mostrar el resultado de la conversion para ver si es correcto
tutiempo=int(input(f"el tiempo que dijitaste es de {horas:.0f} horas y {minutos} minutos  \n deseas continuar para saber cuanta distancia recorreras o has recorrido? \n SI=1 \n NO=2 \n"))

#5) sino es correcto vuelve a pedir el valor del tiempo en minutos y sucribe las variables anteriores
while tutiempo==2:
    tiempo=int(input("vuleve a ingresar tiempo en minutos para ver cuanto recorreras y/o has recorridos\n-> "))
    minutos=int(tiempo%60)
    horas=(tiempo-minutos)/60
    hora=tiempo*1/60
    
    #5.1)  vuelve y pregunta si es valor de la convercion es correcta de lo comtraio vuelve y pregunta 
    tutiempo=int(input(f"el tiempo que dijitaste es de {horas:.0f} horas y {minutos} minutos  \n deseas continuar para saber cuanta distancia recorreras o has recorrido? \n SI=1 \n NO=2 \n"))
    if tutiempo==2:
        tutiempo==2

    #5.2)si es correcta rompe el ciclo while y sigui con el algoritmo
    else:
        tutiempo==1

#6)si el valor es correcto  hace la formula de la distancia  la imprime
#y tambien cuanta distancia segun su velocidad recorrera en una hora   
if tutiempo==1:
    distancia=velocidad*hora
    print(f"la distancia que recorreras o has recorido en {horas:.0f} horas y {minutos} es de {distancia} km")
    distanciaenunahora=velocidad*1
    print(f"la distancia que recorreras o has recorido en 1 hora es de {distanciaenunahora} km ")

#7)termina el programa