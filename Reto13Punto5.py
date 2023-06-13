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

  

