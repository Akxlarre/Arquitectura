from flask import Blueprint, request, jsonify
from controllers.GastoController import GastoController

gasto_blueprint = Blueprint('gasto_blueprint', __name__)

class GastoView:
    @staticmethod
    @gasto_blueprint.route('/gastos/generar', methods=['POST'])
    def generar_gasto():
        # Obtener los datos del cuerpo de la solicitud
        data = request.get_json()
        departamentos = data.get('departamentos')
        periodo = data.get('periodo')
        monto = data.get('monto')
        
        GastoController.generar_gasto_controller(departamentos, periodo, monto)
        return jsonify({"mensaje": "Gastos generados exitosamente"}), 201

    @staticmethod
    @gasto_blueprint.route('/gastos/marcar-pagado', methods=['POST'])
    def marcar_como_pagado():
        data = request.get_json()
        departamento = data.get('departamento')
        periodo = data.get('periodo')
        fecha_pago = data.get('fecha_pago')  # Esperamos la fecha en formato YYYY-MM-DD
        
        fecha_pago = datetime.strptime(fecha_pago, "%Y-%m-%d")
        gasto = GastoController.marcar_como_pagado_controller(departamento, periodo, fecha_pago)
        
        if gasto:
            return jsonify({
                "mensaje": "Pago exitoso",
                "gasto": gasto.serialize()
            }), 200
        else:
            return jsonify({"mensaje": "Pago no encontrado o ya marcado como pagado"}), 404
    
    @staticmethod
    @gasto_blueprint.route('/gastos/pendientes', methods=['GET'])
    def obtener_gastos_pendientes():
        mes = request.args.get('mes', type=int)
        anio = request.args.get('anio', type=int)
        
        gastos = GastoController.obtener_gastos_pendientes_controller(mes, anio)
        if gastos:
            gastos_list = [gasto.serialize() for gasto in gastos]
            return jsonify({"gastos": gastos_list}), 200
        else:
            return jsonify({"mensaje": "Sin montos pendientes"}), 404
