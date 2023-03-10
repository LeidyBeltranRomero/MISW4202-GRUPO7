from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from modelos import db
from vistas import \
    VistaOrdenCompra, VistaOrdenesCompra, VistaHealthCheck, VistaModifyHC1

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaOrdenesCompra, '/ordenes')
api.add_resource(VistaOrdenCompra, '/orden/<int:id_orden_compra>')
api.add_resource(VistaHealthCheck, '/healthcheck')
api.add_resource(VistaModifyHC1, '/1')

jwt = JWTManager(app)
