from funciones import *
from colorama import Style, Back, Fore, init
init(autoreset=True)


#Programa principal:
seleccion = 0
while seleccion != 4:
    print()
    limpiar_pantalla()
    print(Back.BLUE + Fore.WHITE + "Bienvenidos al ", end="")
    print(Style.BRIGHT + Back.BLUE + Fore.WHITE + "Banco Francés")
    print()
    print (Fore.BLUE + "1 - Crear usuario") #C: Create
    print (Fore.BLUE + "2 - Ingresar al sistema")
    print (Fore.BLUE + "3 - ¿Olvidó su clave?") #Usuario>Valida existencia>Envía mail p/reestablecer datos).
    print (Fore.BLUE + "4 - Salir del programa")
    print()
    print("Ingrese el número de su elección: ",end="")
    seleccion = validar_entero_positivo_dos()
    if seleccion == 1:
        cliente_nuevo()
    elif seleccion == 2:
        usu_cla = buscar_nom_usu_cla()
        usu_log = ingreso_usuario(usu_cla)
        cuenta_regresiva(2)
        menu2(usu_log)
    elif seleccion == 3:
        print()
        print("",end="")
        usu=str(validacion_dni())
        usu_cla = buscar_nom_usu_cla()
        i = 0
        while i < len(usu_cla):
            if usu_cla[i] == usu:
                print()
                print(f'Estimado cliente {usu_cla[i-2]}, le hemos enviado un mail a {usu_cla[i-1]}, recordando su Usuario {usu_cla[i]} y Clave {usu_cla[i+1]}')
            i += 1
        print()
        cuenta_regresiva(10)
    elif seleccion == 4:
        print("Adios!")
        seleccion = 4
    else:
        print('La opción elegida no está entre las opciones. Vuelva a iniciar.')
        cuenta_regresiva(3)
        