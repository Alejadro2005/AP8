from tiendalibros.modelo.libro_error import LibroError

class ExistenciasInsuficientesError(LibroError):
    def __init__(self, libro, cantidad_a_comprar):
        mensaje = (
            f"El libro con título '{libro.titulo}' y ISBN '{libro.isbn}' "
            f"no tiene suficientes existencias para la compra: "
            f"cantidad a comprar: {cantidad_a_comprar}, existencias: {libro.existencias}."
        )
        super().__init__(mensaje)
        self.cantidad_a_comprar = cantidad_a_comprar

    def __str__(self):
        return self.args[0]

