from datetime import datetime
import socket
from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

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

class RHC(Resource):
    count = 0
class VistaModifyHC1(RHC):
    def get(self):
        nueva_orden = OrdenCompra(\
            cliente = 1, \
            product = 1, \
            quantity = 2, \
            state = "OK", \
        )
        db.session.add(nueva_orden)
        db.session.commit()
        return "OK"
    
class VistaHealthCheck(RHC):
   def get(self):
        now = datetime.now()
        ordenes = OrdenCompra.query.all()
        if len(ordenes) %2 == 0:
            return "OK "+str(now.second)+" - "+socket.gethostname()+" COUNT:"+str(len(ordenes)), 200
        else:
            return "Fail "+str(now.second)+" - "+socket.gethostname()+" COUNT:"+str(len(ordenes)),500