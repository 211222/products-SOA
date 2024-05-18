from src.database.MySQL import Base
from sqlalchemy import Column, String, Integer, Float


class Productos(Base):
    __tablename__ = 'product'
    id = Column(String(36), primary_key=True)
    nombre = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock
        }
