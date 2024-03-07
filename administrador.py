import time
import os


class Administrador(object):
    def __init__(
        self,
        contador_computadoras,
        contador_bicicletas,
        contador_comidas,
        contador_materiales,
        computadores,
        bicicletas,
        comidas,
        materiales_papeleria,
    ):
        self.contador_computadoras = contador_computadoras
        self.contador_bicicletas = contador_bicicletas
        self.contador_comidas = contador_comidas
        self.contador_materiales = contador_materiales
        self.computadores = computadores
        self.bicicletas = bicicletas
        self.comidas = comidas
        self.materiales_papeleria = materiales_papeleria

    def limpiar_pantalla(self):
        os.system("cls" if os.name == "nt" else "clear")

    def animar_texto(self, texto):
        for caracter in texto:
            print(caracter, end="", flush=True)
            time.sleep(0.003)
        print()

    def mostrar_tabla_ascii(self, datos):
        # Encabezado de la tabla
        self.animar_texto("+-------------------------------------------+")
        self.animar_texto("|               Menú Principal              |")
        self.animar_texto("+-------------------------------------------+")

        # Contenido de la tabla
        for opcion in datos:
            print(f"| {opcion:<41} |")

        # Pie de la tabla
        self.animar_texto("+-------------------------------------------+")

    def mostrar_menu_administrador(self):
        self.limpiar_pantalla()
        opciones_menu_administrador = [
            "1. Ver informes y análisis",
            "2. Agregar recursos",
            "3. Salir",
        ]

        while True:
            self.animar_texto("\nMenú Administrador:")
            self.mostrar_tabla_ascii(opciones_menu_administrador)

            eleccion = input("Seleccione una opción (1-3): ")

            if eleccion == "1":
                self.limpiar_pantalla()
                self.animar_texto(
                    f"Han sido alquiladas {self.contador_computadoras} computadoras"
                )
                self.animar_texto(
                    f"Han sido alquiladas {self.contador_bicicletas} bicicletas"
                )
                self.animar_texto(f"Han sido compradas {self.contador_comidas} comidas")
                self.animar_texto(
                    f"Han sido comprados {self.contador_materiales} materiales"
                )
            elif eleccion == "2":
                self.limpiar_pantalla()
                opciones_agregar = [
                    "1. Computador",
                    "2. Bicicleta",
                    "3. Comida",
                    "4. Material de papeleria",
                ]
                self.mostrar_tabla_ascii(opciones_agregar)
                nueva_eleccion = input("Seleccione una opcion (1-4): ")
                if nueva_eleccion == "1":
                    computador_nuevo = input(
                        "Ingrese el modelo del computador a agregar: "
                    )
                    ram_computador = input(
                        "Ingrese la cantidad de ram del computador: "
                    )
                    almacenamiento_computador = input(
                        "Ingrese el almacenamiento del computador: "
                    )
                    precio_computador = int(input("Ingrese su precio: "))
                    self.agregar_computadora(
                        computador_nuevo,
                        ram_computador,
                        almacenamiento_computador,
                        precio_computador,
                    )
                elif nueva_eleccion == "2":
                    bicicleta_nueva = input("Ingrese el tipo de bicicleta a agregar: ")
                    precio_bicicleta = int(input("Ingrese el precio de la bicicleta: "))
                    self.agregar_bicicleta(bicicleta_nueva, precio_bicicleta)
                elif nueva_eleccion == "3":
                    comida_nueva = input("Ingrese el nombre de la comida a agregar: ")
                    precio_comida = int(input("Ingrese su precio: "))
                    self.agregar_comida(comida_nueva, precio_comida)
                elif nueva_eleccion == "4":
                    material_nuevo = input(
                        "Ingrese el nombre del material de papeleria a agregar: "
                    )
                    precio_material = int(input("Ingrese su precio: "))
                    self.agregar_material_papeleria(material_nuevo, precio_material)

            elif eleccion == "3":
                self.limpiar_pantalla()
                self.animar_texto("Cerrando sesion...")
                time.sleep(1)
                break
            else:
                self.animar_texto(
                    "Opción no válida. Por favor, elija una opción válida."
                )
            input("Presiona Enter para continuar...")

    def agregar_computadora(self, modelo, ram, almacenamiento, precio):
        nueva_computadora = {
            "modelo": modelo,
            "ram": ram,
            "almacenamiento": almacenamiento,
            "precio": precio,
        }
        self.computadores.append(nueva_computadora)
        self.contador_computadoras += 1

    def agregar_bicicleta(self, tipo, precio):
        nueva_bicicleta = {"tipo": tipo, "precio": precio}
        self.bicicletas.append(nueva_bicicleta)
        self.contador_bicicletas += 1

    def agregar_comida(self, nombre, precio):
        nueva_comida = {"nombre": nombre, "precio": precio}
        self.comidas.append(nueva_comida)
        self.contador_comidas += 1
        self.animar_texto(
            f"¡Se ha agregado la siguiente comida:\nNombre: {nombre}\nPrecio: ${precio}"
        )

    def agregar_material_papeleria(self, nombre, precio):
        nuevo_material = {"nombre": nombre, "precio": precio}
        self.materiales_papeleria.append(nuevo_material)
        self.contador_materiales += 1
        self.animar_texto(
            f"¡Se ha agregado el siguiente material de papelería:\nNombre: {nombre}\nPrecio: ${precio}"
        )
