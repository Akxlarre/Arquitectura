from app import create_app
from views.GastoView import gasto_común_blueprint  

app = create_app()

# Registrar los blueprints
app.register_blueprint(gasto_común_blueprint)  
if __name__ == '__main__':
    # Ejecutar la aplicación con el modo de depuración activado
    app.run(debug=True)
