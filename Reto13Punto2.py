#Definir una función para crear el primer diccionario ingresado por el usuario
def crearDiccionario1():
    diccionario1 = {} #Se crea un diccionario vacio
    tamaño = int(input("Ingrese el tamaño del diccionario 1: ")) #Se sokicita el ingreso de la cantidad de claves
    for i in range(tamaño): #Ciclo for para cada indice
        #Se solicita que se ingrese cada clave y su respectivo valor
        clave = input("Ingrese la clave: ") 
        valor = (input("Ingrese el valor: "))
        diccionario1[clave] = valor #Agregar el valor y la clave al diccionario
    return diccionario1 #Se retorna la función definida

#Definir una función para crear el segundo diccionario ingresado por el usuario
def crearDiccionario2():
    diccionario2 = {} #Se crea un diccionario vacio
    tamaño = int(input("Ingrese el tamaño del diccionario 2: ")) #Se sokicita el ingreso de la cantidad de claves
    for i in range(tamaño): #Ciclo for para cada indice
        #Se solicita que se ingrese cada clave y su respectivo valor
        clave = input("Ingrese la clave: ") 
        valor = (input("Ingrese el valor: "))
        diccionario2[clave] = valor #Agregar el valor y la clave al diccionario
    return diccionario2 #Se retorna la función definida

#Definir otra función para unir los diccionarios ingresados anteriormente
def mezclarDiccionarios(diccionario1, diccionario2):
    diccionarioCombinado = diccionario1.copy() #Realizar una copia del primer diccioario y asignarlo
    diccionarioCombinado.update(diccionario2) #Unir el segundo diccionario a la copia del primero
    return diccionarioCombinado #Se retorna la función definida

#Llamar las funciones e imprimir el resultado de cada diccionario y la unión de estos
if __name__ == "__main__":
    print("Primer diccionario:")
    diccionario1 = crearDiccionario1()
    print(diccionario1)
    print("Segundo diccionario:")
    diccionario2 = crearDiccionario2()
    print(diccionario2)
    diccionarioCombinado = mezclarDiccionarios(diccionario1, diccionario2)
    print("Diccionario mezclado:")
    print(diccionarioCombinado)

