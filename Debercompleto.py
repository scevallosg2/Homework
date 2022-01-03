# Tipos de Datos y Acciones elementales 
#Ejercicio°1 

S = ("Hola mundo", "" , "Verdadero", "1", "c", "256", "8>19" )
print(S)

#Ejercicio°2

respuesta = 2 *(4 - 10 + 8)/2* 36 *(1/2)
print(respuesta)
print(type(respuesta))

#Ejercicio°4

nume1 = 5
nume2 = 7

sum = nume1 + nume2
resta = nume1 - nume2
multip = nume1 * nume2
divi = nume1 / nume2
modlo = nume1 % nume2

print(sum)
print(resta)
print(multip)
print(divi)
print (modlo)

#Ejercicio°5
from math import sqrt
a = 20
b = 6
c = 9
d = 0
e = 0
if ((b**2)-4*a*c) < 0:
     print("Solución de la ecuación incluye números complejos")
else:
    d = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    e = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    print("Soluciones de la ecuación:")
    print(d)
    print(e)

print("Soluciones: ", d , e)

#Ejercicio°6
import math
cate1 = float(input("Ingrese cateto 1: "))
cateto2 = float(input("Ingrese cateto 2: "))

hipotenusa  = math.sqrt((cate1**2) + (cate2**2))
print("Hipotenusa: ", hipotenusa)

#Ejercicio°7

a = int(input("Ingresar un número: "))
if a % 2 == 0:
    print("0")
else:
    print("1")

#Ejercicio°9

lista=[]
for x in range(4):
    val=int(input("Ingrese un valor entero: "))
    lista.append(val)

repe = lista.count(1)
if repe % 2 == 0:
    print("El codigo de paridad es 1")
else:
    print("El codigo de paridad es 0")

#Ejercicio°10

a = '1010'

n = 0

for pos, dgt_string in enumerate(a[::-1]):
	n += int(dgt_string) * 2 ** pos

print(f'El número decimal es {n}')

#Ejercicio°11

numero = int(input("Ingresar numero entero de 4 cifras: "))
u = numero / 1000
t = numero % 1000

cent = t / 100
t = t % 100

d = t / 10
unid = t % 10

print("Unidades de mil : %i" % u)
print("Centenas: %i" % cent)
print ("Decenas: %i" % d)
print("Unidades: %i" % unid)
