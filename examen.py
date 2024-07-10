
trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
import funciones
import csv
sueldos_trabajadores = {}
while True:
        print("Bienvenido a reportes.py\n--------Menu--------\n1)Asignar sueldos aleatorios\n2)Clasificar sueldos\n3)Ver estadisticas\n4)Reporte de sueldos\n5)Salir del programa")
        menu = input("")
        if menu == "1":
            sueldos_trabajadores = funciones.asignar_sueldos(trabajadores)
        elif menu == "2":
               funciones.clasificar_sueldos(sueldos_trabajadores)
        elif menu =="3":
               funciones.ver_estadistica(sueldos_trabajadores)
        elif menu == "4":
               funciones.reporte(sueldos_trabajadores)
        elif menu == "5":
                print("Finalizando programa......\nDesarrollado por Steven Larraguibel\nRUT 20.688.896-2")
                break
        else:
                print("Por favor ingrese uno de los numeros indicados en el menu")

           