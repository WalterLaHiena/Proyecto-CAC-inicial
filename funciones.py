import json
import time
from colorama import Style, Back, Fore, init
init(autoreset=True)
###FUNCION PARA ELIMINAR LAS CLAVES DEL DICCIONARIO DE CADA CLIENTE
def eliminar_clave(datos, nombre, usu_log):  # Función para eliminar una clave
    limpiar_pantalla()
    mostrar_diccionario(datos, usu_log)
    for nombre in datos:
        if nombre["Usuario"] == usu_log and usu_log == "8888":
            while True:
                print("Ingrese qué quiere borrar: ", end="")
                clave = validar_texto()
                clave = clave.title()
                if clave not in ["Nombre", "Dni", "Correo", "Usuario", "Clave", "Saldo"]:
                    if clave in nombre:
                        print(f"{clave}: {nombre[clave]}")
                        del nombre[clave]
                        guardar_json('cliente.json', datos)
                        break
                    else:
                        print("Clave no encontrada. Intente nuevamente.")
                else:
                    print("Este dato no se puede borrar.")
        elif nombre["Usuario"] == usu_log:
            while True:
                print("Ingrese qué quiere borrar: ", end="")
                clave = validar_texto()
                clave = clave.title()
                if clave not in ["Nombre", "Dni", "Correo", "Usuario", "Clave", "Saldo"]:
                    if clave in nombre:
                        print(f"{clave}: {nombre[clave]}")
                        del nombre[clave]
                        guardar_json('cliente.json', datos)
                        break
                    else:
                        print("Clave no encontrada. Intente nuevamente.")
                else:
                    print("Este dato no se puede borrar.")
    return
###FUNCION DE CUENTA REGRESIVA PARA MANTENER LOS DATOS EN PANTALLA POR t SEGUNDOS
def cuenta_regresiva(t):
    for i in range(t,-1,-1):
        time.sleep(1)
        print(f'\rSe borra en: {i}',end=" ")
###FUNCION PARA LIMPIAR LA PANTALLA (según Sistema Operativo)
def limpiar_pantalla(): 
    import os #Importa funciones de OS
    #Con el IF comprueba qué tipo de sistema operativo tiene la máquina en dónde se está ejecutando
    if os.name =="posix": 
        os.system("clear")
    elif os.name=="ce" or os.name=="nt" or os.name=="dos":
        os.system("cls")
    return 
###FUNCION PARA CARGAR BASE DE DATOS (.JSON)
def cargar_json(nombre_archivo): 
    archivo = open(nombre_archivo, 'r')
    datos = json.load(archivo)
    archivo.close()
    return datos
###FUNCION PARA AGREGAR UN DICCIONARIO NUEVO A LA LISTA DE DICCIONARIOS (.JSON)
def agregar_diccionario(datos, nuevo_cliente): 
    datos.append(nuevo_cliente)
###FUNCION DE NUEVO CLIENTE (DATOS)
def cliente_nuevo():
    limpiar_pantalla()
    print()
    print(f'A continuación se le pedirán una serie de datos, los cuales serán utilizados para ingresarlo como cliente del Banco.')
    print() #Se piden todos los datos del nuevo cliente
    print("Ingrese su/s nombre/s: ", end='')
    nombre = validar_texto()
    print("Ingrese su/s apellido/s: ", end='')
    apellido=validar_texto()
    print("",end="")
    dni=validacion_dni()
    print("Ingrese su correo electrónico: ",end="")
    correo=validar_vacio()
    print("Ingrese su dirección: ",end="")
    direccion=validar_vacio()
    print("Ingrese su teléfono, sin guiones ni puntos (xxxxxxxxxx): ",end="")
    telefono=validar_entero_positivo_dos()
    usuarioVal= str(dni)
    print("Ingrese una clave numérica con la que desea iniciar sesión: ", end="")
    contraseniaVal = str(validacion_clave())
    print()
    limpiar_pantalla()
    print()
    print("SUS DATOS SON LOS SIGUIENTES".center(80)) #Muestras los datos ingresados
    print()
    print(f'NOMBRE: {Fore.RED}{nombre.title():<30}{Fore.RESET} APELLIDO: {Fore.RED}{apellido.title():<25}{Fore.RESET} DNI: {Fore.RED}{dni:<15}{Fore.RESET}')
    print(f'CORREO: {Fore.RED}{correo:<30}{Fore.RESET} DIRECCIÓN: {Fore.RED}{direccion.title():<24}{Fore.RESET} TELÉFONO: {Fore.RED}{telefono:<15}{Fore.RESET}')
    print(f'USUARIO: {Fore.RED}{usuarioVal:<29}{Fore.RESET} CLAVE: {Fore.RED}{contraseniaVal:<24}{Fore.RESET}')
    print()
    print("Chequee si los datos están bien; de estar mal, debe volver a ejecutar el menú. \nGuardar los nuevos datos?(SI/NO): ",end="")
    pregunta=validar_texto()
    pregunta = pregunta.upper()
    if pregunta == "NO":
        print("Vuelve al menú")
        return
    elif pregunta == "SI":
        print ()
        print("¡Felicidades! Por haber elegido nuestro banco te bonificamos $50.000. ¡Que los disfrutes! :)") 
        print() #Se crea un Diccionario para almacenar los datos nuevos
        nuevo_cliente = {
            "Nombre": nombre, 
            "Apellido": apellido,
            "Dni": dni,
            "Correo": correo,
            "Direccion": direccion,
            "Telefono": telefono,
            "Usuario": usuarioVal,
            "Clave": contraseniaVal,
            "Saldo": 50000 #EL SALDO SE OTORGA AUTOMÁTICAMENTE POR UNA PROMOIÓN BANCARIA.
        }
        datos = cargar_json('cliente.json')
        agregar_diccionario(datos, nuevo_cliente) # Agregar un nuevo diccionario a la lista
        guardar_json('cliente.json', datos)
        cuenta_regresiva(10)
    else:
        print("La opción ingresada no es válida")
    return nuevo_cliente
###FUNCION PARA BUSCAR NOMBRE, MAIL, USUARIO, CLAVE
def buscar_nom_usu_cla():
    datos=cargar_json('cliente.json')
    usu_cla = []
    i = 0
    while i < len(datos):
        nombre = datos[i]['Nombre']
        mail = datos[i]['Correo']
        usuario = datos[i]['Usuario']
        clave = datos[i]['Clave']
        usu_cla.append(nombre)
        usu_cla.append(mail)
        usu_cla.append(usuario)
        usu_cla.append(clave)
        i += 1
    return usu_cla
###FUNCION DE INGRESO DE USUARIO
def ingreso_usuario(datos):
    for intento in range(3, 0, -1): #Comienza en 3, termina en 1, decreciendo en 1
        usuario = str(validacion_dni())
        print("Ingrese su clave numérica: ", end="")
        contrasenia = str(validacion_clave())
        for indice in range (len(datos)):
            if usuario == datos[indice] and contrasenia == datos[indice + 1]:
                print("Inicio de sesión exitoso.")
                usu_log = usuario
                return usu_log
        else:
            print("Usuario o contraseña incorrectos.")
            print(f"Intentos restantes: {intento - 1}")
        if intento == 1:
            print("Se han agotado los intentos. Cierre del programa.")
    return usu_log
###FUNCION PARA MOSTRAR LOS DATOS (DICCIONARIO) CARGADO EN JSON
def mostrar_diccionario(datos, usu_log):
    cargar_json('cliente.json')
    for nombre in datos:
        if nombre["Usuario"] == usu_log and usu_log == "8888":
            for nombre in datos:
                for clave, valor in nombre.items():
                    print(f'{clave}: {valor}')
                print("----------------------")
        elif nombre["Usuario"] == usu_log:
            limpiar_pantalla()
            for clave, valor in nombre.items():
                print(f'{clave}: {valor}')
    return nombre
###FUNCION PARA GUARDAR LOS DATOS MODIFICADOS
def guardar_json(nombre_archivo, datos): 
    archivo = open(nombre_archivo, 'w')
    json.dump(datos, archivo)
    archivo.close()
###FUNCION PARA REALIZAR TRANFERENCIAS
def tranferencia(usu_log):
    datos = cargar_json('cliente.json')
    for nombre in datos:
        if nombre["Usuario"] == usu_log:
            for clave in nombre.items():
                print(f"Su saldo es $ {nombre["Saldo"]}")
                saldo = nombre["Saldo"]
                print("Ingrese el monto a tranferir: ",end="")
                monto_transferir = float(validar_decimal_positivo_dos())
                print("Ingrese el CBU de destino: ",end="")
                cbu = validar_entero_positivo_dos()
                if saldo > 0:
                    if saldo >= monto_transferir:
                        saldo_final = saldo - monto_transferir
                        print(f'Su saldo actual es: {saldo_final}. Transferiste: {monto_transferir} a la cuenta {cbu}')
                        saldo = saldo_final
                        nombre["Saldo"] = saldo_final
                        guardar_json('cliente.json', datos)
                    elif saldo < monto_transferir:
                        print("Su saldo no es suficiente para realizar esta transferencia.")
                else: 
                    print("No dispone de saldo sufiente para realizar esta operación.")
                return
###FUNCION PARA CONSULTAR SALDO
def consultar_saldo(usu_log):
    datos = cargar_json('cliente.json')
    for nombre in datos:
        if nombre["Usuario"] == usu_log:
            print(f"Su saldo es $ {nombre['Saldo']}")
    return
###FUNCION DE MENU TERCIARIO
def menu3(datos, usu_log):
    selec = 0
    while selec != 7:
        print("1 - Cambiar NOMBRE")
        print("2 - Cambiar APELLIDO")
        print("3 - Cambiar CORREO")
        print("4 - Cambiar DIRECCIÓN")
        print("5 - Cambiar TELÉFONO")
        print("6 - Cambiar CLAVE")
        print("7 - Volver al menú anterior")
        print("Ingrese el número de su selección: ",end="")
        selec = validar_entero_positivo_dos()
        match selec:
            case 1:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'NOMBRE: {nombre["Nombre"]}')
                        print("Ingrese el nuevo nombre/s: ",end="")
                        new_name = validar_texto()                        
                        nombre["Nombre"] = new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
            case 2:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'APELLIDO: {nombre["Apellido"]}')
                        print("Ingrese el nuevo apellido/s: ",end="")
                        new_name = validar_texto()
                        nombre["Apellido"] = new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
                        
            case 3:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'CORREO: {nombre["Correo"]}')
                        print("Ingrese el nuevo correo: ",end="")
                        new_name = validar_vacio()
                        nombre["Correo"] = new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
            case 4:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'DIRECCIÓN: {nombre["Direccion"]}')
                        print("Ingrese la nueva dirección: ",end="")
                        new_name = validar_vacio()
                        nombre["Direccion"] = new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
            case 5:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'TELÉFONO: {nombre["Telefono"]}')
                        print("Ingrese el nuevo teléfono sin guiones: ",end="")
                        new_name = validar_entero_positivo_dos()
                        nombre["Telefono"] = new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
            case 6:
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print(f'CLAVE: {nombre["Clave"]}')
                        print("Ingrese la nueva clave: ",end="")
                        new_name = validar_entero_positivo_dos()
                        nombre["Clave"] == new_name
                        guardar_json('cliente.json', datos)
                        mostrar_diccionario(datos, usu_log)
            case 7:
                return
###FUNCION DE MENU SECUNDARIO
def menu2(usu_log):
    seleccion = 0
    while seleccion != 8:
        print()
        limpiar_pantalla()
        print(Fore.RED + "1 - Consultar saldo")
        print(Fore.RED + "2 - Transferencias")
        print(Fore.RED + "3 - Consultar datos")
        print(Fore.RED + "4 - Modificar datos (Actualizar los datos ya almacenados)")
        print(Fore.RED + "5 - Borrar datos (Borrar datos ya almacenados)")
        print(Fore.RED + "6 - Agregar información adicional (Opcionales: Religión, Fecha de nacimiento, etc.)")
        print(Fore.RED + "7 - Volver al menú principal")
        print()
        print("Ingrese el número de su selección: ",end="")
        seleccion = validar_entero_positivo_dos()
        match seleccion:
            case 1:
                consultar_saldo(usu_log)
                cuenta_regresiva(2)
            case 2:
                tranferencia(usu_log)
                cuenta_regresiva(2)
            case 3:
                datos = cargar_json('cliente.json')
                print("Datos cargados:")
                mostrar_diccionario(datos, usu_log)
                print("Presione enter para regresar: ",end="")
                teclas = input()
                while teclas == True:
                    teclas=False
                    return
            case 4:
                print("Modificar datos existentes")
                datos = cargar_json('cliente.json')
                mostrar_diccionario(datos, usu_log)
                menu3(datos, usu_log)
            case 5:
                print("Seleccione qué datos desea eliminar")
                datos = cargar_json('cliente.json')
                mostrar_diccionario(datos, usu_log)
                eliminar_clave(datos, usu_log, usu_log)
                cuenta_regresiva(3)
            case 6:
                print("Agregue informacion adicional a los datos")
                limpiar_pantalla()
                datos = cargar_json('cliente.json')
                mostrar_diccionario(datos, usu_log)
                for nombre in datos:
                    if nombre["Usuario"] == usu_log:
                        print()
                        print("Ingrese el/los campo/s que desea agregar: (ej: Fecha de Nacimiento, Religion, etc)")
                        clave = 1
                        valor = 1
                        while clave != "0" or valor != "0":
                            clave = input("Campo nuevo (0 para salir): ")
                            valor = input("Ingrese el valor del campo nuevo (0 para salir): ")
                            clave = clave.title()
                            valor = valor.title()
                            nombre[clave] = valor
                        nombre.pop("0")
                        guardar_json('cliente.json', datos)
                cuenta_regresiva(3)
            case 7:
                return
###FUNCIONES PARA REALIZAR VALIDACIONES
def validar_texto(): # Valida ingreso de texto
    while True:
        ingreso = input()
        # Verificar si el ingreso está vacío o contiene caracteres que no sean letras
        if len(ingreso) == 0:
            print("El dato no puede estar vacío. Reintente: ", end="")
        elif not ingreso.isalpha():
            print("El dato solo puede contener letras. Reintente: ", end="")
        else:
            return ingreso
def validar_vacio():
    ingreso = input()
    while len(ingreso) == 0:
        ingreso = input("El dato no puede estar vacío. Reintente: ")
    return ingreso
def validar_entero_positivo_dos():
    while True:
        try:
            ingreso = input()
            if len(ingreso) == 0:
                print("El dato no puede estar vacío. Reintente: ", end='')
                continue
            if not ingreso.isdigit():
                print("El dato debe ser un número entero. Reintente: ", end='')
                continue
            ingreso_num = int(ingreso)
            if ingreso_num < 0:
                print("El número debe ser positivo. Reintente: ", end='')
                continue
            return ingreso_num
        except ValueError:
            print("Hubo un error inesperado. Reintente:")
def validar_decimal_positivo_dos():
    while True:
        try:
            ingreso = input()
            if len(ingreso) == 0:
                print("El dato no puede estar vacío. Reintente: ", end='')
                continue
            if not ingreso.replace('.', '', 1).isdigit() or ingreso.count('.') > 1:
                print("El dato debe ser un número decimal positivo. Reintente: ", end='')
                continue
            ingreso_num = float(ingreso)
            if ingreso_num < 0:
                print("El número debe ser positivo. Reintente: ", end='')
                continue
            return ingreso_num
        except ValueError:
            print("Hubo un error inesperado. Reintente: ", end='')
def validacion_dni():
    print("Ingrese su DNI (sin puntos): ", end='')
    while True:
        try:
            ingreso = input()
            if len(ingreso) == 0:
                print("El dato no puede estar vacío. Reintente: ", end='')
                continue
            if not ingreso.isdigit():
                print("El dato debe ser un número entero. Reintente: ", end='')
                continue
            ingreso_num = int(ingreso)
            if ingreso_num < 0:
                print("El número debe ser positivo. Reintente: ", end='')
                continue
            return ingreso_num
        except ValueError:
            print("Hubo un error inesperado. Reintente: ", end='')
def validacion_clave():
    while True:
        #print("Ingrese su clave numérica: ", end='')
        try:
            ingreso = input()
            if len(ingreso) == 0:
                print("El dato no puede estar vacío. Reintente: ", end='')
                continue
            if not ingreso.isdigit():
                print("El dato debe ser un número entero. Reintente: ", end='')
                continue
            ingreso_num = int(ingreso)
            if ingreso_num < 0:
                print("El número debe ser positivo. Reintente: ", end='')
                continue
            return ingreso_num
        except ValueError:
            print("Hubo un error inesperado. Reintente: ", end='')
def validacion_avanzada():
    print("Ingrese un número entero positivo: ", end='')
    while True:
        try:
            ingreso = input()
            if len(ingreso) == 0:
                print("El dato no puede estar vacío. Reintente: ", end='')
                continue
            if not ingreso.isdigit():
                print("El dato debe ser un número entero. Reintente: ", end='')
                continue
            ingreso_num = int(ingreso)
            if ingreso_num < 0:
                print("El número debe ser positivo. Reintente: ", end='')
                continue
            return ingreso_num
        except ValueError:
            print("Hubo un error inesperado. Reintente: ", end='')#Programa principal:



