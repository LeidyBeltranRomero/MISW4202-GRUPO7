from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import hashlib

from modelos import \
    db, \
    OrdenCompra, Product, Cliente, \
    OrdenCompraSchema, ProductSchema, ClienteSchema

orden_compra_schema = OrdenCompraSchema()
product_schema = ProductSchema()
cliente_schema = ClienteSchema()

class VistaOrdenCompra(Resource):
      
   def get(self, id_orden_compra):
        return orden_compra_schema.dump(OrdenCompra.query.get_or_404(id_orden_compra))

class VistaOrdenesCompra(Resource):
    
   def get(self):
        ordenes = OrdenCompra.query.all()
        return [orden_compra_schema.dump(orden) for orden in ordenes]
   
   def post(self):
        nueva_orden = OrdenCompra(\
            cliente = request.json["cliente"], \
            product = request.json["product"], \
            quantity = request.json["quantity"], \
            state = request.json["state"], \
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return orden_compra_schema.dump(nueva_orden)