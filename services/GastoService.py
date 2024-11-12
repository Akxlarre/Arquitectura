from models.GastoModel import db, Gasto
from datetime import datetime

class GastoService:
    @staticmethod
    def generar_gasto(departamentos, periodo, monto):
        # Generar un gasto común para cada departamento
        for dep in departamentos:
            gasto = Gasto(departamento=dep, periodo=periodo, monto=monto)
            db.session.add(gasto)
        db.session.commit()

    @staticmethod
    def marcar_como_pagado(departamento, periodo, fecha_pago):
        # Buscar el gasto por departamento y periodo
        gasto = Gasto.query.filter_by(departamento=departamento, periodo=periodo, estado='pendiente').first()
        if gasto:
            gasto.estado = 'pagado'
            gasto.fecha_pago = fecha_pago
            db.session.commit()
            return gasto
        return None

    @staticmethod
    def obtener_gastos_pendientes(mes, anio):
        # Obtener todos los gastos pendientes de un determinado mes y año
        periodo = f"{anio}-{mes:02d}"
        return Gasto.query.filter_by(periodo=periodo, estado='pendiente').order_by(Gasto.periodo).all()
