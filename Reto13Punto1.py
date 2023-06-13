#Definir una función para crear un diccionario ingresado por el usuario
def crearDiccionario():
    diccionario = {} #Se crea un diccionario vacio
    tamaño = int(input("Ingrese el tamaño del diccionario: ")) #Se sokicita el ingreso de la cantidad de claves
    for i in range(tamaño): #Ciclo for para cada indice
        #Se solicita que se ingrese cada clave y su respectivo valor
        clave = input("Ingrese la clave: ") 
        valor = float(input("Ingrese el valor (Números): "))
        diccionario[clave] = valor #Agregar el valor y la clave al diccionario
    return diccionario #Se retorna la función definida

#Definir función para ordenar de manera ascendente el diccionario
def ordenAscendente(diccionario):
    #Se utiliza el método sorted para ordenar de forma ascendente el diccionario ingresado
    diccionarioOrden = sorted(diccionario.items(), key=lambda x: x[1])
    return diccionarioOrden #Se retorna la función definida

#Llamar las funciones e imprimir el resultado   
if __name__ == "__main__":
    #Se llaman las funciones definidas anteriormente
    diccionario = crearDiccionario()
    diccionarioOrden = ordenAscendente(diccionario)
    #Se imprime el diccionario ingresado
    print("El diccionario ingresado fue: ")
    print(diccionario)
    #Se imprime el diccionario ingresado con sus valores ordenados de manera ascendente
    print("El diccionario ingresado en orden ascendente es el siguiente: ")
    print(diccionarioOrden)

     