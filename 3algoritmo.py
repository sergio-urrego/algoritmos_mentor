"""Elabore un algoritmo que permita ingresar una persona (nombre) y preguntar su edad, al
finalizar, el algoritmo debe preguntar si desea registrar otra persona (nombre) y su edad, si
decide no hacerlo el algoritmo debe arrojar los siguientes datos:
• Número de personas mayores de edad (personas mayores a 17 años)
• Número de personas menores de edad (personas menores a 18 años)
• Número de personas pertenecientes a la tercera edad (personas mayores a 60 años)
• Número de infantes (niños menores de 7 años)
• Número de personas que NO son infantes NI pertenecientes a la tercera edad.
• Persona (nombre) con mayor edad y su edad.
• Persona (nombre) con menor edad y su edad.
PD: Tenga en cuenta que el algoritmo nunca debe salirse sin haber registrado por lo menos
una persona.
Ejemplo:
Carlos 22 años.
Juan 16 años.
Mattias 7 años
Luis 62 años.
Resultado:
• Número de personas mayores de edad (personas mayores a 17 años): 2
• Número de personas menores de edad (personas menores a 18 años): 2
• Número de personas pertenecientes a la tercera edad (personas mayores a 60 años): 1
• Número de infantes (niños menores de 7 años): 1
• Número de personas que NO son infantes NI pertenecientes a la tercera edad: 2
• Persona (nombre) con mayor edad y su edad: Luis 62 años
• Persona (nombre) con menor edad y su edad: Mattias 7 años"""

"""1)primero inicializamos dos listas una va a contener los nombres de las personas y sus edades
"""

nombres=[]
edades=[]
"""2)despues inicializamos lso contadores para ver cuantas personas son mayores de edad cuantas no,
     cuantas adulto mayor y cuantos infante 
"""

mayoresedad=0
menoresedad=0
adultomayor=0
infante=0
print("----------------------------------------------------------------------------------------------")
print("---------------------------------Bienvenido-------------------------------------------------- ")
print("----------------------------------------------------------------------------------------------")
"""3) hacemos la primera insercion obligatoria"""
insertar=1
nombre=str(input("dijita el nombre de  la persona \n"))
nombres.append(nombre)
edad=int(input(f"ingresa la edad  de {nombre}\n"))
edades.append(edad)

"""4)preguntamos si queremos agregar mas personas"""
print("----------------------------------------------------------------------------------------------------")
insertar=int(input("quieres insertar otra perosna \n NO=0 \n SI=1 \n->"))
print("----------------------------------------------------------------------------------------------------")

"""4.1) si quiere agregar mas personas vulve a preguntar los datos para la siguiente persona"""
while insertar==1:
    nombre=str(input("dijita el nombre de  la persona \n"))
    nombres.append(nombre)
    edad=int(input(f"ingresa la edad  de {nombre}\n"))
    edades.append(edad)
    print("----------------------------------------------------------------------------------------------------")
    insertar=int(input("quieres insertar otra perosna \n NO=0 \n SI=1 \n->"))
    print("----------------------------------------------------------------------------------------------------")
    if insertar==1:
        insertar==1
    else:
        insertar==0
"""5)cuando ya no hay que insertar mas personas viene una comprovacion y incializamos las variables de rango de edaddes"""
if insertar==0:
    mayoredad=18
    adultosmayores=60
    niños=7
    notitas=[]
    """6)hacemos un ciclo for para recorrer la lista y con la posicion de los datos de esa sacamos el dato de la otra  """
    for c in  range(len(edades)):
        clasificacion=edades[c]
        notitas.append(clasificacion)
        nombre=nombres[notitas.index(clasificacion)]
        validar=clasificacion
        maxima=max(edades)
        minima=min(edades)
        """7)valaidamos si la persona es mayor de edad """
        if validar>=mayoredad and validar<=adultosmayores:
            mayoresedad=mayoresedad+1
            print(f"la persona {nombre} es mayor de edad y tiene {validar} años de edad")
            print("----------------------------------------------------------------------------------------------------")
        """8)validamos si la persona es menor de edad"""
        if validar < mayoredad and validar > niños :
            menoresedad=menoresedad+1
            print(f"la persona {nombre} es menor de edad y tiene {validar} años de edad")
            print("----------------------------------------------------------------------------------------------------")
        """9)validamos si la persona es menor de 7 años """
        if validar<=niños:
            infante=infante+1
            print(f"el niñ@ {nombre} y tiene {validar} años de edad")
            print("----------------------------------------------------------------------------------------------------")
        """10)validamos si la persona es un adulto mayor"""
        if validar>60:
            adultomayor=adultomayor+1
            print(f"la persona {nombre} es un adulto mayor y tiene {validar} años de edad")
            print("----------------------------------------------------------------------------------------------------")
        """11)validamos que persona tiene la edad mas alta"""
        if validar==maxima:
            print(f"la persona con mas edad es {nombre} y tiene {validar} años de edad")
            print("----------------------------------------------------------------------------------------------------")
        """12)validamos que persona tiene la edad mas baja"""
        if validar==minima:
            print(f"la persona con menos edad es {nombre} y tiene {validar} años de edad ")
            print("----------------------------------------------------------------------------------------------------")
        """13)imprimimos los contadores para saber cuantas personas hay de cada grupo """

    print(f"el numero de mayores de edad es de {mayoresedad}")
    print("----------------------------------------------------------------------------------------------------")
    print(f"el numero de menores de edad de {menoresedad}")
    print("----------------------------------------------------------------------------------------------------")
    print(f"el numero de infantes es de {infante}")
    print("----------------------------------------------------------------------------------------------------")
    print(f"el numero de adultos mayores  es de {adultomayor}")
    print("----------------------------------------------------------------------------------------------------")
    """14)fin del programa :)"""
    input("presione enter para continuar")
    
            


   

    