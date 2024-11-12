from app import db

class Gasto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    departamento = db.Column(db.String(10), nullable=False)  # Por ejemplo: '1305'
    periodo = db.Column(db.String(10), nullable=False)  # Por ejemplo: '2024-10'
    monto = db.Column(db.Float, nullable=False)  # Monto del gasto común
    estado = db.Column(db.String(20), nullable=False, default='pendiente')  # Estado del pago (pendiente, pagado)
    fecha_pago = db.Column(db.Date)  # Fecha de pago, si está marcado como pagado

    def serialize(self):
        return {
            'id': self.id,
            'departamento': self.departamento,
            'periodo': self.periodo,
            'monto': self.monto,
            'estado': self.estado,
            'fecha_pago': self.fecha_pago
        }
