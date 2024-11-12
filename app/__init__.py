from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Instancia de SQLAlchemy
db = SQLAlchemy()

# Singleton para inicializar la base de datos
class SingletonDB:
    _instance = None

    def __new__(cls, app=None):
        if cls._instance is None:
            cls._instance = super(SingletonDB, cls).__new__(cls)
            cls._instance.init_app(app)
        return cls._instance

    def init_app(self, app):
        if app is not None:
            db.init_app(app)  # Se inicializa la base de datos con la app

def create_app():
    app = Flask(__name__)

    # Cargar configuración desde el archivo de configuración
    app.config.from_object('config.Config')

    # Instancia del SingletonDB
    SingletonDB(app)

    # Definir el contexto de la aplicación
    with app.app_context():
        # Importar modelos y crear las tablas
        from models.GastoModel import Gasto
        db.create_all()  # Crear todas las tablas en la base de datos

    return app
