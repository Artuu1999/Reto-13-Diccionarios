# Reto #13 Diccionarios
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de los diccionarios dentro de nuestra clase de programación de computadores.
## Ejemplo No. 1
Crear un código que permita ingresar un diccionario y posteriormente imprimir de manera ascendente los valores de dicho diccionario
El código solución es el siguiente:
```sh
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
```
El programa al correrlo se ve de la siguiente manera:

![image](https://github.com/Artuu1999/Reto-13-Diccionarios/assets/124615034/ad9cfc9b-a63f-4746-b058-0e62ebf27848)


## Ejemplo No. 2
Crear un algoritmo que permita al usuario ingresar dos diccionarios y que posteriormente mezcle los dos diccionarios ingresados por el usuario en otro diccionario.
El código solución es el siguiente:
```sh
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
```
El programa al ejecutarse se ve así:

![image](https://github.com/Artuu1999/Reto-13-Diccionarios/assets/124615034/09d008b1-a76f-49d4-9c17-80244bbc819f)

## Ejemplo No. 3
Procesar el siguiente archivo JSON y diseñar un código que al ejecutarse solicite el ingreso de un deporte y un rango de edad, y así mismo imprima las personas que práctican el deporte ingresado y las personas que se encuentran dentro del rango de edad ingresado:
```JSON
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "Daz Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["Futbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
La solución al problema planteado es el siguiente:
```sh
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
```
El código al ejecutarse se ve de la siguiente manera:

![image](https://github.com/Artuu1999/Reto-13-Diccionarios/assets/124615034/d2c6eb85-a3e4-4494-8435-19179ca8011e)


## Ejemplo No. 4
El siguiente código contiene un JSON con el pronostivo detallado del clima para 8 días:
Revise los campos: 'alertAlertas', 'alertPrecip', 'alertTmpMax', 'alertTmpMin', 'alertVelViento'. Para cada uno identifique si se presentan alertas ({0: x} indica que el día 0 habra un fenomeno de la alerta en cuestión, {1:"-"} indica que no habrá ningun fenomeno climatico). En caso que se presente una alerta obtenga la fecha del campo 'dt' (aquí pueden revisar como se convierte de UTC a fecha), así como los parametros relevantes del evento (e.g. si es un fenomeno de lluvias, busqye el nivel de lluvia, si es vientos, la velocidad del viuento). Al final deberá imprimir las fechas de alerta, el tipo de alerta y las variables asociadas.
El código solución es el siguiente:
```sh
import json
from datetime import datetime
jsonString = '''
{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"sunrise\": {\"0\": 1685097348, \"1\": 1685183745, \"2\": 1685270143, \"3\": 1685356542, \"4\": 1685442942, \"5\": 1685529342, \"6\": 1685615743, \"7\": 1685702145}, \"sunset\": {\"0\": 1685143042, \"1\": 1685229458, \"2\": 1685315875, \"3\": 1685402291, \"4\": 1685488708, \"5\": 1685575124, \"6\": 1685661541, \"7\": 1685747958}, \"moonrise\": {\"0\": 1685118300, \"1\": 1685207460, \"2\": 1685296620, \"3\": 1685385720, \"4\": 1685474880, \"5\": 1685564220, \"6\": 1685653740, \"7\": 1685743500}, \"moonset\": {\"0\": 0, \"1\": 1685164320, \"2\": 1685253000, \"3\": 1685341560, \"4\": 1685430120, \"5\": 1685518740, \"6\": 1685607600, \"7\": 1685696640}, \"moon_phase\": {\"0\": 0.22, \"1\": 0.25, \"2\": 0.28, \"3\": 0.31, \"4\": 0.35, \"5\": 0.38, \"6\": 0.41, \"7\": 0.45}, \"pressure\": {\"0\": 1011, \"1\": 1012, \"2\": 1012, \"3\": 1012, \"4\": 1012, \"5\": 1012, \"6\": 1012, \"7\": 1011}, \"humidity\": {\"0\": 85, \"1\": 61, \"2\": 68, \"3\": 74, \"4\": 84, \"5\": 66, \"6\": 81, \"7\": 82}, \"dew_point\": {\"0\": 23.93, \"1\": 22.5, \"2\": 23.67, \"3\": 23.35, \"4\": 24.22, \"5\": 22.73, \"6\": 22.58, \"7\": 24.02}, \"wind_speed\": {\"0\": 2.94, \"1\": 2.95, \"2\": 2.88, \"3\": 2.76, \"4\": 2.77, \"5\": 2.97, \"6\": 2.94, \"7\": 2.79}, \"wind_deg\": {\"0\": 196, \"1\": 182, \"2\": 182, \"3\": 177, \"4\": 183, \"5\": 193, \"6\": 195, \"7\": 181}, \"weather\": {\"0\": {\"id\": 804, \"main\": \"Clouds\", \"description\": \"overcast clouds\", \"icon\": \"04n\"}, \"1\": {\"id\": 500, \"main\": \"Rain\", \"description\": \"light rain\", \"icon\": \"10d\"}, \"2\": {\"id\": 803, \"main\": \"Clouds\", \"description\": \"broken clouds\", \"icon\": \"04d\"}, \"3\": {\"id\": 803, \"main\": \"Clouds\", \"description\": \"broken clouds\", \"icon\": \"04d\"}, \"4\": {\"id\": 804, \"main\": \"Clouds\", \"description\": \"overcast clouds\", \"icon\": \"04n\"}, \"5\": {\"id\": 803, \"main\": \"Clouds\", \"description\": \"broken clouds\", \"icon\": \"04n\"}, \"6\": {\"id\": 803, \"main\": \"Clouds\", \"description\": \"broken clouds\", \"icon\": \"04n\"}, \"7\": {\"id\": 803, \"main\": \"Clouds\", \"description\": \"broken clouds\", \"icon\": \"04d\"}}, \"clouds\": {\"0\": 100, \"1\": 100, \"2\": 66, \"3\": 64, \"4\": 98, \"5\": 67, \"6\": 83, \"7\": 60}, \"pop\": {\"0\": 0, \"1\": 0.2, \"2\": 0, \"3\": 0, \"4\": 0.4, \"5\": 0, \"6\": 0, \"7\": 0}, \"uvi\": {\"0\": 0, \"1\": 1.36, \"2\": 2.29, \"3\": 1.85, \"4\": 0, \"5\": 1.89, \"6\": 2.24, \"7\": 1.42}}
'''
data = json.loads(jsonString)
numereCord = len(data['dt'])
for x in range(numereCord):
    time = data['dt'][str(i)]
    sunriseTime = data['sunrise'][str(x)]
    sunsetTimesMode = data['sunset'][str(x)]

    date = datetime.fromtime(time)
    sunrise = datetime.fromtime(sunriseTime)
    sunset = datetime.fromtime(sunsetTimesMode)

    print(f"Registro {x+1}")
    print("Fecha y hora:", date)
    print("Amanecer:", sunrise)
    print("Atardecer:", sunset)
```

## Ejemplo No. 5
Diseñar un código, el cual se conecte a 3 [API's ](https://apipheny.io/free-api/), y se extraigan determinados valores de dichos archivos JSON.
A continuación la solución al ejemplo:
```sh
# Se instala requests y se importa junto con json
import requests
import json

# Definir función para obtener la nacionalidad del nombre a partir de la API
def informacionNacionalidad(nombre: str):
    url = 'https://api.nationalize.io'  # Definir la API en la variable URL
    clave = {'name': nombre}  # Se solicita el parámetro de nombre, que es en el que se basa la API
    valor = requests.get(url, params=clave)  # Se obtiene la llave y el valor
    print(valor.url)  # Se imprime la URL
    data = json.loads(valor.text)  # Convierte la respuesta de json a formato python
    return data  # Se retorna la función definida

# Definir función para obtener información del nombre a partir de la API
def informacionNombre(nombre: str):
    url = 'https://api.agify.io'  # Definir la API en la variable URL
    clave = {'name': nombre}  # Se solicita el parámetro de nombre, que es en el que se basa la API
    valor = requests.get(url, params=clave)  # Se obtiene la llave y el valor
    print(valor.url)  # Se imprime la URL
    data = json.loads(valor.text)  # Convierte la respuesta de json a formato python
    return data  # Se retorna la función definida

# Definir función para obtener una imagen de un perro a partir de la API
def imagenPerro():
    url = 'https://dog.ceo/api/breeds/image/random'  # Definir la API en la variable URL
    valor = requests.get(url)  # Se obtiene la llave y el valor
    print(valor.url)  # Se imprime la URL
    data = json.loads(valor.text)  # Convierte la respuesta de json a formato python
    imagen = data['message']  # Se extrae el link de la imagen del diccionario de la API data
    return imagen  # Se retorna la función definida

# Llamar las funciones e imprimir el resultado de cada diccionario de la API
if __name__ == "__main__":
    nombre = input("Ingrese un nombre: ")
    respuesta = informacionNacionalidad(nombre)
    print("Información de la nacionalidad del nombre " + str(nombre) + ": ")
    print(json.dumps(respuesta, indent=2))
    respuesta = informacionNombre(nombre)
    print("Información general del nombre " + str(nombre) + ": ")
    print(json.dumps(respuesta, indent=2))
    imagen = imagenPerro()
    print("Imagen de perro: ")
    print(imagen)
```
El código funcionando se obseva de la siguiente manera:

![image](https://github.com/Artuu1999/Reto-13-Diccionarios/assets/124615034/db4927be-bc74-452d-a054-f421b6991fc4)



