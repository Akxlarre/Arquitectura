from flask import Flask
from views.GastoView import gasto_blueprint  
from app import create_app

app = create_app()

# Registrar el blueprint
app.register_blueprint(gasto_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
