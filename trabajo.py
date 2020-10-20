import math

from datetime import date
from datetime import datetime

#print('1) Calcular el area de un triangulo ')
#b = input('Ingrese la base ')
#a = input('Ingrese la Altura ')

#res = (float(b) * float(a)) / 2


#print("El area del triangulo es " + str(res) + '\n')



#print('2) Conversion de moneda')

#dolar = input('Ingrese el la cantidad de dolares ')

#cambio = int(dolar) * 3700

#print('Los ' + str(dolar) + ' dolares, equivalen a ' + str(cambio) + ' pesos Colombianos \n') 


# ---------------------------------------------------------------------------------------------------------- 

#print('3) Convertir centigrados a Fahrenheit ')

#centi = input('Ingrese los centigrados a cambiar ')

#faren = float(centi) * 32

#print('Los ' + str(centi) + ' grados centigrados equivalen a ' + str(faren) + ' grados Fahrenheit \n' )

#print('4) Cantidad de segundos que tiene un lustro \n')

#print('Un lustro equivale a 157680000 segundos \n')

# ---------------------------------------------------------------------------------------------------------- 

#print('5) Viaje de la luz del sol a marte ')

#DISTANCIA_SOL_MARTE = 206700000
#VELOCIDAD_LUZ = 299708

#segun = int(DISTANCIA_SOL_MARTE) / int(VELOCIDAD_LUZ)

#print('Distancia del sol a marte ' + str(DISTANCIA_SOL_MARTE) + 'Km')
#print('Velocidad de la luz ' + str(VELOCIDAD_LUZ) + 'Km/s ')

#print('El tiempo que tarda en llegar la luz del sol a marte es de unos ' + str(segun) + ' segundos \n')

# ---------------------------------------------------------------------------------------------------------- 

#print('6) Numero de vueltas que da una llanta ')

#print('Cantidad de metros = 1000')
#print('Diametro de la llanta = 50')

#vueltas = 1000/50

#print('La cantidad de vueltas que da la llanta es ' + str(int(vueltas)) + ' \n')

# ---------------------------------------------------------------------------------------------------------- 

#print('7) Longitud de la sombra de un edificio')

#print('Ecuacion de la sombra del edificio es Tan 22 = opuesto / 20m \n')

## Primero se convierten los grados a radianes

#rad = float(0.0174533) * 22

#sombra = math.tan(rad) * 20

#print('La sombra que proyecta el edificio con los rayos del sol es ' + str(float(sombra)) + ' metros \n')


# ---------------------------------------------------------------------------------------------------------- 

#print('8) Edad ingresadas son iguales')

#edad1 = int(input("Digite la primera edad "))
#edad2 = int(input("Digite la segunda edad "))

#if edad1 == edad2:
#    print('True')
#else:
#    print('False')


# ---------------------------------------------------------------------------------------------------------- 

print('10) Promedio de un alumno')

nota1 = float(input("Ingrese la nota de Español "))
nota2 = float(input("Ingrese la nora de Matematicas "))
nota3 = float(input("Ingrese la nota de Economia "))
nota4 = float(input("Ingrese la nota de Programacion "))
nota5 = float(input("Ingrese la nota de Ingles \n"))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("El promedio de las notas del alumno es de " + str(float(promedio)) + " ")






