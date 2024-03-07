import time
import os
from administrador import Administrador

# Arreglo de computadoras disponibles con precios
computadoras = [
    {"modelo": "Ryzen 5", "ram": "8GB", "almacenamiento": "120TB", "precio": 800},
    {
        "modelo": "Intel i7",
        "ram": "16GB",
        "almacenamiento": "256GB SSD",
        "precio": 1200,
    },
    {"modelo": "AMD Athlon", "ram": "4GB", "almacenamiento": "1TB HDD", "precio": 500},
    {
        "modelo": "Intel Core m3",
        "ram": "8GB",
        "almacenamiento": "512GB SSD",
        "precio": 1000,
    },
    {
        "modelo": "Ryzen 9",
        "ram": "32GB",
        "almacenamiento": "1TB NVMe SSD",
        "precio": 1500,
    },
    {"modelo": "Intel i5", "ram": "12GB", "almacenamiento": "2TB HDD", "precio": 1100},
    {
        "modelo": "AMD Ryzen 7",
        "ram": "16GB",
        "almacenamiento": "512GB SSD",
        "precio": 1300,
    },
    {
        "modelo": "Intel Celeron",
        "ram": "4GB",
        "almacenamiento": "128GB eMMC",
        "precio": 400,
    },
    {"modelo": "Ryzen 3", "ram": "6GB", "almacenamiento": "500GB HDD", "precio": 600},
    {
        "modelo": "Intel Core i9",
        "ram": "64GB",
        "almacenamiento": "4TB NVMe SSD",
        "precio": 2000,
    },
]

# Arreglo de bicicletas disponibles con precios
bicicletas = [
    {"tipo": "Bicicleta de Montaña", "precio": 200},
    {"tipo": "Bicicleta de Ciudad", "precio": 150},
    {"tipo": "Bicicleta Eléctrica", "precio": 100},
]

# Arreglo de comidas con precios
comidas = [
    {"nombre": "Hamburguesa", "precio": 50},
    {"nombre": "Pizza", "precio": 50},
    {"nombre": "Ensalada", "precio": 50},
]

# Arreglo de materiales de papeleria con precios
materiales_papeleria = [
    {"nombre": "Cuaderno", "precio": 50},
    {"nombre": "Lápices (paquete)", "precio": 20},
    {"nombre": "Bolígrafos (paquete)", "precio": 30},
]

# Contadores globales
computadoras_alquiladas = 0
bicicletas_alquiladas = 0
comidas_compradas = 0
materiales_papeleria_comprados = 0


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def animar_texto(texto):
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(0.003)
    print()


def animar_tabla_inicio_sesion():
    limpiar_pantalla()
    animar_texto("+-------------------------------------------+")
    animar_texto("|        Inicio de Sesión - PUSP            |")
    animar_texto("+-------------------------------------------+")
    time.sleep(0.5)  # Breve pausa antes de mostrar el formulario de inicio de sesión


def mostrar_tabla_ascii(datos):
    # Encabezado de la tabla
    animar_texto("+-------------------------------------------+")
    animar_texto("|               Menú Principal              |")
    animar_texto("+-------------------------------------------+")

    # Contenido de la tabla
    for opcion in datos:
        print(f"| {opcion:<41} |")

    # Pie de la tabla
    animar_texto("+-------------------------------------------+")


def iniciar_sesion():
    animar_tabla_inicio_sesion()
    animar_texto(
        "¡Bienvenido a la PUSP - Plataforma Universitaria de Servicios y Préstamos!"
    )

    # Simulación de inicio de sesión
    animar_texto("PARA ESTUDIANTE: USUARIO=estudiante CONTRASEÑA=contraseña_estudiante")
    animar_texto("PARA ADMINISTRADOR: USUARIO=administrador CONTRASEÑA=contraseña_admin")
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    # Verificación de credenciales (esto es solo un ejemplo, deberías mejorar la seguridad)
    if usuario == "estudiante" and contrasena == "contraseña_estudiante":
        return "estudiante"
    elif usuario == "administrador" and contrasena == "contraseña_admin":
        return "administrador"
    else:
        return None


def mostrar_computadores(datos):
    # Encabezado de la tabla
    animar_texto(
        "+--------+------------------------+------+----------------+---------+"
    )
    animar_texto(
        "| Número |        Modelo          | RAM  | Almacenamiento | Precio  |"
    )
    animar_texto(
        "+--------+------------------------+------+----------------+---------+"
    )

    # Contenido de la tabla
    for i, computadora in enumerate(datos, 1):
        modelo = computadora["modelo"]
        ram = computadora["ram"]
        almacenamiento = computadora["almacenamiento"]
        precio = f"${computadora['precio']}"
        animar_texto(
            f"| {i:<6} | {modelo:<23} | {ram:<4} | {almacenamiento:<13} | {precio:<7} |"
        )

    # Pie de la tabla
    animar_texto(
        "+--------+------------------------+------+----------------+---------+"
    )


def mostrar_bicicletas(bicicletas):
    # Encabezado de la tabla
    animar_texto("+--------+------------------------+--------+")
    animar_texto("| Número |         Tipo           | Precio |")
    animar_texto("+--------+------------------------+--------+")

    # Contenido de la tabla
    for i, bicicleta in enumerate(bicicletas, 1):
        tipo = bicicleta["tipo"]
        precio = f"${bicicleta['precio']}"
        animar_texto(f"| {i:<6} | {tipo:<23} | {precio:<7} |")

    # Pie de la tabla
    animar_texto("+--------+------------------------+--------+")


def mostrar_comidas(comidas):
    # Encabezado de la tabla
    animar_texto("+--------+------------------------+--------+")
    animar_texto("| Número |         Comida         | Precio |")
    animar_texto("+--------+------------------------+--------+")

    # Contenido de la tabla
    for i, comida in enumerate(comidas, 1):
        nombre = comida["nombre"]
        precio = f"${comida['precio']}"
        animar_texto(f"| {i:<6} | {nombre:<23} | {precio:<7} |")

    # Pie de la tabla
    animar_texto("+--------+------------------------+--------+")


def mostrar_materiales_papeleria(materiales_papeleria):
    # Encabezado de la tabla
    animar_texto("+--------+------------------------+--------+")
    animar_texto("| Número |  Material de Papelería | Precio |")
    animar_texto("+--------+------------------------+--------+")

    # Contenido de la tabla
    for i, material in enumerate(materiales_papeleria, 1):
        nombre = material["nombre"]
        precio = f"${material['precio']}"
        animar_texto(f"| {i:<6} | {nombre:<23} | {precio:<7} |")

    # Pie de la tabla
    animar_texto("+--------+------------------------+--------+")


def menu_estudiante():
    global computadoras_alquiladas, bicicletas_alquiladas, comidas_compradas, materiales_papeleria_comprados
    opciones_menu_estudiante = [
        "1. Alquilar y devolver computadoras",
        "2. Reservar bicicletas",
        "3. Comprar Comida",
        "4. Comprar materiales de papeleria",
        "5. Salir",
    ]

    # Saldo inicial del estudiante
    saldo_inicial = 2000
    saldo_actual = saldo_inicial

    computadora_alquilada = None
    bicicleta_alquilada = None
    total_alquiler = 0
    total_gastos_comida = 0
    total_gastos_papeleria = 0

    while True:
        limpiar_pantalla()
        animar_texto("Tu saldo actual es: ")
        print(saldo_actual)
        time.sleep(1)
        limpiar_pantalla()
        animar_texto("Menú Estudiante:")
        mostrar_tabla_ascii(opciones_menu_estudiante)

        eleccion = input("Seleccione una opción (1-5): ")

        if eleccion == "1":
            limpiar_pantalla()
            animar_texto("Opción 1: Alquilar y Devolver Computadoras\n")

            if computadora_alquilada is None:
                # Mostrar las computadoras disponibles
                animar_texto("Computadoras disponibles para alquilar:")
                mostrar_computadores(computadoras)

                # Solicitar al usuario que elija una computadora
                seleccion = input(
                    "Seleccione el número de la computadora que desea alquilar (1-10): "
                )

                try:
                    seleccion = int(seleccion)
                    if 1 <= seleccion <= len(computadoras):
                        comp_seleccionada = computadoras.pop(seleccion - 1)
                        if saldo_actual >= comp_seleccionada["precio"]:
                            total_alquiler += comp_seleccionada["precio"]
                            computadora_alquilada = comp_seleccionada
                            saldo_actual -= comp_seleccionada["precio"]
                            computadoras_alquiladas += 1
                            limpiar_pantalla()
                            animar_texto(
                                f"¡Has alquilado la siguiente computadora:\n{comp_seleccionada['modelo']} - {comp_seleccionada['ram']} - {comp_seleccionada['almacenamiento']}\nCosto Total del Alquiler: ${total_alquiler}"
                            )
                        else:
                            animar_texto(
                                "Saldo insuficiente. Elige una computadora más económica."
                            )
                    else:
                        animar_texto(
                            "Selección no válida. Por favor, elija un número válido."
                        )
                except ValueError:
                    animar_texto("Error: Por favor, ingrese un número válido.")
            else:
                # El usuario ya tiene una computadora alquilada, ofrecer opción para devolverla
                animar_texto("Ya tienes una computadora alquilada.")
                devolver = input("¿Deseas devolverla? (S/N): ")
                if devolver.lower() == "s":
                    # Devolver la computadora y reiniciar el estado
                    total_alquiler -= computadora_alquilada["precio"]
                    computadoras.append(computadora_alquilada)
                    limpiar_pantalla()
                    animar_texto(
                        f"¡Has devuelto la siguiente computadora:\n{computadora_alquilada['modelo']} - {comp_seleccionada['ram']} - {comp_seleccionada['almacenamiento']}\nCosto Total del Alquiler: ${total_alquiler}"
                    )
                    computadora_alquilada = None
                elif devolver.lower() != "n":
                    animar_texto(
                        "Opción no válida. Por favor, elija 'S' para devolverla o 'N' para continuar."
                    )

        elif eleccion == "2":
            limpiar_pantalla()
            animar_texto("Opción 2: Alquilar y Devolver Bicicletas\n")

            if bicicleta_alquilada is None:
                # Mostrar las bicicletas disponibles
                animar_texto("Bicicletas disponibles para alquilar:")
                mostrar_bicicletas(bicicletas)

                # Solicitar al usuario que elija una bicicleta
                seleccion = input(
                    "Seleccione el número de la bicicleta que desea alquilar (1-3): "
                )

                try:
                    seleccion = int(seleccion)
                    if 1 <= seleccion <= len(bicicletas):
                        bicicleta_seleccionada = bicicletas.pop(seleccion - 1)
                        if saldo_actual >= bicicleta_seleccionada["precio"]:
                            total_alquiler += bicicleta_seleccionada["precio"]
                            bicicleta_alquilada = bicicleta_seleccionada
                            saldo_actual -= bicicleta_seleccionada["precio"]
                            bicicletas_alquiladas += 1
                            limpiar_pantalla()
                            animar_texto(
                                f"¡Has alquilado la siguiente bicicleta:\n{bicicleta_seleccionada['tipo']}\nCosto Total del Alquiler: ${total_alquiler}"
                            )
                        else:
                            animar_texto(
                                "Saldo insuficiente. Elige una bicicleta más económica."
                            )
                    else:
                        animar_texto(
                            "Selección no válida. Por favor, elija un número válido."
                        )
                except ValueError:
                    animar_texto("Error: Por favor, ingrese un número válido.")
            else:
                # El usuario ya tiene una bicicleta alquilada, ofrecer opción para devolverla
                animar_texto("Ya tienes una bicicleta alquilada.")
                devolver = input("¿Deseas devolverla? (S/N): ")
                if devolver.lower() == "s":
                    # Devolver la bicicleta y reiniciar el estado
                    total_alquiler -= bicicleta_alquilada["precio"]
                    bicicletas.append(bicicleta_alquilada)
                    limpiar_pantalla()
                    animar_texto(
                        f"¡Has devuelto la siguiente bicicleta:\n{bicicleta_alquilada['tipo']}\nCosto Total del Alquiler: ${total_alquiler}"
                    )
                    bicicleta_alquilada = None
                elif devolver.lower() != "n":
                    animar_texto(
                        "Opción no válida. Por favor, elija 'S' para devolverla o 'N' para continuar."
                    )

        elif eleccion == "3":
            limpiar_pantalla()
            animar_texto("Opción 3: Comprar Comida\n")

            # Mostrar las comidas disponibles
            animar_texto("Comidas disponibles para comprar:")
            mostrar_comidas(comidas)

            # Solicitar al usuario que elija una comida
            seleccion_comida = input(
                "Seleccione el número de la comida que desea comprar (1-3): "
            )

            try:
                seleccion_comida = int(seleccion_comida)
                if 1 <= seleccion_comida <= len(comidas):
                    comida_seleccionada = comidas.pop(seleccion_comida - 1)
                    if saldo_actual >= comida_seleccionada["precio"]:
                        total_gastos_comida += comida_seleccionada["precio"]
                        saldo_actual -= comida_seleccionada["precio"]
                        comidas_compradas += 1
                        limpiar_pantalla()
                        animar_texto(
                            f"¡Has comprado la siguiente comida:\n{comida_seleccionada['nombre']}\nGastos Totales en Comida: ${total_gastos_comida}"
                        )
                    else:
                        animar_texto(
                            "Saldo insuficiente. Elige una comida más económica."
                        )
                else:
                    animar_texto(
                        "Selección no válida. Por favor, elija un número válido."
                    )
            except ValueError:
                animar_texto("Error: Por favor, ingrese un número válido.")

        elif eleccion == "4":
            limpiar_pantalla()
            animar_texto("Opción 4: Comprar Materiales de Papelería\n")

            # Mostrar los materiales de papelería disponibles
            animar_texto("Materiales de papelería disponibles para comprar:")
            mostrar_materiales_papeleria(materiales_papeleria)

            # Solicitar al usuario que elija un material de papelería
            seleccion_papeleria = input(
                "Seleccione el número del material de papelería que desea comprar (1-3): "
            )

            try:
                seleccion_papeleria = int(seleccion_papeleria)
                if 1 <= seleccion_papeleria <= len(materiales_papeleria):
                    material_papeleria_seleccionado = materiales_papeleria.pop(
                        seleccion_papeleria - 1
                    )
                    if saldo_actual >= material_papeleria_seleccionado["precio"]:
                        total_gastos_papeleria += material_papeleria_seleccionado[
                            "precio"
                        ]
                        saldo_actual -= material_papeleria_seleccionado["precio"]
                        materiales_papeleria_comprados += 1
                        limpiar_pantalla()
                        animar_texto(
                            f"¡Has comprado el siguiente material de papelería:\n{material_papeleria_seleccionado['nombre']}\nGastos Totales en Papelería: ${total_gastos_papeleria}"
                        )
                    else:
                        animar_texto(
                            "Saldo insuficiente. Elige un material de papelería más económico."
                        )
                else:
                    animar_texto(
                        "Selección no válida. Por favor, elija un número válido."
                    )
            except ValueError:
                animar_texto("Error: Por favor, ingrese un número válido.")

        elif eleccion == "5":
            limpiar_pantalla()
            animar_texto("Cerrando sesion...")
            time.sleep(1)
            break

        else:
            limpiar_pantalla()
            animar_texto("Opción no válida. Por favor, elija una opción válida.")

        input("Presiona Enter para continuar...")


def menu_administrador(administrador):
    administrador.mostrar_menu_administrador()


def main():

    while True:
        tipo_usuario = iniciar_sesion()

        if tipo_usuario == "estudiante":
            menu_estudiante()
        elif tipo_usuario == "administrador":
            administrador = Administrador(
                computadoras_alquiladas,
                bicicletas_alquiladas,
                comidas_compradas,
                materiales_papeleria_comprados,
                computadoras,
                bicicletas,
                comidas,
                materiales_papeleria,
            )
            menu_administrador(administrador)
        else:
            limpiar_pantalla()
            print("Credenciales incorrectas. ¡Hasta luego!")


if __name__ == "__main__":
    main()
