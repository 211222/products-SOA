from src.productos.domain.ports.ProductosPort import ProductosPort as Port, Productos


class CreateProductoUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def run(self, data):
        productos = [Productos(**d) for d in data]
        return self.__repository.create_n_productos(productos)
