# Reto #13 Diccionarios
Espero que se encuentren excelente estimados lectores, en el presente repositorio haremos varios ejemplos de código en Python utilizando lo aprendido acerca de los diccionarios dentro de nuestra clase de programación de computadores.
## Ejemplo No. 1
Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
El código solución es el siguiente:
```sh
def crearDiccionario():
    diccionario = {}
    tamaño = int(input("Ingrese el tamaño del diccionario: "))
    for i in range(tamaño):
        clave = input("Ingrese la clave: ")
        valor = float(input("Ingrese el valor (Números): "))
        diccionario[clave] = valor
    return diccionario

def ordenAscendente(diccionario):
    diccionarioOrden = sorted(diccionario.items(), key=lambda x: x[1])
    return diccionarioOrden

if __name__ == "__main__":
    diccionario = crearDiccionario()
    diccionarioOrden = ordenAscendente(diccionario)
    print("El diccionario ingresado fue: ")
    print(diccionario)
    print("El diccionario ingresado en orden ascendente es el siguiente: ")
    print(diccionarioOrden)

```

## Ejemplo No. 2
Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
El código solución es el siguiente:
```sh
def crear_diccionario1():
    diccionario1 = {}
    tamaño = int(input("Ingrese el tamaño del diccionario 1: "))
    for i in range(tamaño):
        clave = input("Ingrese la clave: ")
        valor = input("Ingrese el valor: ")
        diccionario1[clave] = valor
    return diccionario1

def crear_diccionario2():
    diccionario2 = {}
    tamaño = int(input("Ingrese el tamaño del diccionario 2: "))
    for i in range(tamaño):
        clave = input("Ingrese la clave: ")
        valor = input("Ingrese el valor: ")
        diccionario2[clave] = valor
    return diccionario2

def mezclar_diccionarios(diccionario1, diccionario2):
    nuevo_diccionario = diccionario1.copy()
    nuevo_diccionario.update(diccionario2)
    return nuevo_diccionario

if __name__ == "__main__":
    print("Primer diccionario:")
    diccionario_1 = crear_diccionario1()
    print(diccionario_1)

    print("Segundo diccionario:")
    diccionario_2 = crear_diccionario2()
    print(diccionario_2)

    diccionario_mezclado = mezclar_diccionarios(diccionario_1, diccionario_2)

    print("Diccionario mezclado:")
    print(diccionario_mezclado)

```

## Ejemplo No. 3
Dado el JSON:
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
 Cree un programa que lea de un archivo con dicho JSON y: 
 - Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
 - Imprima los nombres completos (nombre y apellidos) de las personas que esten en un rango de edades dado por el usuario.
El código solución es el siguiente:
```sh
import json

def Json(archivo):
    with open(archivo, 'r') as file:
        data = json.load(file)
    return data
def NombresDeporte(data, deporte):
    for usuario, info in data.items():
        if deporte in info['deportes']:
            nombres = info['nombres']
            apellidos = info['apellidos']
            nombreCompleto = f"{nombres} {apellidos}"
            print(nombreCompleto)
def NombresRangoEdades(data, edadMin, edadMax):
    for usuario, info in data.items():
        edad = info['edad']
        if edadMin <= edad <= edadMax:
            nombres = info['nombres']
            apellidos = info['apellidos']
            nombreCompleto = f"{nombres} {apellidos}"
            print(nombreCompleto)

ArchivoJson = 'datos.json'
data = Json(archivoJson)

deporteIngresado = input("Ingrese el nombre del deporte : ")
print("Nombres de personas que practican", deporteIngresado)
NombresDeporte(data, deporteIngresado)

edadMinima = int(input("Ingrese la edad mínima: "))
edadMaxima = int(input("Ingrese la edad máxima: "))
print("Nombres de personas en el rango es de ", edadMinima, "a", edadMaxima)
NombresRangoEdades(data, edadMinima, edadMaxima)
```

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
A través de un programa conectese a al menos 3 [API's ](https://apipheny.io/free-api/), obtenga el JSON, imprimalo y extraiga los pares de llave : valor.
Primera  API:
```sh
import json
import requests

url = 'https://api.agify.io'

def obtenerInformacionPorNombre(nombre: str):
    params = {'name': nombre}
    peticion = requests.get(url, params=params)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    return data

if __name__ == "__main__":
    nombre = input("Ingrese la llave: ")
    respuesta = obtenerInformacionPorNombre(nombre)
    print("Información para el nombre:", nombre)
    print(json.dumps(respuesta, indent=2))
```
Segunda  API:
```sh
import requests
import json

url = 'https://dog.ceo/api/breeds/image/random'

def obtenerImagenPerro():
    peticion = requests.get(url)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    imagen = data['message']
    return imagen

if __name__ == "__main__":
    imagen_perro = obtenerImagenPerro()
    print("Imagen aleatoria de perro:")
    print(imagen_perro)
```
Tercera  API:
```sh
import requests
import json

url = 'https://api.nationalize.io'

def obtenerInformacionNacionalidad(nombre: str):
    params = {'name': nombre}
    peticion = requests.get(url, params=params)
    print(peticion.url)
    print(peticion.status_code)

    data = json.loads(peticion.text)
    return data

if __name__ == "__main__":
    nombre = input("Ingrese el nombre: ")
    respuesta = obtenerInformacionNacionalidad(nombre)
    print("Información de nacionalidad para el nombre:", nombre)
    print(json.dumps(respuesta, indent=2))
```
