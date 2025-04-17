from flask_apscheduler import APScheduler
from services.suscrip_service import SuscripcionesService

scheduler = APScheduler()

def init_scheduler(app):
    scheduler.init_app(app)

    # @scheduler.task('interval', id='tarea_mensualidades',seconds=10)
    @scheduler.task('cron', id='tarea_mensualidades', hour=00, minute=5)
    def generar_mensualidades():
        with app.app_context():
            SuscripcionesService.generar_mensualidades_del_mes()
            print("Proceso ejecutado")

    scheduler.start()
