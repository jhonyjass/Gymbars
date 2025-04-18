from repositories.reportes_repo import ReportesRepository


class ReporteService:


    @staticmethod
    def obtener_ingresos_recibidos():
        return ReportesRepository.ingresos_por_mes()

    @staticmethod
    def obtener_porcentajes_tipos_pago():
        return ReportesRepository.porcentaje_por_tipo_pago()
    
    @staticmethod
    def obtener_suscrip_activas_inactivas():
        return ReportesRepository.contar_suscripciones_estado()