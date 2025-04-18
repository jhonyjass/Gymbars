from flask import render_template, current_app
from resend import Emails
from decouple import config
import resend

resend.api_key = config("RESEND_API_KEY")
emisor = config("EMISOR_EMAIL")

def enviar_correo_plantilla(to, subject, template_name, context):
    with current_app.app_context():
        html_content = render_template(template_name, **context)
        return Emails.send({
            "from": emisor,
            "to": [to],
            "subject": subject,
            "html": html_content
        })


def enviar_correo_mensualidad(cliente, fecha_inicio, fecha_final, cantidad):
    subject = "Nueva mensualidad"
    context = {
        "cliente": cliente,
        "fecha_inicio": fecha_inicio.strftime("%d-%m-%Y"),
        "fecha_final": fecha_final.strftime("%d-%m-%Y"),
        "cantidad": f"Q{float(cantidad):,.2f}"
    }
    return enviar_correo_plantilla(cliente.correo, subject, "correos/correo_mensualidad.html", context)


def enviar_correo_bienvenida(cliente):
    subject = "bienvenida a Gymbars"

    context ={
        "cliente": cliente
    }
    return enviar_correo_plantilla(cliente.correo, subject, "correos/correo_bienvenida.html", context)