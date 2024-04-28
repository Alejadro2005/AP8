from tiendalibros.modelo.libro_error import LibroError

class LibroExistenteError(LibroError):
    def __init__(self, isbn):
        mensaje = f"El libro con ISBN '{isbn}' ya existe en el catálogo."
        super().__init__(mensaje)

    def __str__(self):
        # Devuelve una representación como cadena del error
        return f"El libro con ISBN '{isbn}' ya existe en el catálogo."
