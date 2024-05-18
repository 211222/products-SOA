from src.database.MySQL import Base, engine, session_local
from src.productos.domain.ports.ProductosPort import ProductosPort
from src.productos.domain.entities.Productos import Productos
from src.productos.infrestructure.models.MySQLProductosModel import Productos as Model
from src.productos.infrestructure.dtos.responses.BaseResponse import BaseResponse


class ProductosRepository(ProductosPort):
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()

    def get_productos(self):
        productos = [p.to_dict() for p in self.db.query(Model).all()]
        status = True if productos else False
        message = "productos encontrados exitosamente" if status else "productos no encontrados"
        status_code = 200 if status else 500
        return self.generate_response(productos, message, status, status_code)

    def create_n_productos(self, productos: list[Productos]):
        news = [Model(**producto.__dict__) for producto in productos]
        [self.db.add(new) for new in news]
        self.db.commit()
        responses = [n.to_dict() for n in news]
        return self.generate_response(responses, "Producto creado", True, 201)

    def delete_productos(self, id):
        producto = self.db.query(Model).filter(Model.id == id).first()
        status = True
        status_code = 200
        message = "Producto eliminado "
        if producto:
            self.db.delete(producto)
            self.db.commit()
        else:
            status = False
            message = "Producto no encontrado"
            status_code = 500
        return {"message": message, "status": status}, status_code

    def generate_response(self, data, message, status, httpsstatuscode):
        return BaseResponse(data, message, status, httpsstatuscode).response()
