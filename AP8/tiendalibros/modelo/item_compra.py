from tiendalibros.modelo.libro import Libro

class ItemCompra:
    def __init__(self, libro, cantidad):
        if not isinstance(libro, Libro):
            raise ValueError("El primer parámetro debe ser un objeto de la clase Libro")
        if not isinstance(cantidad, int) or cantidad < 1:
            raise ValueError("La cantidad debe ser un entero positivo")
        self.libro = libro
        self.cantidad = cantidad

    def calcular_subtotal(self):
        return self.cantidad * self.libro.precio
