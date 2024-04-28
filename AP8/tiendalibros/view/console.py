import sys
from tiendalibros.modelo.tienda_libros import TiendaLibros
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError


class UIConsola:
    def __init__(self):
        self.tienda_libros = TiendaLibros()  # Instancia de TiendaLibros
        self.opciones = {
            "1": self.adicionar_un_libro_a_catalogo,
            "2": self.agregar_libro_a_carrito_de_compras,
            "3": self.retirar_libro_de_carrito_de_compras,
            "4": self.salir,
        }

    @staticmethod
    def salir():
        print("\nGRACIAS POR VISITAR NUESTRA TIENDA DE LIBROS. VUELVA PRONTO")
        sys.exit(0)

    @staticmethod
    def mostrar_menu():
        titulo = "¡Tienda de Libros!"
        print(f"\n{titulo:_^30}")
        print("1. Adicionar un libro al catálogo")
        print("2. Agregar libro al carrito de compras")
        print("3. Retirar libro del carrito de compras")
        print("4. Salir")
        print(f"{'_':_^30}")

    def ejecutar_app(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida.")

    def retirar_libro_de_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a retirar del carrito: ")
        try:
            self.tienda_libros.retirar_item_de_carrito(isbn)
            print("Libro retirado del carrito con éxito.")
        except ValueError:
            print("El libro con el ISBN ingresado no está en el carrito.")

    def agregar_libro_a_carrito_de_compras(self):
        isbn = input("Ingrese el ISBN del libro a agregar al carrito: ")
        cantidad = int(input("Ingrese la cantidad de unidades a agregar: "))
        try:
            self.tienda_libros.agregar_libro_a_carrito(isbn, cantidad)
            print("Libro agregado al carrito con éxito.")
        except LibroAgotadoError as e:
            print("Error:", str(e))
        except ExistenciasInsuficientesError as e:
            print("Error:", str(e))
        except ValueError as e:
            print("Error:", str(e))
        except Exception as e:
            print("Error desconocido:", str(e))

    def adicionar_un_libro_a_catalogo(self):
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        precio = float(input("Ingrese el precio del libro: "))
        existencias = int(input("Ingrese la cantidad de existencias del libro: "))
        try:
            self.tienda_libros.adicionar_libro_a_catalogo(isbn, titulo, precio, existencias)
            print("Libro adicionado al catálogo con éxito.")
        except LibroExistenteError as e:
            print("Error:", str(e))
        except Exception as e:
            print("Error desconocido:", str(e))
