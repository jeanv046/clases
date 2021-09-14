# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 19:05:48 2021

@author: Jean Vega
"""

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

#Tabla del or
# v or x = v
# v or f = v
# f or v = v
# f or f = f

print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

# Negacion

print(not True) #False
print(not False) #True

# Mas de dos condiciones al mismo tiempo 
print(True and False and True or False or True or False) #True
print(True and (False and True) or False or (True or True))#True

#Jerarquia de operaciones
#1. Parentesis y llaves
#2. Potencias y raices
#3. Multiplicacion y division
#4. Sumas y restas

#Jerarquia de operaciones booleanas
#1. Parentesis y llaves
#2. Tabla de verdad


#Estructura if
x = 1
if(x > 0):
    print('1')
else:
    print('2')
    print('3')


#Haga un algoritmo que dada la edad de una persona indique si es mayor
# o menor de edad.
edad = int(input("Digita tu edad: "))

if(edad >= 18):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad.")


#indique si aprobo o no el estudiante
#sabiendo que aprueba de 3.0 hasta 5.0
nota = float(input("Digita tu nota: "))

if(nota >= 3.0 and nota <= 5.0):
    print("aprobaste")
elif (nota < 3.0 and nota > 0):
    print("Reprobasate")
else:
    print("Digite una nota valida")


#HUA que dado un numero n diga si es negativo, positivo o cero
numero = float(input("Digita un número: "))

if(numero > 0):
    print("Es positivo")
elif(numero == 0):
    print("Su número es 0")
else:
    print("Es negativo")

#ciclos

#ciclo for
for valor in range(11):
    print(valor)

for valor in range(1, 11): 
    print(valor)

for valor in range(2, 11, 2):
    print(valor)



#HUA que de las n notas de un estudiante y sacar el promedio final
#Hola Jean
num = int(input("Cuantas notas va a digitar?: "))
if(num > 0):
    suma = 0
    for x in range(num):
        nota = float(input(f"Digite la nota {x + 1}: "))
        suma = suma + nota
    promedio = suma / num
    promedio = round(promedio, 2)
    print(f"El promedio final es: {promedio}")
else:
    print("El numero de notas no puede ser menor que 0")















