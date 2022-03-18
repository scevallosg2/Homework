from datetime import date
class codigoEstr:

#Ejercicio 4
    def operadores (self):

        valor1 = int(input("Ingrese un número: "))
        valor2 = int(input("Ingrese un número: "))

        a = valor1 + valor2
        b = valor1 - valor2
        c = valor1 * valor2
        d = valor1 / valor2
        e = valor1 % valor2

        print ("El resultado de la suma es: {} ".format (a))
        print ("El resultado de la resta es: {} ".format (b))
        print ("El resultado de la multiplicación es: {} ".format (c))
        print ("El resultado de la división es: {} ".format (c))
        print ("El resultado de la módulo es: {} ".format (e))

#Ejercicio 5
    def resolvente (self):

        valor1 = int(input("Ingrese un valor de a : "))
        valor2 = int(input("Ingrese un valor de b : "))
        valor3 = int(input("Ingrese un valor de c: "))

        d = ((valor2)**2)-4*valor1*valor3
        
        if d > 0: 
            x1 = (-valor2 + (((valor2**2) - (4 * valor1 * valor3))**0.5)) / (2 * valor1)
            x2 = (-valor2 - (((valor2**2) - (4 * valor1 * valor3))** 0.5)) / (2 * valor1)
            return x1,x2 
        elif d == 0:
            x = -valor2/(2*valor1)
            return x
        else: 
            n = "No existe valores"
            return n

#Ejercicio 6
    def hipotenusa (self):

        valor1 = int(input("Ingrese uno de los catetos: "))
        valor2 = int(input("Ingrese el segundo cateto: "))

        return ((valor1 * valor1)+(valor2 * valor2))**0.5
    
#Ejercicio 7     
    def parOimpar (self):

        valor1 = int(input("Ingrese el segundo cateto: "))

        if valor1 % 2 == 0:  
            g = "0, par"  
            return g

        else: 
            f = "1, es impar"
            return f

#Ejercicio 9  
    def binarioBitparidad (self):

        numbinar = int(input("Ingrese un valor en formato binario de 4 dígitos: "))

        n1 = int(numbinar[0])
        n2 = int(numbinar[1])
        n3 = int(numbinar[2])
        n4 = int(numbinar[3])
        cont = n1 + n2 + n3 + n4
        if cont % 2 == 0:
            print ("El bit de paridad es cero")
        else:
            print ("El bit de paridad es 1")


#Ejericio 10 
    def binarioAdecimal (self):

        numbi = int(input("Ingrese un número binario (4 dígitos) para convertirlo a decimales: "))

        n1 = int(numbi[0])
        n2 = int(numbi[1])
        n3 = int(numbi[2])
        n4 = int(numbi[3])
        conversion = (n4 * 2**0) + (n3 * 2**1) + (n2 * 2**2) + (n1 * 2**3)
        print ("El número decimal es: ".format(conversion))

#Ejercicio 11
    def separarUnidades (self):

        convernum = int(input("Ingrese un número conformado por 4 dígitos: "))
    
        if convernum > 1000 and convernum < 9999:
            unidadesDemil = convernum // 1000
            print ("La unidad de mil es: ", unidadesDemil)
            centenas = (convernum - (unidadesDemil * 1000)) // 100
            print ("La centena es:", centenas)
            decenas = (convernum - (unidadesDemil * 1000) - (centenas * 100)) // 10
            print ("La decena es: ", decenas)
            unidad = (convernum - (unidadesDemil * 1000) - (centenas * 100) - (decenas * 10))
            print ("La unidad es: ", unidad)
        else: 
            print ("Ingrese un valor válido dentro del rango establecido ")

#Ejercicio 1 - Parte 2 
    def añoBisiesto (self):

        self.ddmmaaaa = int(input("Ingrese un año: "))

        año = self.ddmmaaaa % 1000
        día = self.ddmmaaaa // 1000000
        mes = (self.ddmmaaaa // 10000) % 100
        if ((año % 4 == 0) and (año % 100 != 0) or (año % 400 == 0)):
            print("Es un año bisiesto")
        else:
            print("Mp es un año bisiesto")

#Ejercicio 2 - Parte 2 
    def capicua (self):

        num_cap = int(input("Ingresar un número de 5 dígitos para conocer si es capicúa: "))

        if 9999 < num_cap < 99999:
            if str(num_cap) == str(num_cap) [::-1]:
                print ("Es capicúa")
            else: 
                print ("No es capicúa")
        else: 
            print ("Ingrese un número de 5 dígitos")

#Ejercicio 3 - Parte 2
    def horasMinutos (self):

        self.hora = int(input("Ingresa el tiempo en hora: "))
        self.minuto = int(input("Ingresa el tiempo en minutos: "))


        if 1 < self.hora < 24 and 1 < self.minuto < 1440:
            Hs = self.hora * 3600
            print("El equivalente de {} ".format (self.hora), "hora(s) a segundos es: {} ".format(Hs))
            Ms = self.minuto * 60
            print("El equivalente de {} ".format(self.minuto), "minuto(s) a segundos es: {} ".format(Ms))
        
        else:
            "Se excede del límite establecido"

#Ejercicio 4 - Parte 2 
    
    def convertirSegundos (self):

        self.num6 = int(input("Ingrese un valor en segundos: "))

        if self.num6 > 0: 
            conversionAminutos = self.num6/60
            minutos = round(conversionAminutos, 2) 
            print ("El valor en minutos es: ", minutos)

            conversionAhoras = self.num6/3600
            horas= round(conversionAhoras, 2) 
            print ("El valor en horas es: ", horas)

            conversionAdias = self.num6/86400
            dias = round(conversionAdias, 2) 
            print ("El valor en días es: ", dias)
        else:
            print ("Ingrese un valor mayor que 0")

#Ejercicio 5 - Parte 2 
    def Mayorque (self):

        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        num3 = int(input("Ingresa el tercer número: "))


        if num1 and num2 and num3 > 0:

            if num3 < num2 > num1:
                print("El primer mayor es: {} ".format(num2))
                if num1 > num3: 
                    print("El segundo mayor es: {} ".format(num1))
                else:
                    print ("El segundo mayor es: {} ".format(num3))
            elif num2 < num3 > num1:
                print("El primer mayor es: {} ".format(num3))
                if num1 > num2: 
                    print ("El segundo mayor es: {} ".format(num1))
                else: 
                    print ("El segundo mayor es: {} ".format(num2))

            elif num3 < num1 > num2:
                print("El primer mayor es: {} ".format(num1))
                if num2 > num3:
                    print ("El segundo mayor es: {} ".format(num2))

                else: 
                    print ("El segundo mayor es: {} ".format(num3))

            else:
                print("Todos son iguales ")
        else:
            print("Digite un número mayor a 0")

#Ejercicio 6 - Parte 2
    def estacionamiento (self):
        tiempoe = [0, 0, "", 0, 0, ""]
        tiempos = [0]*2
        pbs = ["Su hora de ingreso al estacionamiento es: ", "Los minutos excedentes de entrada", 2, "Hora de partida del estacionamiento", "Los minutos excedentes de salida", 5]
        ct = 0

        for i in pbs:
            if (ct != 2 or ct != 5):
                if (i != 2 and i != 5):
                    tiempoe[ct] = int(input("Ingrese {}: ".format(i)))
                ct += 1
            if ct == 2 or ct == 5:
                horario = input("La hora que ingresada, ¿Es A.M o P.M? ")
                tiempoe[(pbs[ct])] = horario

        tiempos[0] = (tiempoe[0] * 3600) + (tiempoe[1] * 60)
        tiempos[1] = (tiempoe[3] * 3600) + (tiempoe[4] * 60)

        if tiempoe[2] == tiempoe[5]:
            nhp = tiempos[1] - tiempos[0]
        else:
            nhp = (43200 - tiempos[0]) + tiempos[1]

        tiempos[0] = (nhp-(nhp % 3600)) / 3600
        tiempos[1] = (nhp%3600)/60
        print(tiempos)
        mp = tiempos[0] * 4

        if tiempos[1] >= 30:
            mp = mp + 2.50
        print("El dueño del vehículo deberá pagar Bs. ",mp)


#Ejercicio 7 - Parte 2 
    def pesoCorporal (self):

        mapersonal = int(input("Ingrese la masa de la persona: "))

        masa = mapersonal/2.205
        estatura = (self.estatu**2)

        IMC = masa/estatura

        if 16 < IMC < 16.9:
            print ("Infra peso")
        elif 17 < IMC < 18.4:
            print ("Bajo peso")
        elif 18.5 < IMC < 24.9:
            print ("Peso normal")
        elif 25 < IMC < 29.9:
            print ("Sobrepeso")
        elif 30 < IMC < 34.9:
            print ("Obesidad pre-móbida")
        elif 40 < IMC < 45:
            print ("Obesidad mórbida")  
        else:
            print ("Obesidad híper-móbida ")

#Ejercicio 8 - Parte 2
    def añoAdescu (self):

        self.mes = int(input("Ingresa el mes: "))
        self.dia = int(input("Ingresa el día: "))


        diaActual = date(2014, self.mes, self.dia)
        pasado = date(2014,1,1)
        diferenciaDedías = diaActual - pasado

        print("El tiempo transcurrido es de: {} ".format(diferenciaDedías.days), "desde el 1 de enero del 2014")

#Ejercicio 9 - Parte 2        
    def ConocerMes (self):

        self.mesd = int(input("Ingresa un número (del 1 hasta 12) que desea saber qué mes representa: "))

        if 1 <= self.mesd <= 12:

            if self.mesd == 1:
                print("El mes es enero")
            elif self.mesd == 2:
                print("El mes es febrero")  
            elif self.mesd == 3:
                print("El mes es marzo")
            elif self.mesd == 4:
                print("El mes es abril")
            elif self.mesd == 5:
                print("El mes es mayo")
            elif self.mesd == 6:
                print("El mes es junio")
            elif self.mesd == 7:
                print("El mes es julio")
            elif self.mesd == 8:
                print("El mes es agosto")
            elif self.mesd == 9:
                print("El mes es septiembre")
            elif self.mesd == 10:
                print("El mes es octubre")
            elif self.mesd == 11:
                print("El mes es noviembre")
            elif self.mesd == 12:
                print("El mes es diciembre")
        else: 
            print ("El valor no se encuentra dentro del rango establecido")

#Ejercicio 10 - Parte 2 
    def calcularDescuento (self):

        self.valor = int(input("Ingresa el precio de la compra: "))


        if self.valor > 1000: 
            desc = self.valor * 0.20
            precioApagar = self.valor - desc
            print("Su precio a pagar es de: {} ".format(precioApagar))
        else: 
            print("El precio original a pagar es de: {} ".format(self.valor))

#Ejercicio 1 - Parte 3 
    def digitosDeN (self):

        self.nen = int(input("Digitar un número para calcular sus dígitos: "))

        while 0 < self.nen >=0:
            digitos = len(str(self.nen))
            print("El número tiene: ", digitos, "dígitos")
            break

#Ejercicio 3 - Parte 3 
    def numeroPrimo (self):

        self.primo = int(input("Ingrese un número primo: "))


        for i in range (2, self.primo):
            if self.primo % i == 0:
                print("El número registrado es: {} ".format(self.primo),"no es primo")
            else: 
                print("El número: {} ".format(self.primo), "es primo")
            break
#Ejercicio 4 - Parte 3 
    def factorial (self):
        connum = int(input("Ingresa una contraseña conformada por 10 dígitos: "))

        while True:
            if connum < 0:
                print("No es posible calcular es facotiral")
            elif connum == 0:
                print("Su factorial es 1")
            else: 
                resultad1 = connum -1 
                while resultad1 > 0:
                    connum = connum * resultad1

                    resultad1 = resultad1 -1
                print("El factorial es: {} ".format(connum))
            break


#Ejercicio 5 - Parte 3 
    def clave (self):

        num3ontra = int(input("Ingresa una contraseña conformada por 10 dígitos: "))

        s = 0 
        while num3ontra > 0: 
            num3ontra //= 10
            s = s + 1
        if s == 10: 
            print ("Es una contraseña segura")
        else:
            print ("No es segura")

#Ejercicio 6 - Parte 3 
    def solicitar_ingreso (self):
        lista = []
        a = True 
        while a: 
            numAcac = int(input("Ingresar un número y si desea detener el proceso, digite un 0: "))
            if numAcac == 0:
                a = False 
            else: 
                lista.append(numAcac)
        mayor, menor = codigoEstr.mayor_menor(lista)
        if len(lista) > 0:
            print ("El número mayor es: ", mayor)
            print ("El número menor es: ", menor)
    def mayor_menor(lista): 
        mayor = 0
        menor = 99999
        for numAcac in lista: 
            if numAcac > mayor: 
                mayor = numAcac
            
            if numAcac < menor: 
                menor = numAcac
        return mayor, menor
#Ejercicio 7 - Parte 3

    def calculvariables(self):
        edad=[20,30,40,50,60,70]
        peso=[40,50,60,70,80,90]
        estatura=[1.40,1.50,1.60,1.70,1.80,1.90]
        prom_edad=(sum(edad))/len(edad)
        prom_peso=(sum(peso))/len(peso)
        prom_estatura=(sum(estatura))/len(estatura)
        c=0
        x=0
        while c < 8:
            x+=(edad.count(20+c))
            c+=1  
        c=1
        cal=0  
        while c<150:
            cal+=(edad.count(40+c))
            c+=1
        c=0
        contPos=0
        while c<36:
            contPos=[i for i,x in enumerate(edad) if x>=18 and x<=35]
            c+=1
        suma=0
        c=0
        while c<len(contPos):
            suma+=peso[contPos[0+c]]
            c+=1
        print(contPos)
        print(f"El promedio de edades de todas las personas es de: {prom_edad:.2f}")
        print(f"El promedio de peso de todas las personas es de: {prom_peso:.2f}")
        print(f"El promedio de estatura de todas las personas es de: {prom_estatura:.2f}")
        print(f"Hay {x}, persona(s) con edad de entre [18-25] ")
        print(f"Hay {cal}, personas mayor(es) a 36 años")
        print(f"El promedio de peso entre las personas de 18 a 35 años es: {suma/len(contPos):.2f}")


#Ejercicio 8 - Parte 3
    def tablaDemultiplicar (self):

        self.tnumero = int(input("Ingresa el número del que desea saber el factorial: "))

        for i in range(0,11):
            resultado = i * self.tnumero
            print (self.tnumero,"x",i,"=",resultado)

#Ejercicio 9 - Parte 3
    def fichasdo (self):
        for i in range (0,7):
            for j in range (0, i+1):
                print("|"+str(i)+"|"+str(j))

#Ejercicio 10 - Parte 3
    def calpromedio (self):
        valor = int(input("Ingresar un número: "))

        conta = 0 
        sum = 0

        while valor > 1: 
            valor = int(input("Ingresar otro datos: "))
            sum = sum + valor
            conta = conta + 1
        if conta == 0:
            print ("No tiene ningún dígito")
        else:
            promedio = sum / conta
            print("El promedio de los {} ".format(conta), "número es igual a {} ".format(promedio) )  

        
#Ejercicio 1 - Parte 4
    def calcularMedia (self):

        lista = []
        t = True 
        while t: 
            self.edad = int(input("Digitar una edad mayor a 18 años y si desea finalizar, ingrese un 0: "))
            if self.edad > 18:
                lista.append(self.edad)
            else:
                t = False
        
        promedio = codigoEstr.promediarEdad(lista)
        if len(lista) > 0:
            print("El promedio de las edades: ", promedio)
        else: 
            print("No se puede calcular el promedio")

    def promediarEdad(lista):
        for edad in lista:
            if edad > 18:
                promedio = sum(lista)/len(lista)
                return promedio

#Ejercicio 2 - Parte 4
    def elevar (self):

        base = int(input("Ingresar un número (base): "))
        exponente = int(input("Ingresa otro número (exponente): "))

        elevado = codigoEstr.potenciacion(self, base, exponente)
        print("El resultado de esa operación es: {} ".format(elevado))

    def potenciacion(self, base, exponente):
        elevado = base**exponente
        return elevado

#Ejercicio 3 - Parte 4
    def pentagono (self):
        acum = 0
        for i in range(5):
            lado = int(input("Ingresar la medida de un lado: "))
            acum = codigoEstr.perimetro(acum,lado)
        print("El perímetro del pentágono es: {} ". format(acum))
        
    def perimetro(acum,lado):
        acum = acum + lado 
        return acum
        
#Ejercicio 4 - Parte 4 

    def salario (self):
        id = {}
        acp = codigoEstr()

        while len(id) <= 4:
            a= input("Ingresar su nombre: ")
            id[a] = int(input("Ingresar horas trabajadas {}:".format(a)))
        horas = int(input("Ingresar el monto por hora: "))

        ss = acp.CalcularSalar(id, horas)
        for i in ss: 
            print (i, "cobrará", ss[i][1])

    def CalcularSalar (self, a, ht):
        cacp = codigoEstr()
        for i in a:
            if a[i] <= 40:
                a[i] = [a[i], (a[i] * ht)]
            
            else:
                a[i] = [a[i], (40 * ht)]
                a[i][1] = cacp.aumentoTa(a[i],ht)
        print("*"*20)
        return a
    def aumentoTa (self, k, ht):
        ext = k[1] + ((k[0]- 40) * (ht+(ht*0.35)))
        return ext
#Ejercicio 5 - Parte 4
    def caldistancia (self):
        for i in range (4):
            ciudad_1 = input("Ingreso del nombre de ciudad partida: ")
            ciudad_2 = input("Ingreso del nombre de ciudad llegada: ")

            milla_a_km = codigoEstr.MillasAKilómetros(self)
            print("La distancia entre {} ".format(ciudad_1), "y {} ".format(ciudad_2),"es {} ".format(milla_a_km))
    def MillasAKilómetros (self):
        distancias_millas = float(input("Ingresar la distnacia en millas: "))
        millas_a_km = distancias_millas * 1.60935
        return millas_a_km

var = codigoEstr()
var.estacionamiento()
