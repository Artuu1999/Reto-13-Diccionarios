# Se importa json
import json

#Definir una función para determinar las personas que práctican determinado deporte
def NombresDeporte(data, deporte):
    nombresCompletos = [] #Crear una lista vacía en la que se agregaran los nombres completos
    for usuario, info in data.items(): #Ciclo for para iterar sobre  los elementos del archivo
        if deporte in info['deportes']: #Condicinal que mira si el deporte ingresado está en el archivo
            nombres = info['nombres'] #Se obtiene los nombres si el condicional se cumple
            apellidos = info['apellidos'] #Se obtienen los apellidos
            nombre= f"{nombres} {apellidos}" #Concatena los nombre y apellidos obtenidos anteriormente
            nombresCompletos.append(nombre) #Se agrega a la lista vacía los nombres y apellidos encontrados
    return nombresCompletos #Se retorna la función definida

#Definir una función para determinar las personas se encuentran en determinado rango de edad
def NombresRangoEdades(data, edadMinima, edadMaxima):
    nombreRango = [] #Crear una lista vacía en la que se agregaran los nombres completos
    for usuario, info in data.items(): #Ciclo for para iterar sobre  los elementos del archivo
        edad = info['edad'] #Obtiene la edad de las personas del diccionario
        #Condicinal para verificar que la edad se encuentre dentro del rango de edad ingresado por el usuario
        if edadMinima <= edad <= edadMaxima:
            nombres = info['nombres'] #Si se encuentra, se obtiene los nombres de la persona
            apellidos = info['apellidos'] #Se obtiene los apellidos de la persona
            nombreRangoEdad = f"{nombres} {apellidos}" #Concatena los nombre y apellidos obtenidos anteriormente
            nombreRango.append(nombreRangoEdad) #Se agrega a la lista vacía los nombres y apellidos encontrados
    return nombreRango #Se retorna la función definida

# Llamar las funciones e imprimir el resultado
if __name__ == "__main__":
    #Se llama el archivo, se abre y se lee
    archivo = 'archivoJson.json'
    with open(archivo, 'r') as file:
        data = json.load(file)
    #Se solicita el ingreso del deporte que se desea averiguar
    deporteIngresado = input("Ingrese el nombre del deporte (Con buena ortografía): ")
    print("Nombres de personas que practican "+str(deporteIngresado)+": ")
    nombresCompletos = NombresDeporte(data, deporteIngresado) #Se llama la función definida
    print(nombresCompletos) #Imprimimos el resultado
    # Se solicita el ingreso del rango de edad que se desea averiguar
    edadMinima = int(input("Ingrese la edad mínima: "))
    edadMaxima = int(input("Ingrese la edad máxima: "))
    print("Personas dentro del rango de edad de "+str(edadMinima)+" años a "+str(edadMaxima)+" años: ")
    nombreRango = NombresRangoEdades(data, edadMinima, edadMaxima) #Se llama la función definida
    print(nombreRango) #Imprimimos el resultado


