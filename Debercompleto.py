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

#Estructuras de Control de Flujo de Datos

#Ejercicio°1

year = 0
lista_1 = []
def string_int(m_info):
    for b in m_info:
        lista_1.append(int(a))
p_f = input("Ingresar fecha en formato (ddmmaaaa): ")
string_int(p_f)

w = lista_1
x = lista_1[6]
y = lista_1[5]
z = lista_1[4]

if year % 4 != 0:
    print("Año No bisiesto")
elif year % 4 == 0 and year % 100 != 0:
    print("Año bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
    print("Año No bisiesto")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print("Año bisiesto")


#Ejercicio°2 

list_1 = []

def string_int(mi_inform):
    for h in mi_inform:
        list_1.append(int(h))

p_nume = input("Ingresar numero entero de 5 digitos: ")
string_int(p_nume)

m = list_1[0]
n = list_1[1]
o = list_1[2]
p = list_1[3]
q = list_1[4]

if m == q:
    if n == p:
        print("El número es capicúa")
    else:
        print("El número NO es capicúa")
else:
    print("El número no es capicúa")
    
#Ejercicio°3

hour = int(input("Ingresar la cantidad de horas: "))
minutes= int(input("Ingrresar la cantidad de minutos: "))

h_a_s = hour * (3600)
m_a_s = min *(60)
total_seg = h_a_s +m_a_s

print("El total de segundos es: ", total_seg)

#Ejercicio°4

sgds = int(input("Ingresar los segundos: "))

if sgds> 0 :
    min = sgds / 60
    hora = sgds / 3600
    d = sgds / 86400

    print("\n La cantidad de minutos es: ", min)
    print("\n La cantidad de horas es: ", hora)
    print("\n La cantidad de días es: ", d)
else:
    print("Ingresar una cantidad de segundos válida")

#Ejercicio°5

X = int(input("Ingresar el primero entero positivo: "))

if X > 0:
    Y = int(input("Ingrese el el segundo entero positivo: "))
    if Y > 0:
        Z = int(input("Ingrese el Tercer entero positivo: "))
        if Z > 0:
            if X > Y and X > Z:
                print("\n El mayor es: ", X)
                if Y > Z:
                    print("\n El segundo mayor es: ", Y)
                else:
                    print("\n El segundo mayor es: ", Z)
            elif Y > X and Y > Z:
                print("\n EL numero mayor es: ", Y)
                if X > Z:
                    print("\n El segundo mayor es: ", X)
                else: 
                     print("\n El segundo mayor es: ", Z)
            elif Z > X and Z > Y:
                print("\n EL numero mayor es: ", Z)
                if X > Y:
                    print("\n El segundo mayor es: ", X)
                else:
                    print("\n El segundo mayor es: ", Y)
            else:
                print("No se ha podido deteerminar el mayor de los 3 numeros") 
        else:
            print("Por favor ingrese un numero entero positivo")
    else:
        print("Por favor ingrese un numero entero positivo")
else:
    print("Por favor ingrese un numero entero positivo")

#Ejercicio°6

horas_e = int(input("Ingrese las horas en formato de 12 en la que se estaciono:"))
if horas_e >= 0 and horas_e <= 12:   
    min_e = int(input("Ingrese el o los minutos en la que se estaciono: "))   
    if min_e >= 0 and min_e < 60: 
        am_pm_e  = input("SI usted se estaciono en la mañana ingrese la letra A y si ingreso pasado del medio dìa ingrese la letra P: ") 
        if am_pm_e == "A" or am_pm_e == "P" :
            horas_s = int(input("Ingrese la hora en formato de 12 en la que sale del estacionamiento: "))
            if horas_s >= 0 and horas_s <= 12:
                s_s= int(input("Ingrese la hora en la que sale del estacionamiento: ")) 
                if s_s >= 0 and s_s < 60:
                    am_pm_sale = input("SI usted sale del estacionamiento en la mañana ingrese la letra A y si salio pasado del medio dìa ingrese la letra P: ")
                    if am_pm_sale == "A" or am_pm_sale == "P" :
                        if am_pm_e == "A" and am_pm_sale == "A" or am_pm_e == "A" and am_pm_sale == "P" or am_pm_e == "P" and am_pm_sale == "P":
                            if am_pm_e == "A" and am_pm_sale == "A" or am_pm_e == "P" and am_pm_sale == "P":
                                res_H = horas_e - horas_s
                                T_Horas = res_H * 4
                                res_M = min_e - s_s
                                T_Min = res_M/30
                                T_Min_2 = 0
                                if T_Min < 0 :
                                    T_Min_2 = 2.50
                                    T_Tiempo = T_Horas + T_Min_2
                                    print("El Valor a pagar es: Bs", T_Tiempo)
                            elif am_pm_e == "A" and am_pm_sale == "P":
                                horas_s+=12
                                rest_Horas = horas_e - horas_s
                                Total_Horas = rest_Horas * 4
                                rest_min = min_e - s_s
                                Total_Min = rest_min/3
                                Total_Min_2 = 0
                                if Total_Min < 0 :
                                    Total_Min_2 = 2.50
                                    Total_Tiempo = Total_Horas + Total_Min_2
                                    print("El Valor a pagar es: Bs", Total_Tiempo)
                        else:
                            print("Los datos de entrada y salida no coinciden")
                    else:
                        print("Ingrese una Letra Valida")
                else:
                    print("Ingrese unos minutos de salida valido")        
            else:
                print("Ingrese una hora de salida valida")
        else:
            print("Ingrese una letra valida")    
    else:
        print("Ingrese una cantidad de minutos valido")   
else:
    print("Ingrese una hora de entrada valida")

#Ejercicio°7

libs = float(input("Ingrese su peso en Libras: "))
cm = int(input("Ingrese su Altura en Centimetros: "))

peso = libs*0.453592
altura = cm /100

promed = peso/(altura * altura)

print("Su peso en Kg es: ", peso)
print("Su altura en Metros es: ", altura)
print("Su promedio es: ", promed)

if promed < 16 :
    print("Su categoria es Criterio de ingreso.")
elif promed >= 16 and promed <= 16.9:
    print("Su categoria es infra peso.")
elif promed >= 17 and promed <= 18.4:
    print("Su categoria es bajo peso.")
elif promed >= 18.5 and promed <= 24.9:
    print("Su categoria es peso normal.")
elif promed >= 25 and promed <= 29.9:
    print("Su categoria es sobrepeso.")
elif promed >= 30 and promed <= 34.9:
    print("Su categoria es obesidad pre-mórbida.")
elif promed >= 40 and promed <= 45:
    print("Su categoria es obesidad mórbida.")
elif promed > 45 :
    print("Su categoria es obesidad híper-mórbida.")

#Ejercicio°8

a = int(input("Ingrese un dia correspondiente al 2014: "))
if a > 0 and a < 31:
    mes = int(input("Ingrese un numero de mes correspondiente al 2014: "))
    if mes > 0 and mes <=12 :
        dia_Mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x = 0
        acum = 0
        while x <= mes - 1:
            acum = acum + dia_Mes[x]
            i = i + 1
        total = acum + a
        print("\n EL total de dias que han pasado desde el 1 de enero del 20154 hasta la fecha que se pide es: ", total)

#Ejercicio°9

mes = int(input("Ingresar un numero entre el 1 y el 12: "))
if mes > 0 and mes <= 12 :
    if mes == 1 :
        print("Enero")
    elif mes ==2 :
        print("Febrero")
    elif mes ==3 :
        print("Marzo")
    elif mes ==4 :
        print("Abril")
    elif mes ==5 :
        print("Mayo")
    elif mes ==6 :
        print("Junio")
    elif mes ==7 :
        print("Julio")
    elif mes ==8 :
        print("Agosto")
    elif mes ==9 :
        print("Septiembre")
    elif mes ==10 :
        print("Octubre")
    elif mes ==11:
        print("Noviembre")
    elif mes ==12 :
        print("Diciembre")       
else:
    print("Ingrese un numero valido")

#Ejercicio°10

a = float(input("Ingrese la cantidad a pagar en el almacen: "))

if a > 1000:
    tt = a * 0.80
    print("SU total a pagar aplicando el descuento de la tienda es de: Bs", tt)
else:
    print("Su total a pagar es de: Bs", a)

#Estructuras Iterativas

#Ejercicio°1

import math
nume = int(input("Ingrese un número entero: "))
if nume > 0:
    digi = int(math.log10(nume))+1
    print(digi)
elif nume == 0:
    digi = 1
    print(digi)
elif nume < 0:
    print("Ingrese un número válido")

#Ejercicio°2

def inver_numero(a):
    n3 = 0
    while a!= 0:
        n3 = 10*n3+a % 10
        a //= 10
    return n3

def cap(n3):
    return n3 == inver_numero(n3)

nums = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for n3 in nums:
    es_cap = cap(n3)
    print(f"El número {n3} es capicúa? {es_cap}")

#Ejercicioº3

def es_p(n4):
    cont = 0

    for a in range(1, n4+1):
        if n4 % a == 0:
            cont += 1
    
    if cont == 2:
        print("Es un numero primo")
        return True
    else:
        print("No es un numero primo")
        return False
n5 = int(input("Ingrese un numero primo positico: "))
if n5 > 0:
    print(es_p(n5))  

#Ejercicio°4

T = int(input("Ingrese un numero entero: "))
if T >= 0 :
    U = 1
    V = 1
    while U <= T:
        V = V *U 
        U += 1
    print("El factorial de ",T," es: ",V)
else:
    print("No se pudo calcular el factorial")

#Ejercicio°5

def vali(valor):
    	return False

va = 0
while not va:
    contra = input("Introduzca la contraseña con al menos 10 digitos: ")
    v = len(contra) >= 10
print("\n Felicidades has ingresado una contraseña correcta")

#Ejercicio°6

def secuencia_menor_mayor():
    ingresa = True
    lista = []
    while ingresa:
        valor = int(input("Ingresa un valor o 0 para finalizar, debe ser un valor entero: "))
        if valor == 0:
            break
        else:
            lista.append(valor) 
    print(lista)
    print(u'Menor %s' % min(lista)) 
    menor = lista[0] 
    mayor = lista[0] 
    for elemento in lista: 
        if elemento < menor: 
            menor = elemento
    for elemento in lista:
        if elemento > mayor:
            mayor = elemento
    print(u'Menor %s' % menor)
    print(u'Mayor %s ' % max(lista))
    print(u'Mayor %s ' % mayor)

#Ejercicio°7

def secuencia(self):
            e=[18,24,25,30,35,36]
            p=[40,50,60,70,80]
            esta=[1.40,1.45,1.50,1.55,1.60,1.70]
            p_edad=(sum())/len()
            p_peso=(sum(p))/len(p)
            p_es=(sum(p))/len(esta)
            c=0
            x=0
            while c<8:
                x+=(p_edad.count(18+c))
                c+=1  
            c=1
            mayores_36=0  
            while c<150:
                mayores_36+=(p_edad.count(36+c))
                c+=1
            c=0
            freire=0
            while c<36:
                freire=[i for i,x in enumerate(p_edad) if x>=18 and x<=35]
                c+=1
            suma=0
            c=0
            while c<len(freire):
                suma+=p[freire[0+c]]
                c+=1
            print(freire)
            print("El promedio de la edad :", p_edad)
            print("El promedio del peso : ", p_peso)
            print("El promedio de la  estatura : " ,p_es)
            print("un rango entre 18 y 25 : ", x)
            print("Las personas mayores : " , mayores_36)
            print("El promedio de pesos de todas las personas : " , suma/len(freire))

#Ejercicio°8

def alg(self):
        for w in range (10):
            print("tabla de mult: "+str(w+1))
            for v in range (12):
                print(str(+1)+"*"+str(v+1)+"="+str(w+1)* (v+1))
                print ("\n")  

#ejercicio °9 y °10
def fichas(self):
        for o in range(0,7):
            for e in range(0, o+1):
                print("|" + str(o) + "|" + str(e) + "|")

def num_pos(self):
        c=0
        numeros_posi=0
        while True:
            nume=int(input("Ingresar solo  números positivos: "))
            if nume==0:
                break
            elif nume > 1:
                numeros_posi+=nume
                c+=1
                prome1=numeros_posi/c
            print("serie promedio : " ,prome1 )       

#Prodecimientos (Acciones y Funciones)

#Ejercicio°1

def edades_us(self):
        d=0
        e_ma=0
        while True:
            print("presione [enter] para dejar de ingresar notas!")
            edades=(input("ingrese las edades a promediar:"))
            if edades=='':
                break
            elif edades >= "18":
                edades=int(edades)
                e_ma+=edades
                d+=1
                pro=e_ma/d
        return pro

#Ejercicio°2

def Eleva(self):
    base=int(input("ingrese la base: "))
    ex=int(input("ingrese el exponente: "))
    ex= 2
    result=base**ex
    print(f"El resultado es: {result} ")

#Ejercicio°3

def pentagono(self):
    lado=float(input("Ingrese el valor de uno de los lados del pentágono:"))
    per=5*lado
    return per

#Ejercicio º4
def c_pago(horas, valor, extra=False):
    if extra:
        total = round(horas * valor, 2)
        return total + ((total*35) / 100.0)
    return round(horas * valor, 2)

def horas_extras():
    i = 1
    data = []
    datos = {}
    while i <= 5:
        empleado = input("Identificación del empleado: ")
        valor = float(input("Valor por hora, debe ser un valor numerico: "))
        horas = int(input("Horas laboradas, debe ser un valor entero: "))
        datos = {'identificacion': empleado, 'valor': valor, 'horas': horas}
        data.append(datos)
        i += 1
    for d in data:
        if int(d['horas']) <= 40:
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' %(d['identificacion'], d['valor'], d['horas'], 0, c_pago(d['valor'], d['horas']), 0))
        else:
            print(u'Empleado: %s, valor_hora: %s, horas_lab: %s, extras: %s, TOTAL_PAGO: %s, TOTAL_EXTRAS: %s' % (d['identificacion'], d['valor'], d['horas'], d['horas'] - 40, c_pago(d['valor'], 40), c_pago(d['valor'], int(d['horas']) - 40, True)))

#Ejercicio°5

def horas(self):
        def MillasAKm(mi):
            kilome=mi*1.60935
            return kilome
        ci=['']*12
        xyz=['A','B','','C','D','','F','G','','H','I']
        ind=0
        while ind<=11:
            if ind==0 or ind==1 or ind==3 or ind==4 or ind==6 or ind==7 or ind==9 or ind==10:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingresar la ciudad {xyz[0+ind]}: ")
                ind+=1
            else:
                while ci[ind]<='':
                    ci[ind]=input(f"Ingresar la distancia entre ciudades: ")
                ind+=1
        print(f"\nEntre {ci[0]} y {ci[1]}, hay {MillasAKm(int(ci[2])):.2f} Km de distancia\n")
        print(f"Entre {ci[3]} y {ci[4]}, hay {MillasAKm(int(ci[5])):.2f} Km de distancia\n")
        print(f"Entre {ci[6]} y {ci[7]}, hay {MillasAKm(int(ci[8])):.2f} Km de distancia\n")
        print(f"Entre {ci[9]} y {ci[10]}, hay {MillasAKm(int(ci[11])):.2f} Km de distancia\n")