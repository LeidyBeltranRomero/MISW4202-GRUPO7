from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class OrdenCompra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.Integer)
    product = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    state = db.Column(db.String(100))

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    referecncia = db.Column(db.String(50))
    value = db.Column(db.Integer)
    perecedero = db.Column(db.Boolean)
    fragil = db.Column(db.Boolean)
    stock = db.Column(db.Integer)

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)


class OrdenCompraSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrdenCompra
        include_relationships = True
        include_fk = True
        load_instance = True
        
    id = fields.String()
    quantity = fields.String()
    state = fields.String()


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_relationships = True
        include_fk = True
        load_instance = True
        
    id = fields.String()
    name = fields.String()
    description = fields.String()
    referecncia = fields.String()
    value = fields.String()
    perecedero = fields.String()
    fragil = fields.String()
    stock = fields.String()

class ClienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        include_relationships = True
        include_fk = True
        load_instance = True
        
    id = fields.String()
    name = fields.String()
