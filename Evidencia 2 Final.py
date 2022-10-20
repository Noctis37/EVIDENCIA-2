"""1.- Definimos los import que utilizaremos para  saber que funciones se usaran en el programa que
hara cada menu

La funcion data time combinación de funciones de fecha y hora,
DATE devuelve el número de serie secuencial que representa una fecha determinada.

La funcion csv permite guardar los datos en un formato de tabla estructurada.

La funcion de openpyxl se encarga de guardar las reservaciones en formato excel

En si cada funcion es importante ya que  estos agrupan datos  para

realizar una tarea concreta y que se pueden reutilizar fácilmente.
.
"""
import datetime
import csv
import openpyxl
import time

"""2.- La parte de los print sirve principamente  de la linea nueve se encarga de darle un toque estetico al menu 
y asi definir el menu del programa.
    """

print("*" * 20)
print("BIENVENIDO A NUESTRO PROGRAMA")
print("*" * 20 )

"""3.- Los diccionarios sirven para que el usuario llene el menu y se queden guardados algunos ya estan predefinidos
    """

Eventos = {1:("XBOX","Gamescom 2022"),
           2:("XBOX","Nintendo Direct Mini"),
           3:("XBOX","Xbox game fest")}

reservas= {}
salas = {}
Usuarios= {}
Horarios={
    "M" : "Matutino",
    "V" : "Vespertino",
    "N" : "Nocturno",
    "m" : "Matutino",
    "v" : "Vespertino",
    "n" : "Nocturno"
}

"""4.- Este mudulo se utiliza como menu adema de dar la posibilidad de elegir las opciones y operaciones que queremos
hacer.

la opcion 1 se encarga de registrar las reservaciones.
la opcion 2 se encarga de modificar las reservaciones.
la opcion 3 se encarga de registrar cuales fechas estan disponibles.
la opcion 4 se encarga de checar las reservaciones en una sala .
la opcion 5 se encarga de registrar una sala.
la opcion 6 se encarga de registrar el cliente.
la opcion 7 se encarga de salir del problama.
la opcion 8 se encatga de exportar una reservacion a excel.
    """
while True:
    Mi_Menu=( "1. Registra la reservacion\n" +
    "2. Modificar las descripciones de la reservacion\n" +
    "3. Consulta la fecha disponible\n" +
    "4. Reporte de la reservaciones de una fecha\n" +
    "5. Registrar Sala\n" +
    "6. Registrar Cliente\n" +
    "7. Salir del programa\n" +
    "8. Exportar en excel\n")

    print(Mi_Menu)

    Opcion = int(input("Seleccione el numero de la accion que quiere realizar \n:"))

    if Opcion == 1:
        while True:
            Nombre=input( "Ingresa el nombre de la reservacion : ")
            if Nombre=="":
                break
            Horario=input( "Ingresa el turno de la reservacion [M, V, N] : ")
            Fecha_ingresada=input( "Ingresa la fecha de la reservacion  : ")
            Fecha = datetime.datetime.strptime(Fecha_ingresada,"%d/%m/%Y").date()
            fecha_actual = datetime.datetime.now()
            cant_dias = int(input("¿Cuantos dias faltan para tu evento?: "))
            if cant_dias <= 1:
                print("Tienes que hacer la reserva con 2 dias de anticipacion.")
            else:
                if Horario== "":
                    break
                else:
                    Nueva_llave=max(list(reservas.keys()),default=0) + 1
                    reservas[Nueva_llave] = (Nombre, Horarios[Horario], Fecha)
                    fecha_actual = datetime.datetime.today()
                    for clave,datos in list(reservas.items()):
                        print("Clave\t" + "Nombre\t"+ "Turno\t" + "Fecha\t")
                        print(f"{clave}\t{datos[0]}\t{datos[1]}\t{datos[2]}\t")
                break

    elif Opcion == 2:
        while True:
            Numero_Evento=int(input("Ingresa el folio de la sala (Solo se perimiten numeros): "))
            if Numero_Evento in Eventos.keys():
                nuevo=input("Ingresa el nombre nuevo (Si deseas regresar al menu escribe salir): ")
            if nuevo=="":
                break
        for Folio_Evento,[Nombre,XBOX] in Eventos.items():
                if Numero_Evento == Folio_Evento:
                    Eventos.update({Folio_Evento:[nuevo,XBOX]})
        for clave,evento in Eventos.items():
            print(f"La clave es {clave} y el evento modifcado es {evento[0]}")
            break


    elif Opcion==3:
        while True:
            salas_hechas = []
            salas_disponibles =[]
            Nueva_llave=max(list(reservas.keys()),default=0) + 1
            reservas[Nueva_llave] = (Horarios, fecha_actual, Sala)
            for clave, [llave, Sala, Horarios] in reservas.items():
                for llave, [sala, cupo] in salas.items:
                    salas_hechas.append((llave, Sala, Horarios))
            sets_salas_hechas = set(salas_hechas)
            for llave, [sala, cupo] in salas.items:
                salas_disponibles.append((llave, sala, Horarios))
                salas_disponibles.append((llave, sala, Horarios))
                salas_disponibles.append((llave, sala, Horarios))
            sets_salas_disponibles = set(salas_disponibles)
            salas_desocupadas = (sets_salas_disponibles - sets_salas_hechas)
            print("Llave, Sala, Horarios")
            for llave, sala, Horarios in salas_desocupadas:
                print(llave, sala, Horarios)
                break


    elif Opcion==4:
        while True:
            Fecha=input("Ingrese fecha del evento (%d/%m/%Y):")
            Fecha_remix=datetime.datetime.strptime(Fecha,"%d/%m/%Y").date()
            print("{:<7} {:<23} {}".format("Nombre","Horario","Fecha"))
            for clave,[Nombre,Horario,fecha_procesada] in reservas.items():
                if  Fecha_remix == fecha_procesada:
                    print("{:<7} {:<23} {}".format(Nombre,Horario,fecha_procesada))
                break


    elif Opcion==5:
        while True:
            Sala=input( "Ingresa la sala : ")
            Cupo=int(input("Ingresa el cupo: "))
            if Sala=="":
                break
            else:
                Nueva_llave=max(list(salas.keys()),default=0) + 1
                salas[Nueva_llave] = (Sala,Cupo)
                for clave,datos in list(salas.items()):
                    print("Clave\t" + "Sala\t")
                    print(f"{clave}\t{datos}\t")
                break


    elif Opcion==6:
        while True:
            Usuario=input( "Ingresa al Usuario : ")
            if Usuario=="":
                break
            else:
                Nueva_llave=max(list(Usuarios.keys()),default=0) + 1
                Usuarios[Nueva_llave] = (Usuario)
                for clave,datos in list(Usuarios.items()):
                    print("Clave\t" + "Usuario\t")
                    print(f"{clave}\t{datos}\t")
                break


    elif Opcion == 7:
        print("Hasta pronto tenga un agradable dia.")
        archivo = open("Usuarios.csv","w", newline="")
        grabador = csv.writer(archivo)
        grabador.writerow(("Clave", "Cliente"))
        grabador.writerows([(clave, datos) for clave, datos in Usuarios.items()])
        archivo.close()
        break

    elif Opcion == 8:
        while True:
            Clave= 1
            Usuarioo= "Alan Javier Gutierrez Garay"
            Nombre= 'Expo XV'
            Horario= 'Nocturno'
            libro = openpyxl.Workbook()
            libro.iso_dates= True
            hoja = libro["Sheet"]
            hoja.title = "Hoja"
            hoja["B1"].value="Reporte"

            hoja["A2"].value="Clave"
            hoja["B2"].value="Usuario"
            hoja["C2"].value="Nombre_evento"
            hoja["D2"].value="Horario"

            hoja["A3"].value=Clave
            hoja["B3"].value=Usuarioo
            hoja["C3"].value=Nombre
            hoja["D3"].value=Horario

            libro.save("Reserva.xlsx")
            break