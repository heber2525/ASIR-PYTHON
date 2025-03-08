#Len -longitud
import math
import random

nombre = "Mario Flores"
print("Longitud del nombre", len(nombre))

#May y Min
print("Quiero tener mi nombre en mayúsculas: ", nombre.upper())
print("Quiero tener mi nombre en mayúsculas: ", nombre.lower())

#Slicing.
#los 3 primeros
print("Los primeros 3 caracteres de mi nombre: ", nombre[:3])
#los 4 ultimos
print("Los primeros 3 caracteres de mi nombre: ", nombre[-4:])

#Reemplazar
frase = "Me encanta Java"
print("Quiero cambiar un palbra: ", frase.replace("Java", "Ptyhon"))
print("Impresion tras reemplazo de palabra", frase)

#Verificar si una cadena tiene o contiene a otra
print("Python" in frase)
nueva_frase= "Me gusta Python"
print("Python"in nueva_frase)

#Unir varias palabras
palabras = ["Hola", "mundo", "Python"]
print("La frase completa es :", " ".join(palabras))

#Dividir una cadena de partes
oracion = "Python es divertido"
palabras = oracion.split()
print(("Lista de palabras", palabras))

#Redondear numero decimal
numero = 3.1416
print("El numero PI redondeo: ", round(numero, 1))

#Formatear numeros con decimales
precio = 19.99
print("Precios con dos decimales: {:.2f}". format(precio))

#obtener el valor


#obtener raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25** 0.5) #no se utiliza
numero_raiz = 16
raiz_numero = math.sqrt(numero_raiz)
print("Raiz cuadrada del numero es:", raiz_numero)

#Divisiones restos y modulos
print("División normal", 10/3)
print("Divisiòn entera", 10//3)
print("Resto: ", 10%3)
print(1)
print(2)
print(3)

#Generar numeros aleatorios
print("Número aleatorio del 1 al 10: ", random.randint(1, 10))

#Convertir numero a cadena
numero_a_cadena = 100
texto = str(numero_a_cadena)
print("Convertido numero a cadena: ", texto)

cadena_a_numero = "200"
numero_a_cadena = int(cadena_a_numero)
print("Convertido numero a cadena: ", numero_a_cadena)

#Redondear siempre hacia arriba
print("Redondeo hacia arriba del numero 3.2: ", math.ceil(3.2))
print("Redondeo hacia arriba del abajo 3.2: ", math.floor(3.2))

#Convertir una lista en un conjunto (eliminado duplicados)
numeros = [1,2,2,3,4,4,5]
sin_duplicados = set(numeros)
print("Lista sin duplicados", sin_duplicados)

#Obtener el tipo de una variable
dato = 9.98
print(("Tipo de dato: ", type(dato)))
print(("Tipo de dato: ", type(dato)))

#Combinar cadenas y variables en un print
nombreProfe= "Mario"
edad=32
print(f"Hola soy {nombreProfe} y tengo {edad} años")


