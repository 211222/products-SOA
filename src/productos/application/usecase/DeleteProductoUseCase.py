from src.productos.domain.ports.ProductosPort import ProductosPort as Port


class DeleteProductoUseCase:
    def __init__(self, repository: Port):
        self.__repository = repository

    def run(self, id):
        return self.__repository.delete_productos(id)

