from src.productos.application.usecase.CreateProductoUseCase import CreateProductoUseCase as UseCase, Port


class CreateProductosController:
    def __init__(self, repository:Port):
        self.__use_case = UseCase(repository)

    def run(self, request):
        return self.__use_case.run(request.get_json())
