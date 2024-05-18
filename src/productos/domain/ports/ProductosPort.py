from src.productos.domain.entities.Productos import Productos
from abc import ABC, abstractmethod


class ProductosPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_productos(self):
        pass

    @abstractmethod
    def create_n_productos(self, productos: list[Productos]):
        pass

    @abstractmethod
    def delete_productos(self, id):
        pass
