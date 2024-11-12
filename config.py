import os

class Config:
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db_gastos.db')  # Para desarrollo local con SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False