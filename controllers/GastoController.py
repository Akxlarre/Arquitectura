from services.GastoService import GastoService

class GastoController:
    @staticmethod
    def generar_gasto_controller(departamentos, periodo, monto):
        GastoService.generar_gasto(departamentos, periodo, monto)
    
    @staticmethod
    def marcar_como_pagado_controller(departamento, periodo, fecha_pago):
        return GastoService.marcar_como_pagado(departamento, periodo, fecha_pago)
    
    @staticmethod
    def obtener_gastos_pendientes_controller(mes, anio):
        return GastoService.obtener_gastos_pendientes(mes, anio)
