from flask import Blueprint, request
from src.productos.infrestructure.controllers.GetProductosController import GetProductosController
from src.productos.infrestructure.controllers.DeleteProductosController import DeleteProductosController
from src.productos.infrestructure.controllers.CreateProductosController import CreateProductosController
from src.productos.infrestructure.repositories.MySQLProductosRepository import ProductosRepository

product_routes = Blueprint('product_routes', __name__)

repo = ProductosRepository()
get_controller = GetProductosController(repo)
delete_controller = DeleteProductosController(repo)
create_controller = CreateProductosController(repo)

@product_routes.route("/", methods=["GET"])
def get():
    return get_controller.run()

@product_routes.route("/", methods=["POST"])
def create():
    return create_controller.run(request)

@product_routes.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return delete_controller.run(id)
