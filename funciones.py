import random
import math
def asignar_sueldos(trabajadores):
            sueldos_trabajadores = {personas:random.randint(300000,2500000) for personas in trabajadores}
            sueldo_trabajadores =sueldos_trabajadores
            return sueldo_trabajadores
def clasificar_sueldos(sueldos):
        pers_8 =[]
        dinero_8 = []
        pers_2m = []
        dinero_2m= []
        pers_25m = []
        dinero_25m = []
        i=0
        j=0
        k=0
        for personas,dinero in sueldos.items():
                if dinero< 800000:
                    pers_8.append(personas)
                    dinero_8.append(dinero)
                    i+=1
                elif dinero>= 800000 and dinero<2000000:
                        pers_2m.append(personas)
                        dinero_2m.append(dinero)
                        j +=1
                else:
                        pers_25m.append(personas)
                        dinero_25m.append(dinero)   
                        k+=1                             
        print("Sueldos menores a 800.000\n","total:",i)
        print("Nombre empleado      Sueldo")
        while i > 0:
                print(pers_8[i-1],"      ",dinero_8[i-1])
                i-=1
        print("Sueldos mayores a 800.000 y menores a 2.000.000\n","total:",j)
        print("Nombre empleado      Sueldo")
        while j > 0:
                print(pers_2m[j-1],"      ",dinero_2m[j-1])
                j-=1
        print("Sueldos mayores a 2.500.000\n","total:",k)
        print("Nombre empleado      Sueldo")
        while k > 0:
                print(pers_25m[k-1],"      ",dinero_25m[k-1])
                k-=1 
def ver_estadistica(personas):
        sueldobajo = 10000000000
        sueldoalto = 0
        total = 0
        media = 1
        for persona,dinero in personas.items():
                if dinero < sueldobajo:
                        persona_menor = persona
                        sueldobajo = dinero
                elif dinero>sueldoalto:
                        persona_mayor = persona
                        sueldoalto = dinero
                total += dinero
                media *= dinero 
        media = media**0.1
        media =math.trunc(media)
        total = total/10
        total = math.trunc(total)
        print("Sueldo mas alto:",persona_mayor,"$",sueldoalto)
        print("sueldo mas bajo:",persona_menor,"$",sueldobajo)
        print("promedio de sueldos: $",total)
        print("Media geometrica de sueldos: $",media)
def reporte(personas):
        print("Nombre empleado     Sueldo base      Descuento salud      Descuento AFP     Sueldo liquido")
        for persona, dinero in personas.items():
                afp = dinero*0.12
                afp = math.trunc(afp)
                salud = dinero*0.07
                salud = math.trunc(salud)
                liquido = dinero-afp-salud
                print(persona,"     ",dinero,"      ",salud,"      ",afp,"     ",liquido)
                