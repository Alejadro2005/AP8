from tiendalibros.modelo.libro_error import LibroError

class LibroAgotadoError(LibroError):
    def __init__(self, titulo, isbn):
        mensaje = (
            f"El libro con título '{titulo}' y ISBN '{isbn}' está agotado."
        )
        super().__init__(mensaje)

    def __str__(self):
        return self.args[0]
